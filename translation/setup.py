import setuptools

with open("REAME.md", "r") as readme:
    description = readme.read()

setuptools.setup(
    name='Epic_Translation',
    version='0.0.1',
    packages=['translation',],
    long_description=description,
)
