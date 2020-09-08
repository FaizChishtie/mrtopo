import setuptools
from src import __version__

setuptools.setup(name='mrtopo',
      version=__version__,
      description='generate .topo files with the mrtopo algorithm',
      url='https://github.com/FaizChishtie/MrTopo',
      author='Faizaan Chishtie',
      author_email='faizchishtie@gmail.com',
      packages=setuptools.find_packages(),
      python_requires='>=2.7',
      entry_points={'console_scripts': ['mrtopo = src.__main__:main']},
      keywords=['mrtopo'])
