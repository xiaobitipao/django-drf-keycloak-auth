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

echo '# 5. Deploy to PyPI'
twine upload --repository pypi dist/*

echo '# 6. Restore pyproject.toml'
mv pyproject.toml_bak pyproject.toml

echo '# 7. Done ...'

# echo '# 1. Generate LONG_DESCRIPTION'
# uv run python build_long_description.py

# echo '# 2. Remove build result folder'
# rm -rf ./dist ./django_drf_keycloak_auth.egg-info

# echo '# 3. Build package via pyproject.toml'
# uv run python -m build

# echo '# 4. Deploy to PyPI'
# twine upload --repository pypi dist/*

# echo '# 5. Done ...'
