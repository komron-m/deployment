import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="githubdeployment",
    version="1.0.2",
    author="Komron Miralizoda",
    author_email="miralizoda.komron@gmail.com",
    description="Simple tool for autodeploying github projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/komron-m/github-deployment",
    packages=setuptools.find_packages(),
    install_requires=[
            'gitpython==3.0.3',
            'requests==2.22.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
