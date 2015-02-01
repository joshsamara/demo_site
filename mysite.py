import cherrypy
import os


class MySite(object):
    pass

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0', })
    cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '8080')), })
    cherrypy.quickstart(MySite())
