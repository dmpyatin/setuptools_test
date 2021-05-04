import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="setuptools_test_dmpyatin",
    version="0.0.4",
    author="Dmitry Pyatin",
    author_email="dmpyatin@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dmpyatin/setuptools_test",
    project_urls={
        "Bug Tracker": "https://github.com/dmpyatin/setuptools_test/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    py_modules=["setuptools_test_dmpyatin"],
    python_requires=">=3.5"
)
