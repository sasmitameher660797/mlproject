from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(filepath : str)->list[str]:
    '''
    this function will return the list of requirements
    '''
    requirments=[]
    with open(filepath) as file_obj:
        requirments= file_obj.readlines()
        requirments=[req.replace("/n","") for req in requirements]
        
        if HYPEN_E_DOT in requirments:
           requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Sasmita',
author_email='sasmitameher660797@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)