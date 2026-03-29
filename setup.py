from setuptools import setup


setup(
    name="pydiceroller",
    version="1.1.0",
    description="a minimal dice roller",
    long_description="The complete description/installation/use/FAQ is available at : https://github.com/thib1984/pydiceroller#readme",
    url="https://github.com/thib1984/pydiceroller",
    author="thib1984",
    author_email="thibault.garcon@gmail.com",
    license="MIT",
    license_files="LICENSE.txt",
    packages=["pydiceroller"],
    install_requires=[],
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "pydiceroller=pydiceroller.pydiceroller:pydiceroller"
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
