from setuptools import setup
from saltant.version import NAME, DESCRIPTION, VERSION


# Parse readme to include in PyPI page
with open('README.md') as f:
    long_description = f.read()


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mwiens91/saltant-py',
    author='Matt Wiens',
    author_email='mwiens91@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
    ],
    packages=['saltant'],
    python_requires='==2.7, >=3.4',
    install_requires=[
        'requests',
    ],
)
