# Example Setuptools A+B Package
[![Demo workflow](https://github.com/dmpyatin/setuptools_test/actions/workflows/demo_workflow.yml/badge.svg)](https://github.com/dmpyatin/setuptools_test/actions/workflows/demo_workflow.yml)

This is a simple example package for publishing on PyPl with setuptools. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/) to write your content.

Links:
https://test.pypi.org/project/setuptools-test-dmpyatin/
https://packaging.python.org/tutorials/packaging-projects/

Windows:
 * Build package: `py -m build`
 * Upload package: `py -m twine upload -r tespypi dist/*`
 * Install: `pip install --index-url https://test.pypi.org/simple/ --no-deps setuptools_test_dmpyatin`

Usage:
```python
import setuptools_test_dmpyatin as std 
print(std.add(1,2))
```