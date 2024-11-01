from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
dp=SQLAlchemy(app)

@app.route('/')
def hell_world():
    return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)