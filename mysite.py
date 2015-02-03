import cherrypy
import os


class MySite(object):
    @cherrypy.expose
    def index(self):
        return """<html>
<head>
    <title>Cat Hats</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
</head>
<html>
    <body>
    <div class="container">
        <!-- Static navbar -->
        <nav class="navbar navbar-default">
            <div class="container-fluid">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="#">Cat Hats</a>
            </div>
            <div id="navbar" class="navbar-collapse collapse">
                <ul class="nav navbar-nav">
                <li class="active"><a href="#">Home</a></li>
                <li><a href="#">Cats</a></li>
                <li><a href="#">Hats</a></li>
                <li><a href="#">Ties</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Contact</a></li>
                </ul>
                <ul class="nav navbar-nav navbar-right">
                </ul>
            </div><!--/.nav-collapse -->
            </div><!--/.container-fluid -->
        </nav>
      <div class="page-header"><h1>Cat Hats  <small>They deserve your $</small></h1></div>
      <div class="alert alert-info" role="alert">Heads Up! This Cat has a Tie too!</div>
      <div class="jumbotron">
            <img class="img-rounded" src="http://i.imgur.com/ogXW5uf.jpg" style="border-radius: 150px; height: 300px;"><br/>
            <blockquote>
                  <p>Cats with hats ... what a genius genius idea.</p>
                    <footer>George Washington <cite title="Source Title">The Declaration of Independence.</cite></footer>
            </blockquote>
            <button type="button" class="btn btn-success">Give Money</button>
        </p>
      </div>
    </div>
</body>
</html>
"""

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0', })
    cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '8080')), })
    cherrypy.quickstart(MySite())
