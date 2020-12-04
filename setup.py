from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

required = ['matplotlib',
            'numpy',
            'pandas',
            'notebook',
            'jupyter',
            'appnope<=0.1.0',
            'tqdm'
            ]

__version__ = 'init'
exec(open('calandarevent/version.py').read())

setup(
    name='calandarevent',
    packages=find_packages(),
    version=__version__,
    description="A short description of the project.",
    author='YannH',
    long_description=long_description,
    long_description_content_type="text/markdown",
    setup_requires=['pytest-runner', 'wheel', 'flake8'],
    tests_require=['pytest', 'pytest-cov', 'treon'],
    install_requires=required,
    license='MIT\
    ',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
