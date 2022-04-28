

from flask import flask
from web app.routes.home_routes import home_routes
from web app.routes.home_routes import book_routes




def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    app.register_blueprint(weather_routes)
    return app



if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
    
