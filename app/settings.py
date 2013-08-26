import app.handlers as handlers


handlers = [
    (r'/static/(.*)', handlers.StaticHandler, {'path': 'static'}),
    (r'/', handlers.IndexHandler),
    (r'/chat', handlers.MainChatHandler),
    (r"/a/message/new", handlers.MessageNewHandler),
    (r"/a/message/updates/(.*)", handlers.MessageUpdatesHandler)
]
