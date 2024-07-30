from flask import Flask, render_template, url_for, redirect, request
from flask import session as login_session
import pyrebase


 
app = Flask(__name__, template_folder='template', static_folder='assets')

app.config['SECRET_KEY'] = 'super-secret-key'

config = {
  "apiKey": "AIzaSyDf8OnDIHYzz-ycd143ZkcVmD-K9ictuQw",
  "authDomain": "auth-lab-53325.firebaseapp.com",
  "projectId": "auth-lab-53325",
  "storageBucket": "auth-lab-53325.appspot.com",
  "messagingSenderId": "140295796023",
  "appId": "1:140295796023:web:11130be94a50c70ef516b2",
  "measurementId": "G-TM23J59KMQ",
  "databaseURL":"https://auth-lab-53325-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db =firebase.database()


@app.route('/', methods=['GET', 'POST'])
def starterpage():
  return render_template("starterpage.html")

@app.route('/rent', methods=['GET', 'POST'])
def rent():
  return render_template("rent.html")

@app.route('/study', methods=['GET', 'POST'])
def study():
  return render_template("study.html")

@app.route('/signup',methods=['POST','GET'])
def signup():
  return render_template("signup.html")

@app.route('/submit',methods=['POST','GET'])
def submit():
  form_data = request.form.to_dict()
  print(form_data)
  return render_template("submit.html")

@app.route('/servicedetails', methods=['GET', 'POST'])
def servicedetails():
  return render_template("servicedetails.html")




if __name__ == '__main__':
 
    app.run( debug=True)