import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="mp3_polly_lambda",
    version="0.0.1",

    description="S3 event triggers creation of polly mp3 with object data",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="Isaac Hinch",

    package_dir={"": "mp3_polly_lambda"},
    packages=setuptools.find_packages(where="mp3_polly_lambda"),

    install_requires=[
        "aws-cdk.core",
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
