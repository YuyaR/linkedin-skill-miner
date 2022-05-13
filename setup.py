from setuptools import setup
from setuptools import find_packages

setup(
    name='careerskills',
    version='0.1.1',
    description='A graphic user interface that allows you to find out the top desired transferable skills in your dream career; can be run in docker and upload results to AWS postgreSQL database',
    url='https://github.com/YuyaR/linkedin-skill-miner.git',
    author='Yuya Ra',
    author_email='yuyacademia@gmail.com',
    license='agpl-3',
    packages=find_packages(),
    install_requires=['dotenv', 'selenium','pandas','matplotlib']
)