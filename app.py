from flask import Flask, render_template, url_for, redirect, request
from flask import session as login_session
import pyrebase
import math
 
app = Flask(__name__, template_folder='template', static_folder='assets')

app.config['SECRET_KEY'] = 'super-secret-key'

config = {
  "apiKey": "AIzaSyDY35t9GW869VOw-H2c4jmm2r6P-EHW4s8",
  "authDomain": "case-study-a3.firebaseapp.com",
  "databaseURL": "https://case-study-a3-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "case-study-a3",
  "storageBucket": "case-study-a3.appspot.com",
  "messagingSenderId": "283372940900",
  "appId": "1:283372940900:web:51b26eeed79e81f35cb971",
  "databaseURL": "https://case-study-a3-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db =firebase.database()


@app.route('/', methods=['GET', 'POST'])
def starterpage():
  if request.method == 'POST':
    if request.form["form_type"] == "study":
      form_data = {
        'fullName': request.form['fullName'],
        'email': request.form['email'],
        'phone': request.form['phone'],
        'dob': request.form['dob'],
        'gender': request.form['gender'],
        'otherGender': request.form['otherGender'],
        'spaceType': request.form['spaceType'],
        'numOccupants': request.form['numOccupants'],
        'preferredDates': request.form['preferredDates'],
        'workshopTopic': request.form['workshopTopic'],
        'preferredTimes': request.form['preferredTimes'],
        'skillsToGain': request.form['skillsToGain'],
        'discoveryMethod': request.form['discoveryMethod'],
        'additionalComments': request.form['additionalComments']
    }
      db.child("Workshops-Requests").update(form_data)
      return redirect(url_for("starterpage"))

    elif request.form["form_type"] == "rent":
      form_data = {
        'fullName': request.form['fullName'],
        'email': request.form['email'],
        'phone': request.form['phone'],
        'dob': request.form['dob'],
        'gender': request.form['gender'],
        'otherGender': request.form['otherGender'],
        'spaceType': request.form['spaceType'],
        'duration': request.form['duration'],
        'timeOfDay': request.form['timeOfDay'],
        'moveInDate': request.form['moveInDate'],
        'equipment': request.form['equipment'],
        'numOccupants': request.form['numOccupants'],
        'comments': request.form['comments']
      }
      db.child("Rent-Requests").update(form_data)
      return redirect(url_for("starterpage"))
    else:
      ppl = int(request.form["ppl"])
      hours = int(request.form["hours"])
      estimate = 0
      if ppl < 21:
        estimate = 5*ppl + ((hours+(3-hours%3)%3)/3)*150
      elif ppl > 20 and ppl < 51:
        estimate = 5*ppl + ((hours+(3-hours%3)%3)/3)*200
      elif ppl > 50 and ppl < 81:
        estimate = 5*ppl + ((hours+(3-hours%3)%3)/3)*300
      elif ppl > 80 and ppl < 121:
        estimate = 5*ppl + ((hours+(3-hours%3)%3)/3)*300

      return render_template("starterpage.html",estimate = estimate)
  else:
    return render_template("starterpage.html",estimate = 0)



@app.route('/rent', methods=['GET', 'POST'])
def rent():
  return render_template("rent.html")

@app.route('/study', methods=['GET', 'POST'])
def study():
  return render_template("study.html")

@app.route('/signup',methods=['POST','GET'])
def signup():
  return render_template("signup.html")

@app.route('/submit',methods=['POST'])
def submit():
  form_data = request.form.to_dict()
  if request.form["form_type"] == "study":
    db.child("Workshops-Requests").update(form_data)
    return render_template("submit.html", name = form_data["fullName"])

  elif request.form["form_type"] == "rent":
    db.child("Rent-Requests").update(form_data)
    return render_template("submit.html", name = form_data["fullName"])

@app.route('/servicedetails', methods=['GET', 'POST'])
def servicedetails():
  return render_template("servicedetails.html")




if __name__ == '__main__':
 
    app.run( debug=True)