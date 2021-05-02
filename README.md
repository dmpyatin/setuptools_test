# Example Package

This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/) to write your content.

Windows:
    Build package: `py -m build`
    Upload package: `py -m twine upload -r tespypi dist/*`

Usage: 
    Install: `pip install --index-url https://test.pypi.org/simple/ --no-deps setuptools_test_dmpyatin`

```python
import setuptools_test_dmpyatin as std 
print(std.add(1,2))
```


