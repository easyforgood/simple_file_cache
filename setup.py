import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simple_file_cache", # Replace with your own username
    version="0.0.6",
    author="Sip",
    author_email="siplexy.pi@outlook.com",
    description="Simple File Cache based on pickle or json",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/easyforgood/simple_file_cache",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)
