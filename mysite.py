import cherrypy


class MySite(object):
    @cherrypy.expose
    def index(self):
        return """ <html>
    <head>
        <title>Cat Hats</title>
    </head>
    <html>
    <body>
        <h1>Cat Hats</h1>
        <img src="http://i.imgur.com/ogXW5uf.jpg">
    </body>
    </html>"""

if __name__ == '__main__':
    cherrypy.quickstart(MySite())
