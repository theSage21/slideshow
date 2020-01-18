from setuptools import setup

__version__ = "2020.1.18"

with open("README.md", "r") as fl:
    long_desc = fl.read()


setup(
    name="slideshow",
    author="Arjoonn Sharma",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    version=__version__,
    packages=["slideshow"],
    python_requires=">=3.6",
    project_urls={"Source": "https://github.com/thesage21/slideshow"},
    zip_safe=True,
)
