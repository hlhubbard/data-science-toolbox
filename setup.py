from distutils.core import setup

with open('requirements.txt') as rf:
  setup(
    name='hh_toolbox',
    version='1.0',
    description='Hayleys data science toolbox for mango solution',
    author='Hayley Hubbard',
    author_email='hubbard.hlb@gmail.com',
    packages = [ 'hh_toolbox' ],
    install_requires=rf.readlines()
  )
