from setuptools import setup, find_packages

setup(
    name='cmsplugin-porticus',
    version=__import__('cmsplugin_porticus').__version__,
    description=__import__('cmsplugin_porticus').__doc__,
    long_description=open('README.rst').read(),
    author='David Thenon',
    author_email='dthenon@emencia.com',
    url='http://pypi.python.org/pypi/cmsplugin-porticus',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'Django>=1.7',
        'django-cms>=3.1',
        'porticus>=1.0.0',
    ],
    include_package_data=True,
    zip_safe=False
)