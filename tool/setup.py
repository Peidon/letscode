from setuptools import setup, find_packages

__version__ = '1.0'
requirements = open('requirements.txt').readlines()

setup(
    name='moo',
    version=__version__,
    author='Pd',
    author_email='',
    url='',
    description='model tool',
    packages=find_packages(exclude=["tests"]),
    python_requires='>=3.5.0',
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'moo=moo.model_tool:main',
        ],
    }
)
