'''
A setup.py file is a standard Python script used for packaging and distributing Python projects. It contains metadata and configuration for your project, allowing tools like `pip` and `setuptools` to build, install, and distribute your package.

**Key purposes of setup.py:**
- Defines project name, version, author, and description.
- Lists dependencies required for installation.
- Specifies which files and packages to include.
- Allows building source and binary distributions.

**Typical example:**
````python
# setup.py
from setuptools import setup, find_packages

setup(
    name="your_project_name",
    version="0.1.0",
    description="A short description of your project",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        # List your dependencies here, e.g. "requests"
    ],
)
````

**Gotcha:**  
If you want your project to be installable via `pip`, a properly configured setup.py is essential. Modern Python projects may also use `pyproject.toml` for configuration, but setup.py is still widely used and supported.
'''


from setuptools import setup, find_packages
from typing import List


from typing import List

def get_requirements(file_path: str = "requirements.txt") -> List[str]:
    """
    Reads the requirements from a file and returns them as a list,
    ignoring comments, empty lines, and editable installs like '-e .'.
    
    Args:
        file_path (str): Path to the requirements file.
        
    Returns:
        List[str]: A list of package names.
    """
    with open(file_path, 'r') as file:
        return [
            line.strip()
            for line in file
            if line.strip() and not line.startswith('#') and not line.strip().startswith('-e .')
        ]

# print(get_requirements())
setup(
    name="network_security",
    version="0.1.0",
    author="Yashas M B",
    author_email="yashasmb2003@gmail.com",
    description="A project for network security analysis and monitoring",
    packages=find_packages(),
    install_requires=get_requirements(),
)