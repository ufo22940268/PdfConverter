#coding:utf-8
import tornado.web
import tornado.ioloop
from tornado.template import Template
from tornado.template import Loader
import logging
import util
import parser
import json
import re
import urllib
import traceback
from util import log
import os
import file_parser

logger = logging.getLogger("test");
class MainHandler(tornado.web.RequestHandler):
    def get(self):
	loader = Loader("./");
	self.write(loader.load("index.html").generate());

class UploadHandler(tornado.web.RequestHandler):

    def post(self):
        try:
            #util.log(self.get_argument("id", default="0"));
            #file1 = self.request.files['files[]'][0];
            #f = file1['body'];
            #open("a.pdf", "w").write(f);
            #os.system("pdf2txt.py -o a.txt a.pdf");

            blocks = file_parser.parseToBlocks("a.txt");
            jo = json.dumps(map(lambda b : b.encode("utf-8"), blocks), ensure_ascii=False);
            self.write(jo);
        except:
            pass;

    def get(self):
        self.post();


application = tornado.web.Application([
    (r"/pdf_converter", MainHandler),
    (r"/css/(.*)", tornado.web.StaticFileHandler, {"path": "./css/"}),
    (r"/js/(.*)", tornado.web.StaticFileHandler, {"path": "./js/"}),
    (r"/js/vendor/(.*)", tornado.web.StaticFileHandler, {"path": "./js/"}),
    (r"/img/(.*)", tornado.web.StaticFileHandler, {"path": "./img/"}),
    (r"/server/(.*)", tornado.web.StaticFileHandler, {"path": "./server/"}),
    (r"/cors/(.*)", tornado.web.StaticFileHandler, {"path": "./cors/"}),
    (r"/upload", UploadHandler),
    ]);

if __name__ == "__main__":
    application.listen(8885)
    tornado.ioloop.IOLoop.instance().start()
