# -*- coding: utf-8 -*-
#
# Copyright (C) 2019-2021 CERN.
# Copyright (C) 2019-2021 Northwestern University.
# Copyright (C)      2021 TU Wien.
#
# Invenio App RDM is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Views related to records and deposits."""


from flask import Blueprint
from invenio_pidstore.errors import PIDDeletedError, PIDDoesNotExistError, \
    PIDUnregistered
from invenio_records_resources.services.errors import PermissionDeniedError

from ..searchapp import search_app_context
from .filters import can_list_files, get_scheme_label, has_previewable_files, \
    make_files_preview_compatible, order_entries, pid_url, \
    select_preview_file, to_previewer_files

#
# Registration
#
def create_blueprint(app):
    """Register blueprint routes on app."""
    routes = app.config.get("APP_ROUTES")

    blueprint = Blueprint(
        "{{cookiecutter.package_name}}_records",
        __name__,
        template_folder="../templates",
    )

    # TODO: register your record views here.

    # Register template filters
    blueprint.add_app_template_filter(can_list_files)
    blueprint.add_app_template_filter(make_files_preview_compatible)
    blueprint.add_app_template_filter(pid_url)
    blueprint.add_app_template_filter(select_preview_file)
    blueprint.add_app_template_filter(to_previewer_files)
    blueprint.add_app_template_filter(has_previewable_files)
    blueprint.add_app_template_filter(order_entries)
    blueprint.add_app_template_filter(get_scheme_label)

    # Register context processor
    blueprint.app_context_processor(search_app_context)

    return blueprint
