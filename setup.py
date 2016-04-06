from setuptools import setup, find_packages

setup(name='pyvisa_drivers',
      version='0.1.0',
      description=u"Python drivers for gpib comm with instruments",
      classifiers=[],
      keywords='pyvisa',
      author=u"Julian Irwin",
      author_email='julian.irwin@gmail.com',
      url='https://github.com/UW-Physics-Rzchlab',
      license='GPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=['mock'],
      setup_requires=['nose>=1.0'],
      extras_require={'test': ['nose']},
      test_suite='nose.collector'
      )
