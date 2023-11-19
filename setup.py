import os
from setuptools import setup


def get_packages(package):
    return [
        dirpath
        for dirpath, dirnames, filenames in os.walk(package)
        if os.path.exists(os.path.join(dirpath, "__init__.py"))
    ]


def get_package_data(package):
    walk = [
        (dirpath.replace(package + os.sep, "", 1), filenames)
        for dirpath, dirnames, filenames in os.walk(package)
        if not os.path.exists(os.path.join(dirpath, "__init__.py"))
    ]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename) for filename in filenames])
    return {package: filepaths}


setup(
    name='django-admin-anylogicfilter',
    version='0.1.1',
    install_requires=[],
    author='Maxim Medentsev',
    author_email='m.v.medencev@gmail.com',
    maintainer='Ivan Golyshev',
    maintainer_email='golyshev.nomer@gmail.com',
    description='Django app that adds admin filter with any functionality you need.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mdncv/django-admin-anylogicfilter',
    packages=get_packages("anylogicfilter"),
    package_data=get_package_data("anylogicfilter"),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
