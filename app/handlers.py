import tornado.web as web
import tornado.escape
import time
import uuid
from app import message


class StaticHandler(web.StaticFileHandler):
    pass


class IndexHandler(web.RequestHandler):
    def get(self):
        self.render('templates/index.html')


#########Chat handlers####################
global_message_buffer = message.MessageBuffer()

class BaseChatHandler(web.RequestHandler):
    pass


class MainChatHandler(BaseChatHandler):
    def get(self):
        self.render('templates/chat.html')


class MessageNewHandler(BaseChatHandler):

    def post(self):
        message = {
            "id": str(uuid.uuid4()),
            "from": self.current_user["first_name"],
            "body": self.get_argument("body"),
            "time": time.strftime("%d %b %Y %H:%M:%S")
        }
        # to_basestring is necessary for Python 3's json encoder,
        # which doesn't accept byte strings.
        message["html"] = tornado.escape.to_basestring(
            self.render_string("message.html", message=message))
        if self.get_argument("next", None):
            self.redirect(self.get_argument("next"))
        else:
            self.write(message)
        global_message_buffer.new_messages([message])


class MessageUpdatesHandler(BaseChatHandler):
    @tornado.web.authenticated
    @tornado.web.asynchronous
    def post(self):
        cursor = self.get_argument("cursor", None)
        global_message_buffer.wait_for_messages(self.on_new_messages,
                                                cursor=cursor)

    def on_new_messages(self, messages):
        # Closed client connection
        if self.request.connection.stream.closed():
            return
        self.finish(dict(messages=messages))

    def on_connection_close(self):
        global_message_buffer.cancel_wait(self.on_new_messages)
