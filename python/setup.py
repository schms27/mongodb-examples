from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md")) as f:
    long_description = f.read()

setup(
    name="fastapi_mongodb",
    use_scm_version=False,
    setup_requires=["setuptools_scm"],
    description="A simple REST-API Service to serve generic documents from MongoDB",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=" https://github.com/schms27/mongodb-examples",
    author_email="noreply@simon.schmid.ch",
    classifiers=[  # Optional
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    entry_points={"console_scripts": ["fastapi_mongodb = api.main:app"]},
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        "scikit-learn",
        "lightgbm",
        "pandas",
        "pyarrow",
    ],
)