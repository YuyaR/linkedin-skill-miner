from setuptools import setup
from setuptools import find_packages

setup(
    name='careerskills',
    version='0.0.1',
    description='A graphic user interface that allows you to find out the top desired transferable skills in your dream career',
    url='https://github.com/YuyaR/linkedin-skill-miner.git',
    author='Yuya Ra',
    License='MIT',
    packages=find_packages(),
    install_requires=['selenium','pandas','matplotlib']
)