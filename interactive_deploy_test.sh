#!/bin/bash

echo '# 1. Install setuptools'
uv sync
uv pip install setuptools==74.0.0

echo '# 2. Rename pyproject.toml'
mv pyproject.toml pyproject.toml_bak

echo '# 3. Remove build result folder'
rm -rf ./build ./dist ./django_drf_keycloak_auth.egg-info

echo '# 4. Build package via setup.py'
python setup.py sdist bdist_wheel 

echo '# 5. Deploy to TestPyPI'
twine upload --repository testpypi dist/*

echo '# 6. Restore pyproject.toml'
mv pyproject.toml_bak pyproject.toml

echo '# 7. Done ...'
