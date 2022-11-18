from flask import Blueprint, render_template, request, flash, url_for, session, redirect

from src.core.socios import buscar_socio
from src.web.exportaciones import carnet_PDF

carnet_blueprint = Blueprint("carnet", __name__, url_prefix="/carnet")


@carnet_blueprint.route("/<id>")
def view_license(id):
    kwargs = {"url": request.url, "socio": buscar_socio(id)}
    return render_template("carnet/carnet_template.html", **kwargs)


@carnet_blueprint.route("/<id>/carnet.png")
def view_license_only(id):
    kwargs = {"url": request.url, "socio": buscar_socio(id)}
    return render_template("carnet/carnet_only.html", **kwargs)
