from flask import Flask, render_template, request, redirect, url_for
from models import db, Todo

app = Flask(__name__)

db.create_all()

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "GET":
        todos_db = db.query(Todo).all()
        return render_template("index.html", todos_template=todos_db)
    else:
        todo = request.form.get("todo")
        new_todo = Todo(todo=todo, check=False)
        db.add(new_todo)
        db.commit()
        todos_db = db.query(Todo).all()
        return render_template("index.html", todos_template=todos_db)

@app.route("/check-todo", methods=["POST"])
def check():
    todo_form = request.form.get("todo")
    todo_db = db.query(Todo).filter_by(todo=todo_form).first()
    if todo_db.check == True:
        todo_db.check = False
    else:
        todo_db.check = True
    db.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()