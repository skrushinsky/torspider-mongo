from setuptools import setup, find_packages


version = '0.0'

setup(name='torspider-mongo',
      version=version,
      description="Plugin for torspider which saves results to MongoDB.",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='web-crawler web-spider mongo',
      author='Sergey Krushinsky',
      author_email='krushinsky@gmail.com',
      url='',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'tornado',
          'motor',
      ],
      entry_points={
          # see: http://amir.rachum.com/blog/2017/07/28/python-entry-points/
          'torspider_init': [
              'mongo_client = torspidermongo:init_client',
          ],
          'torspider_consume': [
              'mongo_client = torspidermongo:save_report',
          ],
      })
