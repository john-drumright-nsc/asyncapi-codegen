from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fp:
    requirements = fp.read().split('\n')

setup(name='asyncapi-codegen',
      version='0.0.1',
      url='http://github.com/pearmaster/asyncapi-codgen',
      author='Jacob Brunson',
      author_email='pypi@jacobbrunson.com',
      description="Generate C++ for an AsyncAPI Specification",
      long_description=long_description,
      long_description_content_type="text/markdown",
      license='GPLv2',
      packages=[
          'asyncapicodegen',
          'asyncapicodegen.templates.cpp',
      ],
      package_data={
            'asyncapicodegen.templates.cpp': ['*.jinja2']
      },
      zip_safe=False,
      install_requires=requirements,
      include_package_data=True,
      python_requires='>=3.7',
)