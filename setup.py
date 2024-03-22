from setuptools import find_packages, setup

setup(
    name='AI_lin',
    packages=find_packages(include=['aifunction.py']),
    version='0.1.0',
    description='Python library for AI',
    author='Me',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)