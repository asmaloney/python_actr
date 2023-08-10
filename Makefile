
# run tests
test:
	python3 -m unittest

## pip packaging

# Install tools required to package for pip.
install-build-tools:
	python3 -m pip install --upgrade build setuptools twine wheel

# Build packages for pip.
build:
	python3 -m build

# Upload the test pip package.
# You must have an account and an API token for this to work.
upload-test:
	python3 -m twine upload --repository testpypi dist/*

# Upload the release pip package.
# You must have an account and an API token for this to work.
upload-release:
	python3 -m twine upload dist/*
