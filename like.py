import os                 # os is used to get environment variables IP & PORT
from flask import Flask   # Flask is the web app that we will customize
from flask import render_template
from flask import request, session
from flask import redirect, url_for 
from database import db
from models import Task as Task
from models import User as User
from models import Comment as Comment
from forms import RegisterForm, LoginForm, CommentForm
import bcrypt
 
app = Flask(__name__)     # create an app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///BooleanBoard_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SECRET_KEY'] = 'SE3155'

def update_like(comment_id, task_id):
            comment = db.session.query(Comment).filter_by(id=comment_id).one()
            comment.comment_like += 1
            db.session.add(comment)
            db.session.commit()
            return redirect(url_for('get_task', task_id=task_id))