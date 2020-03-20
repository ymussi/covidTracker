from setuptools import setup

# install requirements of the project
with open("requirements.txt") as req:
    install_requires = req.read()

setup(name='covidTracker',
      version="0.0.1",
      description="Monitoramento de casos do COVID no Brasil.",
      url="",
      author="Yuri Mussi",
      author_email="ymussi@gmail.com",
      license="BSD",
      keywords=" ",
      packages=["covidTracker"],
      zip_safe=False
      ),