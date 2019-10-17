from flask import Flask,render_template,url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm,RegistrationForm
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

# ******************home route


@app.route('/')
@app.route('/home')
def home():
 return render_template('home.html',posts=posts)

@app.route('/about')
def about():
 return render_template('about.html',title='About',posts=posts)


# ****************this is register router

@app.route('/register',methods=['GET','POST'])
def register():
 form= RegistrationForm()
 if form.validate_on_submit():
	 flash("Account created for {form.username.data}!","success")
	 return redirect(url_for('home'))
 return render_template('register.html',title='register',form=form)



# login router

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


