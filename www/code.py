import web

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        return "Hello, ilya!"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()