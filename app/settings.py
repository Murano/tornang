import app.handlers as handlers


handlers = [
    (r'/static/(.*)', handlers.StaticHandler, {'path': 'static'}),
    (r'/', handlers.IndexHandler),
    (r'/chat', handlers.MainChatHandler)
]
