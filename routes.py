from flask import Blueprint, render_template, request, redirect, url_for
from .models import Patient, Doctor, Appointment, Record
from . import db

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template(
        "index.html",
        patients=Patient.query.count(),
        doctors=Doctor.query.count(),
        appointments=Appointment.query.count()
    )

# ---------------- PATIENTS ----------------

@main.route("/patients", methods=["GET", "POST"])
def patients():
    if request.method == "POST":
        p = Patient(
            name=request.form["name"],
            age=request.form["age"],
            disease=request.form["disease"]
        )
        db.session.add(p)
        db.session.commit()
        return redirect(url_for("main.patients"))

    return render_template("patients.html", data=Patient.query.all())

# ---------------- DOCTORS ----------------

@main.route("/doctors", methods=["GET", "POST"])
def doctors():
    if request.method == "POST":
        d = Doctor(
            name=request.form["name"],
            speciality=request.form["speciality"]
        )
        db.session.add(d)
        db.session.commit()
        return redirect(url_for("main.doctors"))

    return render_template("doctors.html", data=Doctor.query.all())

# ---------------- APPOINTMENTS ----------------

@main.route("/appointments", methods=["GET", "POST"])
def appointments():
    if request.method == "POST":
        a = Appointment(
            patient=request.form["patient"],
            doctor=request.form["doctor"],
            date=request.form["date"]
        )
        db.session.add(a)
        db.session.commit()
        return redirect(url_for("main.appointments"))

    return render_template("appointments.html", data=Appointment.query.all())

# ---------------- RECORDS ----------------

@main.route("/records", methods=["GET", "POST"])
def records():
    if request.method == "POST":
        r = Record(
            patient=request.form["patient"],
            diagnosis=request.form["diagnosis"],
            prescription=request.form["prescription"]
        )
        db.session.add(r)
        db.session.commit()
        return redirect(url_for("main.records"))

    return render_template("records.html", data=Record.query.all())