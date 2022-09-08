"""Setuptools for sqlitefid"""

import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

version = {}
with open("src/sqlitefid/libs/Version.py") as fp:
    exec(fp.read(), version)

setup(
    name="sqlitefid",
    version=version.get("__version__"),
    description="Library and executable for converting format identification reports such as DROID and Siegfried to an sqlite database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/exponential-decay/sqlitefid",
    author="Ross Spencer",
    author_email="all.along.the.watchtower2001+github@gmail.com",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Other Audience",
        "Topic :: System :: Archiving",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="digital-preservation, file-analysis, format-identification",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.9, <4",
    entry_points={"console_scripts": ["sqlitefid=sqlitefid.sqlitefid:main"]},
    project_urls={
        "Part of demystify": "https://github.com/exponential-decay/demystify",
        "Bug Reports": "https://github.com/exponential-decay/sqlitefid/issues",
        "Source": "https://github.com/exponential-decay/sqlitefid",
        "Ko-Fi": "https://ko-fi.com/beet_keeper",
    },
)
