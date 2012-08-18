# -*- coding: utf-8 -*-

"""
Setup file for django-icons-famfamfam package.
"""

from setuptools import setup, find_packages


setup(
    name='django-icons-famfamfam',
    version='0.2-1',
    author='Dmitry Agafonov',
    author_email='Dmitry@Agafonov.pp.ru',
    url='https://github.com/agafonovdmitry/django-icons-famfamfam',
    packages=find_packages(exclude=['example_project']),
    include_package_data=True,
    license='Various, see README file',
    description='Django staticfiles with famfamfam silk and flag icon sets',
    long_description=open('README.rst').read(),
    install_requires=[
        "Django >= 1.3",  # first release with staticfiles app bundled
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
    ],
    zip_safe=False,
)
