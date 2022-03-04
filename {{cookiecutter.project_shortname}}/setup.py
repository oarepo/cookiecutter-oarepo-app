# -*- coding: utf-8 -*-
# Copyright (c) 2022 """{{cookiecutter.author_name}}."""
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

"""{{cookiecutter.project_name}}."""

import os

from setuptools import find_packages, setup

readme = open('README.md').read()

invenio_version = '~=3.5.0a4'
invenio_search_version = '>=1.4.2,<1.5.0'
invenio_db_version = '>=1.0.11,<1.1.0'

tests_require = [
    'pytest-invenio~=1.4.2',
]

setup_requires = [
    'Babel>=2.8,<3',
]

extras_require = {
    # Invenio-Search
    'elasticsearch7': [
        f'invenio-search[elasticsearch7]{invenio_search_version}'
    ],
    # Invenio-DB
    'mysql': [
        f'invenio-db[mysql,versioning]{invenio_db_version}'
    ],
    'postgresql': [
        f'invenio-db[postgresql,versioning]{invenio_db_version}'
    ],
    'sqlite': [
        f'invenio-db[versioning]{invenio_db_version}'
    ],
    # Storage plugins
    's3': [
        'invenio-s3~=1.0.5'
    ],
    # Extras
    'docs': [
        'Sphinx==4.2.0',
    ],
    'tests': tests_require,
}

extras_require['all'] = []
for name, reqs in extras_require.items():
    if name[0] == ':' or name in ('elasticsearch7',
                                  'mysql', 'postgresql', 'sqlite'):
        continue
    extras_require['all'].extend(reqs)

install_requires = [
    'CairoSVG>=2.5.2,<3.0.0',
    f'invenio[base,auth,metadata,files]{invenio_version}',
    'invenio-logging[sentry-sdk]>=1.3.0,<1.4.0',
    {%- if cookiecutter.data_model %}
    '{{cookiecutter.data_model}}>=1.0.0.dev1'
    {%- endif %}
]

packages = find_packages()

# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('{{cookiecutter.package_name}}', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='{{cookiecutter.project_shortname}}',
    version=version,
    description=__doc__,
    long_description=readme,
    long_description_content_type='text/markdown',
    keywords='{{cookiecutter.project_shortname}} OARepo Invenio',
    license='MIT',
    author='{{cookiecutter.author_name}}',
    author_email='{{cookiecutter.author_email}}',
    url='https://github.com/{{cookiecutter.github_repo}}',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'invenio_base.blueprints': [
            '{{cookiecutter.package_name}}_records = ' \
                '{{cookiecutter.package_name}}.records_ui.views:create_blueprint',
            '{{cookiecutter.package_name}} = {{cookiecutter.package_name}}.theme.views:create_blueprint',
        ],
        'invenio_assets.webpack': [
            '{{cookiecutter.package_name}}_theme = {{cookiecutter.package_name}}.theme.webpack:theme',
        ],
        'invenio_config.module': [
            '{{cookiecutter.package_name}} = {{cookiecutter.package_name}}.config',
        ],
        'invenio_i18n.translations': [
            'messages = {{cookiecutter.package_name}}',
        ],
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Development Status :: 5 - Production/Stable',
    ],
)
