#!/usr/bin/python3
"""
Very simple HTTP server for logging requests
Usage::
    ./server.py [<port>]
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import sys

class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        log = "GET %s\n%s\n" % (str(self.path), str(self.headers))
        logging.info(log)
        print ("%s -- [%s]\n" %(self.client_address[0],self.log_date_time_string()))
        print (log)
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        log = "POST %s\n%s\n%s\n" % (str(self.path), str(self.headers), post_data.decode('utf-8'))
        logging.info(log)
        print ("%s -- [%s]\n" %(self.client_address[0],self.log_date_time_string()))
        print (log.encode('utf-8'))
        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        sys.stdout = open('httplog.txt', 'a', 1)
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')
    sys.stdout.close()
    sys.stdout = sys.__stdout__

if __name__ == '__main__':
    from sys import argv
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run(port=80)
