from . import db
from werkzeug.security import generate_password_hash, check_password_hash  # Import password hashing functions

class UserProfile(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    username = db.Column(db.String(80), unique=True)
    password_hash = db.Column(db.String(128), nullable=False)  # New password field

    def __init__(self, first_name, last_name, username, password):
        """Set user details and hash the password."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        """Hash password before storing."""
        self.password_hash = generate_password_hash(password, method='pbkdf2:sha256', salt_length=16)

    def check_password(self, password):
        """Checks if the password matches stored hash."""
        return check_password_hash(self.password_hash, password)
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)