from setuptools import setup

setup(name='sample-app',
      version='0.1',
      description='Sample app to demonstrate pulling unwanted dependencies',
      url='http://github.com/jtiai/pipsync-issue',
      author='Jani Tiainen',
      author_email='jani.tiainen@tintti.net',
      license='BSD',
      packages=['sample_app'],
      install_requires=['Django==1.11.2'],
      zip_safe=False)