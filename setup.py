from setuptools import setup

setup(
    name='mrtopo',
    version='0.0.1',
    packages=['mrtopo', 'mrtopo.util', 'mrtopo.error', 'mrtopo.logger', 'mrtopo.mutator', 'mrtopo.validator',
              'mrtopo.structures', 'mrtopo.structures.networks', 'mrtopo.structures.networks.ring', 'mrtopo.translator',
              'mrtopo.interpreter'],
    url='https://github.com/FaizChishtie/mrtopo',
    license='MIT',
    author='faizchishtie',
    author_email='faizchishtie@gmail.com',
    description='Mutate Mininet topology files with MrTopo'
)
