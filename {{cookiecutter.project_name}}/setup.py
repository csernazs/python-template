#!/usr/bin/env python3

from setuptools import setup, find_packages


DESCRIPTION = open("README.md").read()

setup(
    name="{{ cookiecutter.project_name }}",
    version="{{ cookiecutter.version }}",
    url="https://www.github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}",
    packages=find_packages(),
    author="{{ cookiecutter.full_name }}",
    author_email="{{ cookiecutter.email }}",
    description="{{ cookiecutter.description }}",
    entry_points={"console_scripts": ["{{ cookiecutter.script_name }}={{ cookiecutter.package_name }}.cli:main"]},
    long_description=DESCRIPTION,
    long_description_content_type="text/markdown",
    python_requires=">=3.4",
    install_requires=["typing;python_version<'3.5'"],
    extras_require={
        "dev": [
            "pycodestyle",
            "pylint",
            "wheel",
            "rope",
            "pytest",
            "pytest-cov",
            "coverage",
            "ipdb",
            "sphinx",
            "sphinx_rtd_theme",
            "reno",
        ],
        "test": ["pytest", "pytest-cov", "coverage", "requests"],
    },
    tests_require=["pytest"],
    license="MIT",
    platforms="any",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Pytest",
    ],
)
