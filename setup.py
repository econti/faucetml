import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="FaucetML",
    version="0.0.1",
    author="Edoardo Conti, Lionel Vital",
    author_email="edoardo.conti@gmail.com",
    description="Simple, high-speed batch data reader for ML applications.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/econti/FaucetML",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["pandas>0.20.0", "google-cloud-bigquery>=1.22.0", "retry>=0.9.2"],
)
