from flask import Flask, render_template_string, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "supersecretkey"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"

# =========================
# DATABASE MODELS
# =========================

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    tasks = db.relationship("Task", backref="owner", lazy=True)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(300))
    status = db.Column(db.String(50), default="pending")

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    completed_at = db.Column(db.DateTime, nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# =========================
# AUTH ROUTES
# =========================

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = generate_password_hash(request.form["password"])

        if User.query.filter_by(username=username).first():
            return "Username already exists"

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))

    return render_template_string(SIGNUP_HTML)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(username=request.form["username"]).first()
        if user and check_password_hash(user.password, request.form["password"]):
            login_user(user)
            return redirect(url_for("dashboard"))
        return "Invalid credentials"

    return render_template_string(LOGIN_HTML)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

# =========================
# DASHBOARD
# =========================

@app.route("/")
@login_required
def dashboard():
    tasks = Task.query.filter_by(user_id=current_user.id).order_by(Task.created_at.desc()).all()
    return render_template_string(DASHBOARD_HTML, tasks=tasks)

@app.route("/add", methods=["POST"])
@login_required
def add_task():
    new_task = Task(
        title=request.form["title"],
        description=request.form["description"],
        user_id=current_user.id
    )
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for("dashboard"))

@app.route("/complete/<int:id>")
@login_required
def complete(id):
    task = Task.query.get(id)
    if task and task.user_id == current_user.id:
        task.status = "completed"
        task.completed_at = datetime.utcnow()
        db.session.commit()
    return redirect(url_for("dashboard"))

@app.route("/delete/<int:id>")
@login_required
def delete(id):
    task = Task.query.get(id)
    if task and task.user_id == current_user.id:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for("dashboard"))

# =========================
# BEAUTIFUL UI
# =========================

LOGIN_HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Login</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
<style>
body {
    background: linear-gradient(135deg, #667eea, #764ba2);
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}
.card { border-radius: 20px; }
</style>
</head>
<body>
<div class="card shadow-lg p-5" style="width: 350px;">
    <h3 class="mb-4 text-center">Welcome Back 👋</h3>
    <form method="POST">
        <input class="form-control mb-3" name="username" placeholder="Username" required>
        <input class="form-control mb-3" name="password" type="password" placeholder="Password" required>
        <button class="btn btn-dark w-100">Login</button>
    </form>
    <div class="text-center mt-3">
        <a href="/signup">Create account</a>
    </div>
</div>
</body>
</html>
"""

SIGNUP_HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Sign Up</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
<style>
body {
    background: linear-gradient(135deg, #43cea2, #185a9d);
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}
.card { border-radius: 20px; }
</style>
</head>
<body>
<div class="card shadow-lg p-5" style="width: 350px;">
    <h3 class="mb-4 text-center">Create Account 🚀</h3>
    <form method="POST">
        <input class="form-control mb-3" name="username" placeholder="Username" required>
        <input class="form-control mb-3" name="password" type="password" placeholder="Password" required>
        <button class="btn btn-success w-100">Sign Up</button>
    </form>
    <div class="text-center mt-3">
        <a href="/login">Already have an account?</a>
    </div>
</div>
</body>
</html>
"""

DASHBOARD_HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Dashboard</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
<style>
body { background-color: #f5f6fa; }
.sidebar {
    height: 100vh;
    background: #111827;
    color: white;
    padding: 20px;
}
.content { padding: 40px; }
.card { border-radius: 15px; }
</style>
</head>
<body>
<div class="container-fluid">
<div class="row">

<div class="col-md-2 sidebar">
    <h4>📝 TaskFlow</h4>
    <hr>
    <p>👤 {{ current_user.username }}</p>
    <a href="/logout" class="btn btn-outline-light btn-sm mt-3">Logout</a>
</div>

<div class="col-md-10 content">
    <h2 class="mb-4">Your Tasks</h2>

    <form method="POST" action="/add" class="row g-2 mb-4">
        <div class="col-md-4">
            <input class="form-control" name="title" placeholder="Task title" required>
        </div>
        <div class="col-md-4">
            <input class="form-control" name="description" placeholder="Description">
        </div>
        <div class="col-md-2">
            <button class="btn btn-dark w-100">Add</button>
        </div>
    </form>

    <div class="row">
        {% for task in tasks %}
        <div class="col-md-4 mb-3">
            <div class="card shadow-sm p-3">
                <h5>{{ task.title }}</h5>
                <p class="text-muted">{{ task.description }}</p>

                <small class="text-muted">
                Created: {{ task.created_at.strftime('%Y-%m-%d %H:%M') }}
                </small><br>

                {% if task.completed_at %}
                <small class="text-success">
                Completed: {{ task.completed_at.strftime('%Y-%m-%d %H:%M') }}
                </small><br>
                {% endif %}

                {% if task.status == "completed" %}
                <span class="badge bg-success mt-2">Completed</span>
                {% else %}
                <a href="/complete/{{ task.id }}" class="btn btn-sm btn-outline-success mt-2">Mark Complete</a>
                {% endif %}

                <a href="/delete/{{ task.id }}" class="btn btn-sm btn-outline-danger mt-2">Delete</a>
            </div>
        </div>
        {% endfor %}
    </div>

</div>
</div>
</div>
</body>
</html>
"""

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)