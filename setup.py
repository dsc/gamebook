try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='gamebook',
    version='0.1',
    description='Choose Your Own Choose Your Own Adventure!',
    author=['David Schoonover', 'Leigh Honeywell'],
    author_email=['dsc@less.ly', 'leigh@hypatia.ca'],,
    url='http://github.com/dsc/gamebook',
    install_requires=[
        "Pylons>=1.0",
        "lazyboy>0.7.5",
    ],
    setup_requires=["PasteScript>=1.6.3"],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    package_data={'gamebook': ['i18n/*/LC_MESSAGES/*.mo']},
    #message_extractors={'gamebook': [
    #        ('**.py', 'python', None),
    #        ('templates/**.mako', 'mako', {'input_encoding': 'utf-8'}),
    #        ('public/**', 'ignore', None)]},
    zip_safe=False,
    paster_plugins=['PasteScript', 'Pylons'],
    entry_points="""
    [paste.app_factory]
    main = gamebook.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller
    """,
)
