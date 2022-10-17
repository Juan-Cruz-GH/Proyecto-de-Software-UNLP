from flask import render_template


def not_found_error(e):
    kwargs = {
        "error_name": "404 Not found Error",
        "error_description": "La Url a la que intenta acceder no existe",
    }

    return render_template("error.html", **kwargs), 404
