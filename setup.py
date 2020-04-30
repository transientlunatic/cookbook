# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read()

requirements = requirements.split("\n")

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='cookbook',
    use_scm_version=True,
    setup_requires=['setuptools_scm', 'click'],
    description="""A Python package for managing recipes.""",
    long_description=readme + '\n\n' + history,
    author="Daniel Williams",
    author_email='mail@daniel-williams.co.uk',
    url='https://github.com/transientlunatic/cookbook',
    packages=['cookbook'],
    package_dir={'cookbook': 'cookbook'},
    entry_points={
        'console_scripts': [
            'cookbook=cookbook.cli:cookbook'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=True,
    keywords='cookbook',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)
