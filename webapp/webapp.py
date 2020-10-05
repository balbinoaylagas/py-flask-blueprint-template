from flask import Blueprint, render_template

webapp_bp = Blueprint("webapp_bp", __name__, template_folder="templates")
