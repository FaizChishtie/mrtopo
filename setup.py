import setuptools
import re

with open("README.md", "r") as fh:
    long_description = fh.read()

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('mrtopo/__main__.py').read(),
    re.M
    ).group(1)

setuptools.setup(
    name='mrtopo',
    version=version,
    packages=setuptools.find_packages(),
    url='https://github.com/FaizChishtie/mrtopo',
    license='MIT',
    author='faizchishtie',
    author_email='faizchishtie@gmail.com',
    description='Mutate Mininet topology files with MrTopo',
    python_requires='>=3.0',
    # entry_points={'console_scripts': ['mrtopo = mrtopo.__main__:main']},
    long_description=long_description,
    install_requires=[
            'mininet'
    ]
)
