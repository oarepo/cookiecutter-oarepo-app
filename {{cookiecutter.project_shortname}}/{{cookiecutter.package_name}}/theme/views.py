# Copyright (c) 2022 {{cookiecutter.author_name}}
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT


"""Routes for general pages provided by {{cookiecutter.project_shortname}}."""

from flask import Blueprint, current_app, render_template
from flask_babelex import get_locale
from flask_babelex import lazy_gettext as _
from flask_menu import current_menu


#
# Registration
#
def create_blueprint(app):
    """Blueprint for the routes and resources provided by {{cookiecutter.project_shortname}}."""
    routes = app.config.get("APP_ROUTES")

    blueprint = Blueprint(
        "{{cookiecutter.package_name}}",
        __name__,
        template_folder="templates",
        static_folder="static",
    )

    blueprint.add_url_rule(routes["index"], view_func=index)
    blueprint.add_url_rule(routes["help_search"], view_func=help_search)

    @blueprint.before_app_first_request
    def init_menu():
        """Initialize menu before first request."""
        current_menu.submenu('actions.deposit').register(
            '{{cookiecutter.package_name}}_records.dashboard',
            _('My dashboard'),
            order=1
        )

        current_menu.submenu('plus.deposit').register(
            '{{cookiecutter.package_name}}_records.deposit_create',
            _('New upload'),
            order=1,
        )

    return blueprint


#
# Views
#
def index():
    """Frontpage."""
    return render_template(
        current_app.config['THEME_FRONTPAGE_TEMPLATE'],
    )


def help_search():
    """Search help guide."""
    # Default to rendering english page if locale page not found.
    locale = get_locale()
    return render_template([
        f"{{cookiecutter.project_shortname}}/help/search.{locale}.html",
        "{{cookiecutter.project_shortname}}/help/search.en.html",
    ])
