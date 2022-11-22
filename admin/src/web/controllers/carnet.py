import io

from flask import (
    Blueprint,
    render_template,
    request,
    send_file,
    flash,
    url_for,
    session,
    redirect,
    send_from_directory,
    url_for,
    Response,
)

from flask_weasyprint import HTML, render_pdf
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
from flask_uploads import UploadSet, IMAGES
from pathlib import Path, PurePosixPath

from src.core.socios import buscar_socio, save_photo, get_photo_socio
from src.web.exportaciones import carnet_PDF
from src.web.helpers.permission import has_permission
from src.decoradores.login import login_requerido


carnet_blueprint = Blueprint("carnet", __name__, url_prefix="/carnet")
photos = UploadSet("photos", IMAGES)


class UploadForm(FlaskForm):
    photo = FileField(
        validators=[
            FileAllowed(photos, "Solo se permite subir imagenes"),
            FileRequired("El campo archivo no debería estar vacio"),
        ]
    )
    submit = SubmitField("upload")


@carnet_blueprint.route("public/uploads/<filename>")
@login_requerido
def get_file(filename):
    if not (has_permission(session["user"], "carnet_photo")):
        return abort(403)
    return send_from_directory("public/uploads", filename)


@carnet_blueprint.route("/upload_image/<id>", methods=["GET", "POST"])
@login_requerido
def upload_image(id):
    if not (has_permission(session["user"], "carnet_upload")):
        return abort(403)
    socio = buscar_socio(id)
    form = UploadForm()
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = url_for("carnet.get_file", filename=filename)
        file_url = file_url.replace("/carnet", "")
        save_photo(id, file_url)
    else:
        file_url = None
    return render_template(
        "/carnet/upload_image.html", form=form, file_url=file_url, socio=socio
    )


@carnet_blueprint.route("/<id>")
@login_requerido
def view_license(id):
    if not (has_permission(session["user"], "carnet_license")):
        return abort(403)
    kwargs = {
        "url": request.url,
        "socio": buscar_socio(id),
        "photo": get_photo_socio(id),
    }
    print(image_exists(kwargs["photo"]))
    if not image_exists(kwargs["photo"]):
        kwargs["photo"] = get_default_photo_path()
    return render_template("carnet/carnet_template.html", **kwargs)


@carnet_blueprint.route("/<id>/carnet.png")
def view_license_only(id):
    if not (has_permission(session["user"], "carnet_license")):
        return abort(403)
    kwargs = {
        "url": request.url,
        "socio": buscar_socio(id),
        "photo": get_photo_socio(id),
    }
    print(image_exists(kwargs["photo"]))
    if not image_exists(kwargs["photo"]):
        kwargs["photo"] = get_default_photo_path()
    return render_template("carnet/carnet_only.html", **kwargs)


def image_exists(path):
    path = str(Path(__file__).parent.parent.parent.parent) + path
    return Path(path).exists()


def get_default_photo_path():
    return "/public/uploads/default_photo.jpg"


@carnet_blueprint.route("/download/<id>")
@login_requerido
def carnet_pdf_download(id):
    if not (has_permission(session["user"], "carnet_download")):
        return abort(403)
    return render_pdf(url_for("carnet.view_license_only", id=id))
