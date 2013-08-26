import tornado.web as web
import tornado.escape
import json
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
    def get_current_user(self):
        return {"first_name": "Ivanov"}
        # user_json = self.get_secure_cookie("chatdemo_user")
        # if not user_json: return None
        # return tornado.escape.json_decode(user_json)


class MainChatHandler(BaseChatHandler):
    def get(self):
        self.render('templates/chat.html')


class MessageNewHandler(BaseChatHandler):

    def post(self):
        # self.arguments = json.json_decode(self.request.body)
        # json.
        arguments = json.loads(self.request.body)
        message = {
            "id": str(uuid.uuid4()),
            "from": self.current_user["first_name"],
            "body": arguments["body"],
            "time": time.strftime("%d %b %Y %H:%M:%S")
        }

        # print message
        # to_basestring is necessary for Python 3's json encoder,
        # which doesn't accept byte strings.
        # message["html"] = tornado.escape.to_basestring(
        #     self.render_string("message.html", message=message))
        if self.get_argument("next", None):
            self.redirect(self.get_argument("next"))
        else:
            self.write(message)
        global_message_buffer.new_messages([message])


class MessageUpdatesHandler(BaseChatHandler):
    @tornado.web.asynchronous
    def get(self, cursor):
        # print self.request.body
        # arguments = json.loads(self.request.body)
        # cursor = arguments["cursor"]
        global_message_buffer.wait_for_messages(self.on_new_messages,
                                                cursor=cursor)

    def on_new_messages(self, messages):
        # Closed client connection
        if self.request.connection.stream.closed():
            return
        self.finish(dict(messages=messages))

    def on_connection_close(self):
        global_message_buffer.cancel_wait(self.on_new_messages)
