
from pip._internal.req import parse_requirements
from operator import attrgetter
from os import path
from setuptools import setup, find_packages

def read(fname):
    return open(path.join(path.dirname(__file__), fname)).read()

def from_here(relative_path):
    return path.join(path.dirname(__file__), relative_path)

with open('requirements.txt') as f: 
    requirements = f.readlines() 

# test.pypi

#- rm -rf build dist shipu.egg-info
#- python setup.py sdist bdist_wheel 
#- python3 -m twine upload --repository testpypi dist/*

# pip install --index-url https://test.pypi.org/simple/ --upgrade --no-cache-dir --extra-index-url=https://pypi.org/simple/ shipapp

# pypi

# env\Scripts\activate && python setup.py sdist bdist_wheel && python -m twine upload --skip-existing dist/*

#- rm -rf build dist shipu.egg-info
#- python setup.py sdist bdist_wheel 
# python -m twine upload --skip-existing dist/*
# python -m twine upload dist/*

setup(
    name="shipapp",
    version="0.0.1.7",
    author="Yusuf Ahmed",
    author_email="yusufahmed172@gmail.com",
    packages=['ship'],
    description="The best way to move files between your devices",
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    url="https://github.com/yusuf8ahmed/Ship",
    install_requires=['qrcode==6.1', 'pillow'],
    package_data={
        'ship': ['*.ico', "*.js"],
    },
    entry_points ={ 
        'console_scripts': [ 
            'ship = ship.__main__:main'
        ] 
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords ='ship shipu file transfer shiplite',
    python_requires='>=3',
    zip_safe = False
)