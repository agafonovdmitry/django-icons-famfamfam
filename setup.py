# -*- coding: utf-8 -*-
"""
Setup file for django-icons-famfamfam package.
"""

from setuptools import setup, find_packages


setup(
    name='django-icons-famfamfam',
    version='0.1',
    author='Dmitry Agafonov',
    author_email='Dmitry@Agafonov.pp.ru',
    packages=find_packages(),
    include_package_data=True,
    license='Various, see README.txt file',
    description='Django staticfiles with famfamfam silk and flag icon sets',
    long_description=open('README.txt').read(),
    install_requires=[
        "Django >= 1.3",  # first release with staticfiles app bundled
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
    ],
    zip_safe=False,
)
