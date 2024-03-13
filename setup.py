from setuptools import setup,find_packages
from typing import List


def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open("requirements.txt") as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

setup(
    name = "mlproj",
    version="0.0.1",
    author="Luv",
    author_email="luvarora2003@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")
)