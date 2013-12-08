import tornado.ioloop as ioloop
import tornado.options
import tornado.web as web
import app.settings

tornado.options.parse_command_line()  # logging
application = web.Application(app.settings.handlers, debug=True)

if __name__ == "__main__":
    application.listen(8888)
    print('listen 8888...')
    ioloop.IOLoop.instance().start()
