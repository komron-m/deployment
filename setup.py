import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="deployment",
    version="1.0.4",
    author="Komron Miralizoda",
    author_email="miralizoda.komron@gmail.com",
    description="Simple tool for auto-deployment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/komron-m/deployment",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
