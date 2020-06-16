import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
import json

database_name = "casino_bank"
database_path = ""

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
    !!NOTE you can change the database_filename variable to have multiple verisons of a database
'''
def db_drop_and_create_all():
    db.drop_all()
    db.create_all()

'''
Jeton
a persistent jeton entity, extends the base SQLAlchemy Model
'''
class Jeton(db.Model):
    __tablename__ = 'jetons'

    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    user_id = Column(String, unique=True)
    jeton_ammount =  Column(Integer, nullable=False)

    '''
    format()
        representation of the Jeton model
    '''
    def format(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'jeton_ammount': self.jeton_ammount
        }

    '''
    insert()
        inserts a new model into a database
        the model must have a unique name
        the model must have a unique id or null id
        EXAMPLE
            jeton = Jeton(user_id=req_user_id, jeton_ammount=req_jeton_ammount)
            jeton.insert()
    '''
    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    delete()
        deletes a new model into a database
        the model must exist in the database
        EXAMPLE
            jeton = Jeton(user_id=req_user_id, jeton_ammount=req_jeton_ammount)
            jeton.delete()
    '''
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    update()
        updates a new model into a database
        the model must exist in the database
        EXAMPLE
            jeton = Jeton.query.filter(Jeton.id == id).one_or_none()
            jeton.jeton_ammount = 20000
            jeton.update()
    '''
    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.short())