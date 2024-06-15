from setuptools import setup, find_packages

setup(
    name='tibber_local_lib',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'smllib'
    ],
    author='Leo Tiedt | Sonnenladen GmbH',
    author_email='l.tiedt@sonnenladen.de',
    description='A library to fetch and decode SML data locally from Tibber Pulse',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/SonnenladenGmbH/tibber_local_lib',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)