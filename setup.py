from setuptools import find_packages, setup

setup(
    name="ywsam",
    version="0.1",
    install_requires=[],
    packages=find_packages(exclude="notebooks"),
    extras_require={
        "all": [],
        "dev": [],
    },
)