from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    this function will retun list of requirement
    
    """
    requirement_1st:List[str]=[]
    try:
        with open ('requirements.txt','r') as file:
            #read lines for the file 
            lines=file.readlines()
            ##process each line 
            for line in lines:
                requirement=line.strip()
                ## igonore emptly lines and -e.
                if requirement and requirement!='-e .':
                    requirement_1st.append(requirement)
    except FileNotFoundError:
        print("requirement.txt file not found ")

    return requirement_1st 

print(get_requirements())    

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Suraj Thakur",
    author_email="st12365489@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)

