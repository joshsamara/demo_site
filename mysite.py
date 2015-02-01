import cherrypy
import os


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
    cherrypy.config.update({'server.socket_host': '0.0.0.0', })
    cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '8080')), })
    cherrypy.quickstart(MySite())
