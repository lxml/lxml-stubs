from distutils.core import setup

tests_require = [
    "pytest>=6.0.0",
    "pytest-mypy-plugins==1.4.0",
    "coverage[toml]==5.2",
]


setup(
    name="lxml-stubs",
    version="0.1",
    package_data={"lxml-stubs": ["*.pyi"]},
    packages=["lxml-stubs"],
    tests_require=tests_require,
    extras_require={"test": tests_require},
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
    ],
    zip_safe=False
)
