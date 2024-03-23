from flask import Blueprint, render_template

views = Blueprint(
    "views", __name__, static_folder="static", template_folder="templates"
)


@views.route("/")
def index():
    return render_template("index.html")


@views.route("/about")
def about():
    return render_template("about.html")


@views.route("/methodology")
def methodology():
    return render_template("methodology.html")
