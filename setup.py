import os
from setuptools import setup

# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "1and1",
    version = "1.0",
    author = "Tyler Burkhardt (stackpointcloud.com)",
    author_email = "tyler@stackpointcloud.com",
    description = ("1&1 API Client Library for Python"),
    long_description=read('README'),
    license = "Apache 2.0",
    keywords = "oneandone 1&1 1and1 api client cloud server",
    url = "https://github.com/StackPointCloud/oneandone-cloudserver-sdk-python",
    packages=['1and1'],
    install_requires=['requests>=2.0.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Internet :: WWW/HTTP'],
    ],
)