<!--
 Copyright (c) 2022 CESNET

 This software is released under the MIT License.
 https://opensource.org/licenses/MIT
-->

# Cookiecutter-OARepo-App

This [Cookiecutter](https://github.com/audreyr/cookiecutter) template is designed to help you to generate an OARepo application module
based on [Invenio-App-RDM](https://github.com/inveniosoftware/invenio-app-rdm).
Application module is responsible for handling one or more record models, Invenio application configuration, UI theme, translations.

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet::

    pip install -U cookiecutter

Generate your OARepo instance:

    cookiecutter https://github.com/oarepo/cookiecutter-oarepo-app.git

More detailed steps can be found in the <https://inveniosoftware.org/#getstarted>

## Features

- **Python package:** Python package for your application module.
- **Boilerplate files:** `README` including important badges.
- **License:** [MIT](https://opensource.org/licenses/MIT) file and headers.
- **TODO**

## Configuration

To generate correct files, please provide the following input to Cookiecutter:

- `project_name` Full project name, might contain spaces.
- `project_shortname` Project shortname, no spaces allowed, use `-` as a separator.
- `project_site` Project website host.
- `package_name` Package/Module name for Python, must follow `PEP 0008 <https://www.python.org/dev/peps/pep-0008/>`\_.
- `github_repo` GitHub repository of the project in form of `USER/REPO`,
- `record_model` Name of record model package this app module should be handling.
- not the full GitHub URL.
- `**TODO**` `**TODO**`
