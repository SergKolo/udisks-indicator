import setuptools
from distutils.core import setup

setup(
    name='udisks-indicator',
    version='2.1',
    license='MIT',
    description='Indicator for viewing information about mounted filesystems via mostly DBus and UDisks',
    author='Sergiy Kolodyazhnyy',
    author_email='1047481448@qq.com',
    url='https://github.com/SergKolo/udisks-indicator',
    packages=['udisks_indicator'],
    install_requires=['dbus-python'],
    data_files=[
        ('/usr/share/applications',['udisks_indicator/udisks_indicator.desktop'])
    ],
    classifiers=[
        'Environment :: X11 Applications :: GTK',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.0',
        'Topic :: Utilities'
    ]
)
