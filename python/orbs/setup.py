from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='ORBS',
      version='0.1',
      description='ORBS implementation in Python',
      url='https://github.com/greenmonn/daily-coding',
      author='greenmon',
      author_email='greenmon@kaist.ac.kr',
      license='MIT',
      long_description=long_description,
      long_description_content_type="text/markdown",
      packages=setuptools.find_packages(),
      classifiers=[
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.7',
      ],
      zip_safe=False)
