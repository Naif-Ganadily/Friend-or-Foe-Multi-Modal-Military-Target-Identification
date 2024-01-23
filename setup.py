from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements from the requirements.txt file
    '''
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = [req.strip() for req in file_obj if req.strip() and req.strip() != HYPEN_E_DOT]

    return requirements

setup(
    name = 'Friend or Foe: Battlefield Adversary Detection',
    version = '0.0.1',
    authors= ['Andrew Jeon', 'Bassam Halabiya', 'Naif A. Ganadily', 'Zachary Saunders'],
    authors_emails = ['andrewjjeon@gmail.com', 'b.halabiya@gmail.com', 'ganadilynaif@gmail.com', 'zacharydavidsaunders@gmail.com'],
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')


)