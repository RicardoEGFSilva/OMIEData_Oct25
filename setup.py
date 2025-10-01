import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="OMIEData_Oct25",
    version="0.0.0.2",
    author="Ricardo Silva (Fork) | Alberto Cruz and Mirel Mora (Original)",
    author_email="ricardo.emanuel@inesctec.pt | a.cruz.garcia@gmail.com, mirel.mora@gmail.com",
    description="Package to download marginal prices from https://www.omie.es/.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RicardoEGFSilva/OMIEData_Oct25",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.10",
    keywords=["OMIE", "Electricity prices"],
    install_requires=["pandas>=2.0.1", "requests", "datetime", "babel"],
    extras_require={
        'test': ['pytest>=8.4.1']
    }
)
