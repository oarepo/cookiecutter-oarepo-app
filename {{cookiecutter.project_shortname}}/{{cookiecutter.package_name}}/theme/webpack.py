# -*- coding: utf-8 -*-
#
# Copyright (C) 2019-2022 CERN.
# Copyright (C) 2019-2022 Northwestern University.
# Copyright (C)      2022 TU Wien.
# Copyright (c) 2022 {{cookiecutter.author_name}}
#
# Invenio App RDM is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""JS/CSS Webpack bundles for theme."""

from invenio_assets.webpack import WebpackThemeBundle

theme = WebpackThemeBundle(
    __name__,
    'assets',
    default='semantic-ui',
    themes={
        'semantic-ui': dict(
            entry={
                '{{cookiecutter.package_name}}-landing-page':
                    './js/{{cookiecutter.package_name}}/landing_page/index.js',
                '{{cookiecutter.package_name}}-deposit':
                    './js/{{cookiecutter.package_name}}/deposit/index.js',
                '{{cookiecutter.package_name}}-search':
                    './js/{{cookiecutter.package_name}}/search/index.js',
                '{{cookiecutter.package_name}}-user-dashboard':
                './js/{{cookiecutter.package_name}}/user_dashboard/index.js',
            },
            dependencies={
                '@babel/runtime': '^7.9.0',
                '@ckeditor/ckeditor5-build-classic': '^16.0.0',
                '@ckeditor/ckeditor5-react': '^2.1.0',
                'formik': '^2.1.0',
                "i18next": "^20.3.0",
                "i18next-browser-languagedetector": "^6.1.0",
                'luxon': '^1.23.0',
                'path': '^0.12.7',
                'prop-types': '^15.7.2',
                'react-copy-to-clipboard': '^5.0.0',
                'react-dnd': '^11.1.0',
                'react-dnd-html5-backend': '^11.1.0',
                'react-dropzone': "^11.0.0",
                "react-i18next": "^11.11.0",
                'react-invenio-deposit': '^0.18.0',
                'react-invenio-forms': '^0.10.0',
                'yup': '^0.32.0',
            },
            aliases={
                # Define Semantic-UI theme configuration needed by
                # Invenio-Theme in order to build Semantic UI (in theme.js
                # entry point). theme.config itself is provided by
                # cookiecutter-oarepo-app.
                '../../theme.config$': 'less/theme.config',
                'themes/oarepo': 'less/{{cookiecutter.package_name}}/theme',
                '@less/{{cookiecutter.package_name}}': 'less/{{cookiecutter.package_name}}',
                '@translations/{{cookiecutter.package_name}}': 'translations/{{cookiecutter.package_name}}',
                '@translations/invenio_app_rdm': 'translations/{{cookiecutter.package_name}}'
            }
        ),
    }
)
