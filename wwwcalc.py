import web
from datetime_calculator import Datecalc

calc = Datecalc()

urls = (
    '/', 'index'
)


class index:
    def GET(self):
        return calc.mo12('ilya')

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()