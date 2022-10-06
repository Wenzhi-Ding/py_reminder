import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py_reminder",
    version="0.1.2",
    author="Wenzhi Ding",
    author_email="wenzhi.ding@foxmail.com",
    description="A decorator for monitoring your task",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wenzhi-ding/py_reminder",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
