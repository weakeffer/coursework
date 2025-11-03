from mongoengine import Document, fields
from django.contrib.auth.hashers import make_password, check_password
from datetime import datetime

class Users(Document):
    email = fields.StringField(max_length=50, required = True, unique = True)
    name = fields.StringField(max_length=15, required = True, unique = True)
    password = fields.StringField(max_length=255, required = True, unique = False)
    is_active = fields.BooleanField(default=True)
    is_staff = fields.BooleanField(default=False)
    date_joined = fields.DateTimeField(default=datetime.now)
    
    meta = {
        'collection': 'users',
        'ordering': 'id'
    }

    def set_password(self,raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
    @property
    def is_anonymous(self):
        return False
    
    def get_username(self):
        return self.email
    
    def __str__(self):
        return self.email