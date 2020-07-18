from . import db

class Customer(db.Model):

    __tablename__ = "Customer"
    identification = db.Column(db.String(14), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    address=db.Column(db.String(150),  nullable=False)
    phone=db.Column(db.String(30),  nullable=True)
    mail=db.Column(db.String(30), nullable=False)
    
    children = db.relationship("Socket")

    def __init__(self,identification, name, address,phone,mail):
        self.identification = identification
        self.name = name
        self.address = address
        self.phone = phone
        self.mail = mail