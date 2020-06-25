from flask import Flask , redirect , render_template, request,flash,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager , UserMixin  ,login_user, logout_user
#from werkzeug.security import check_password_hash
#from werkzeug.debug import DebuggedApplication




app=Flask(__name__)



   
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost:3308/db'
app.config['SECRET_KEY']='619619'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
    
db = SQLAlchemy(app)



login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(200))
    email = db.Column(db.String(200))
    password = db.Column(db.String(200))
    admin = db.Column(db.Integer)



@login_manager.user_loader
def get(id):
    return User.query.get(id)


@app.route("/delete_article/<int:id>/delete", methods=['POST'])
def delete_post(id):
    user = User.query.get(id)
    db.delete(user)
    db.commit()
    flash('User  deleted!', 'success')
    return  redirect(url_for('admin'))





@app.route("/admin", methods=['GET'])
def employee():

 
 data = User.query.all()
 return render_template("admin.html", admins=data)





@app.route('/',methods=['GET'])
def get_login():
    return render_template('login.html')



@app.route('/home',methods=['GET'])
#@login_required
def get_home():
    return render_template('home.html')


@app.route('/signup',methods=['GET'])
def get_signup():
    return render_template('signup.html')

@app.route('/login',methods=['POST'])
def login_post():
    email = request.form['email']
    password = request.form['password']

    user = User.query.filter_by(email=email).first()
    if user:
        if user.password == password:
            login_user(user)
            if user.admin==1:
                return redirect('/admin')
            return redirect('/home')
        else:
           return render_template('/login.html')
    else : 
        return render_template('/login.html')

@app.route('/signup',methods=['POST'])
def signup_post():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    admin = request.form['admin']
    user = User(username=username,email=email,password=password,admin=admin)
    db.session.add(user)
    db.session.commit()
    user = User.query.filter_by(email=email).first()
    login_user(user)
    return redirect('/admin')

@app.route('/logout',methods=['GET'])
def logout():
    logout_user()
    return redirect('/')





if __name__=='__main__':
    app.run(debug=True,use_reloader=True)