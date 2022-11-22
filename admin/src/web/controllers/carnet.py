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
)
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
from flask_uploads import UploadSet, IMAGES

from src.core.socios import buscar_socio
from src.web.exportaciones import carnet_PDF

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
def get_file(filename):
    return send_from_directory("public/uploads", filename)


@carnet_blueprint.route("/upload_image", methods=["GET", "POST"])
def upload_image():
    form = UploadForm()
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = url_for("carnet.get_file", filename=filename)
        print(file_url)
        file_url = file_url.replace("/carnet", "")
    else:
        file_url = None
    return render_template("/carnet/upload_image.html", form=form, file_url=file_url)


@carnet_blueprint.route("/<id>")
def view_license(id):
    kwargs = {"url": request.url, "socio": buscar_socio(id)}
    return render_template("carnet/carnet_template.html", **kwargs)


@carnet_blueprint.route("/<id>/carnet.png")
def view_license_only(id):
    kwargs = {"url": request.url, "socio": buscar_socio(id)}
    strIO = io.BytesIO()
    strIO.readlines(render_template("carnet/carnet_only.html", **kwargs))
    strIO.seek(0)
    return send_file(strIO, download_name="carnet.pdf", as_attachment=True)
    # return render_template("carnet/carnet_only.html", **kwargs)
