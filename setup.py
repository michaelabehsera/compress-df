import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="compress-df",
    version="0.0.1",
    author="Michael Abehsera",
    author_email="michaelabehsera@gmail.com",
    description="Compress DataFrame, is a script that will automatically optimize your DataFrame in order to reduce its size in some cases by up to 70%. Note: It only works on numerical variables not Object based ones. Support for more types of variables and other optimization functions coming soon",
    long_description='Compress DataFrame will automatically pick the correct dtypes based on each column and find the one that takes up the least memory',
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
