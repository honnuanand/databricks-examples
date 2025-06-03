from setuptools import setup, find_packages
import os

# Read the contents of README.md
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='mylib',
    version='0.1',
    packages=find_packages(),
    description='A simple custom library for Databricks testing',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Anand Rao',
    author_email='anand@example.com',
    url='https://github.com/yourusername/databricks-examples',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.8',
    install_requires=[],
    extras_require={
        'dev': [
            'pytest>=7.0',
            'black>=22.0',
            'flake8>=4.0',
        ],
    },
)
