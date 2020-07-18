from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()


def create_app():
    
    app = Flask(__name__)
    CORS(app)
    #cors = CORS(app, resources={r"/customers/*": {"origins": "*"}})
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:PruebA01@localhost:5432/postgres'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    
    db.init_app(app)

    with app.app_context():
        from back.routes import customer, socket, measurer
        db.create_all()  
        return app