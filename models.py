from . import db

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    disease = db.Column(db.String(200))


class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    speciality = db.Column(db.String(100))


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient = db.Column(db.String(100))
    doctor = db.Column(db.String(100))
    date = db.Column(db.String(50))


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient = db.Column(db.String(100))
    diagnosis = db.Column(db.String(200))
    prescription = db.Column(db.String(200))
