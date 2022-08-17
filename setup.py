import re
import setuptools

with open("BitlyAPI/__init__.py", encoding="utf-8") as f:
    version = re.findall(r"__version__ = \"(.+)\"", f.read())[0]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bitly-api-python",
    version=version,
    author="Krishna-Singhal",
    author_email="ylikehits3@gmail.com",
    description="Wrapper for [Bitly API](https://api.ksprojects.me/bitly)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Krishna-Singhal/bitly-api-python",
    project_urls={
        "Bug Tracker": "https://github.com/Krishna-Singhal/bitly-api-python/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests"],
    packages=['BitlyAPI'],
    python_requires=">=3.6",
)