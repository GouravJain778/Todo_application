
from flask import Flask, render_template, request, redirect, url_for ,flash
from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager, UserMixin, login_user, logout_user



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.sqlite3'
db=SQLAlchemy(app)
# login_manager = LoginManager()
# login_manager.init_app(app)



# class user(db.Model,UserMixin):
#     ID=db.Column('id',db.integer,primary_key=True)
#     first_name=db.Column(db.String(200))
#     last_name=db.Column(db.String(200))
#     email=db.Column(db.String(200),uniqe=True)
#     password=db.Column(db.String(200))



# with app.app_context():
#     try:
#         db.create_all()
#         print("Database tables created successfully!")
#     except Exception as e:
#         print(f"Error occurred: {e}")


class todo(db.Model):
    id = db.Column('id',db.Integer, primary_key=True)
    text = db.Column(db.String(200)) 
    complete = db.Column(db.Boolean)




with app.app_context():
    try:
        db.create_all()
        print("Database tables created successfully!")
    except Exception as e:
        print(f"Error occurred: {e}")


@app.route('/')
def index():
    complete=todo.query.filter_by(complete=True).all()
    incomplete=todo.query.filter_by(complete=False).all()
    print(incomplete,"kkkkkkkkkkk")
    return render_template('index.html',incomplete=incomplete, complete=complete)




@app.route('/add', methods=['POST'])
def add(): 
    todo_item = todo(text=request.form['todoitem'], complete=False) 
    db.session.add(todo_item) 
    db.session.commit() 

  
    return redirect(url_for('index')) 
  
  
@app.route('/complete/<id>') 
def complete(id):
    todo_item = todo.query.filter_by(id=int(id)).first() 
    todo_item.complete = True
    db.session.commit()
    return redirect(url_for('index'))




# class User(db.Model,UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(250), unique=True,
#                          nullable=False)
#     password = db.Column(db.String(250),
#                          nullable=False)
   



# with app.app_context():
#     try:
#         db.create_all()
#         print("Database tables created successfully!")
#     except Exception as e:
#         print(f"Error occurred: {e}")


# @app.route('/login',methods=['POST','GET'])
# def login():
#     if request.method=="POST" and 'username' in request.form and 'password' in request.form:
#         username=request.form['username']
#         password=request.form['password']
#         if username and password in User:
#             login_user(username)
#             return redirect(url_for("home"))
#         else:
#             return flash("not correct your crendial")

#     else:
#         return render_template("login.html")
    

# @app.route('/register', methods=["GET", "POST"])
# def register():
#     if request.method == "POST":
#         user = User(username=request.form.get("username"),
#                      password=request.form.get("password"))
#         db.session.add(user)
#         db.session.commit()
#         return redirect(url_for("login"))
#     return render_template("sign_up.html")





    



       




app.run(debug=True)
