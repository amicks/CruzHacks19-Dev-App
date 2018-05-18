from flask_sqlalchemy import SQLAlchemy
from uuid import uuid5, NAMESPACE_URL
db = SQLAlchemy()

class Hackers(db.Model):
    __tablename__ = 'hackers'
    
    # IDs
    private_id = db.Column('private_id', db.String(36), primary_key=True)
    public_id = db.Column('public_id', db.Integer, nullable=False, unique=True)
    team_id = db.Column('team_id', db.Integer)
    
    # Contact
    first_name = db.Column('first_name', db.String(32), nullable=False)
    last_name = db.Column('last_name', db.String(32), nullable=False)
    email = db.Column('email', db.String(64), nullable=False, unique=True)
    gender = db.Column('gender', db.String(32))
    
    # Logistics
    #   Could also have skills and health restriction tables/models to filter
    #   between teams if people want to join one, or decide what food to purchase.
    needs_transportation = db.Column('needs_transportation', db.Boolean, nullable=False)
    rsvp_status = db.Column('rsvp_status', db.Boolean, nullable=False) # Accepted (True), Rejected (False)
    app_status = db.Column('app_status', db.Boolean, nullable=False) # Accepted (True), Rejected (False)
    shirt_size = db.Column('shirt_size', db.String(2), nullable=False) # S/M/L/XL

    # Education
    university = db.Column('university', db.String(64))
    class_year = db.Column('class_year', db.Integer)

    def __init__(self, first_name, last_name, email, needs_transportation, rsvp_status, app_status,
                 shirt_size, gender=None, team_id=None, university=None, class_year=None):
        
        # For every function parameter, initialize its respective column
        for arg, val in locals().items():
            setattr(arg, val)
        
        # Still need public ID and private ID, generate them from unique email
        url_id = uuid5(NAMESPACE_URL, email)
        self.private_id = str(url_id)
        
        CONVERT_128_TO_16_BITS = 112
        self.public_id = url_id.int >> CONVERT_128_TO_16_BITS