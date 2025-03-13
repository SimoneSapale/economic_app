from flask import Flask
from app.models.database import db, init_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///latvian_economy.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

from app.routes import register_routes
register_routes(app)

with app.app_context():
    init_db()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
