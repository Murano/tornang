import tornado.web as web


class StaticHandler(web.StaticFileHandler):
    pass


class IndexHandler(web.RequestHandler):
    def get(self):
        self.render('templates/index.html')


#########Chat handlers####################

class BaseChatHandler(web.RequestHandler):
    pass


class MainChatHandler(BaseChatHandler):
    def get(self):
        self.render('templates/chat.html')