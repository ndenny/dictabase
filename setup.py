from setuptools import setup, find_packages

pkg_version = '0.1'

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(name='dictabase',
      version=pkg_version,
      description="DictaBase - Dictionaries are Magic. And maybe even Databases.",
      long_description=open('README.md', 'r').read(),
      classifiers=[
          # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
          'Development Status :: 4 - Beta',

          # Pick your license as you wish (should match "license" above)
          'License :: OSI Approved :: Apache Software License',

          # Indicate who your project is intended for
          "Intended Audience :: Developers",
          "Topic :: Software Development :: Testing",
          "Topic :: Utilities",

          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",

          "Environment :: Console",
      ],
      keywords='dictionary database',
      author='Nick Denny',
      author_email='nick@apimetrics.com',
      url='https://github.com/ndenny/dictabase',
      license='License :: OSI Approved :: Apache Software License',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=install_requires,
      entry_points={}
     )
