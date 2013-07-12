#coding:utf-8
import tornado.web
import tornado.ioloop
from tornado.template import Template
from tornado.template import Loader
import parser
import os
import random
import tornado.httpserver, tornado.ioloop, tornado.options, tornado.web, os.path, random, string

class MainHandler(tornado.web.RequestHandler):
    def get(self):
	loader = Loader("./");
	self.write(loader.load("index.html").generate());

class ParserHandler(tornado.web.RequestHandler):
  def put(self, params):
        path = calculate_path(params)
        with open(path, 'wb') as out:
            body = self.request.get_argument('data')
            out.write(bytes(body, 'utf8'))        

class UploadHandler(tornado.web.RequestHandler):
    def post(self):
        file1 = self.request.files['file1'][0]
        original_fname = file1['filename']
        extension = os.path.splitext(original_fname)[1]
        fname = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(6))
        final_filename= fname+extension
        output_file = open("a.apk", 'w')
        output_file.write(file1['body'])
        output_file.close();
	self.finish("渠道名字是" + parser.parseChannel())

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/assets/css/(.*)", tornado.web.StaticFileHandler, {"path": "./assets/css/"}),
    (r"/assets/js/(.*)", tornado.web.StaticFileHandler, {"path": "./assets/js/"}),
    (r"/assets/img/(.*)", tornado.web.StaticFileHandler, {"path": "./assets/img/"}),
    (r"/upload", UploadHandler),
    ]);

if __name__ == "__main__":
    application.listen(8887)
    tornado.ioloop.IOLoop.instance().start()
