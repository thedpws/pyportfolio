from setuptools import setup, find_packages

setup(
    name="pyportfolio",
    version="0.1.0",
    author="AZ Vasquez",
    author_email="azvasquez99@gmail.com",
    description="A library for declaring portfolios and making projections programmatically.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/thedpws/pyportfolio",
    packages=find_packages(),  # Automatically find packages in the project
    install_requires=[
        "pandas>=1.0.0",
        "matplotlib>=3.0.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)