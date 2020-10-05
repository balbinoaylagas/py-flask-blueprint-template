from flask import Blueprint, render_template
from webapp.core.corefile import CoreClass

home_bp = Blueprint("home_bp", __name__, template_folder="templates")


@home_bp.route("/home")
@home_bp.route("/")
def homeMain():
    coreObject = CoreClass()
    message = coreObject.coreMethod()
    return render_template("home.html", message=message)
