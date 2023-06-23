from setuptools import find_packages,setup

from typing import List

REQUIREMENT_FILE_NAME="requirements.txt"
HYPHEN_E_DOT = "-e ."

#. from means current directory... also hyphen e . is not a libraby so we have to remove it while
     #reading requiremen.txt ...also it is necessary to trigger setup.py file thats why we write it in this
     #this file



def get_requirements()->List[str]:
    
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
    requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
    
    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list



setup(
    name="sensor",
    version="0.0.2",
    author="arvind",
    author_email="arvindparashar007@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements(),
)