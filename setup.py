import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="deployment",
    version="1.0.0",
    author="Komron Miralizoda",
    author_email="miralizoda.komron@gmail.com",
    description="Simple tool for autodeploying github projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/komron-m/simple-auto-deployment",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
