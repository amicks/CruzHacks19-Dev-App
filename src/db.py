from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4

db = SQLAlchemy()

def query_to_dict(query):
    return dict((col, getattr(query, col)) for col in query.__table__.columns.keys())

def get_query_res(db_model, **kwargs):
    """ Returns all kwarg matches in DB model as a list """
    return db_model.query.filter_by(**kwargs).all()


class Hackers(db.Model):
    __tablename__ = 'hackers'

    # IDs
    private_id = db.Column('private_id', db.String(36), primary_key=True)
    public_id = db.Column('public_id', db.Integer, unique=True, nullable=False)
    team_id = db.Column('team_id', db.Integer, nullable=True)
    
    # About
    first_name = db.Column('first_name', db.String(32), nullable=False)
    last_name = db.Column('last_name', db.String(32), nullable=False)
    email = db.Column('email', db.String(64), unique=True, nullable=False)
    gender = db.Column('gender', db.String(32), nullable=True)
    age = db.Column('age', db.Integer, nullable=False)
    
    # Logistics
    #   Could also have skills and health restriction tables/models to filter
    #   between teams if people want to join one, or decide what food to purchase.
    needs_transportation = db.Column('needs_transportation', db.Boolean, nullable=False)
    rsvp_status = db.Column('rsvp_status', db.Boolean, nullable=True) # Accepted (True), Rejected (False)
    app_status = db.Column('app_status', db.Boolean, nullable=True) # Accepted (True), Rejected (False)
    shirt_size = db.Column('shirt_size', db.String(2), nullable=False) # S/M/L/XL

    # Education
    university = db.Column('university', db.String(64), nullable=True)
    class_year = db.Column('class_year', db.Integer, nullable=True)

    def __init__(self, first_name, last_name, email, age, needs_transportation, rsvp_status, app_status,
                 shirt_size, gender=None, team_id=None, university=None, class_year=None):
        
        # For every function parameter, initialize its respective column
        for arg, val in locals().items():
            setattr(self, arg, val)
        
        # Still need public ID and private ID, generate them from unique email
        guid = uuid4()
        self.private_id = str(guid)
        
        CONVERT_128_TO_16_BITS = 112
        self.public_id = guid.int >> CONVERT_128_TO_16_BITS
