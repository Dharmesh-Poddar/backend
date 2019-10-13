from flask import Flask,render_template,url_for
from forms import RegistrationForm,LoginForm
app = Flask(__name__)
app.config['SECRET_KEY']='sdfasf33ddfdsf34343'
posts= [

         {
	       'author':'Dharmesh ji',
	       'title':'bakchodi ki had',
	       'content': 'Badshah ki gali mein aake uska pata nahi poochte ghulamo ke jhuke hue sarr khud ba khud raasta bata dete hai',
           'date_posted':'20october'

         },
         {
	
	       'author':'abhishek',
	       'title':'cricket',
	       'content': 'Badshah ki gali mein aake uska pata nahi poochte ghulamo ke jhuke hue sarr khud ba khud raasta bata dete hai',
           'date_posted':'10novemeber'
         }


]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html',title='About',posts=posts)

@app.route('/register')
def register():
    return render_template('register.html',title='Register',form=form)

@app.route('/login')
def login():
    return render_template('login.html',title='login',form=form)