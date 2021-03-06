import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-simple-admin-overlay',
    version='0.2',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='Lightweight Django app which displays simple overlay with admin links on the frontend pages.',
    long_description=README,
    url='https://github.com/bonidjukic/django-simple-admin-overlay',
    author='Boni Đukić',
    author_email='boni@djukic.com.hr',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Topic :: Utilities',
    ],
)