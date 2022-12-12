# Register Blueprints/Views.
from application.extensions import jinja

def init_views(app):
    import application.controllers.user
    import application.controllers.api
    # app.blueprint(upload)

    @app.route('/')
    def index(request):
        return jinja.render('index.html', request)
    
    