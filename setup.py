import os
from typing import Optional
from setuptools import setup, find_packages


def get_socivolta_package_git_requirement(package_name: str,
                                          repo_name: Optional[str] = None,
                                          git_branch: str = "master") -> str:
    """Get a string that is added to the private dependencies.

    Used for internal packages. If the GIT_USERNAME and GIT_PASSWORD environment
    variables are set, then https is used to install the SociVolta private
    repository. Otherwise, ssh is used (which requires the user to have valid ssh
    keys on the machine performing the setup).

    The GIT_PASSWORD should be an app password with read repository rights for
    the requested packages.

    """
    git_username = os.environ.get('GIT_USERNAME')
    git_password = os.environ.get('GIT_PASSWORD')

    if repo_name is None:
        repo_name = package_name

    if git_username is None or git_password is None:
        return (f'{package_name} @ git+ssh://git@bitbucket.org/SociVolta/{repo_name}.git'
                f'@{git_branch}')
    return (f'{package_name} @ git+https://{git_username}:{git_password}@bitbucket.org'
            f'/SociVolta/{repo_name}.git@{git_branch}')

setup(
    name='apilambdatest',
    version='0.1',
    description='Test for cross-region api gateway and lambda deployment.',
    url=f'https://bitbucket.org/SociVolta/apilambdatest.git',
    author='Socivolta Inc.',
    author_email='info@socivolta.com',
    license='Socivolta Inc.',
    packages=find_packages(),
    zip_safe=False,
    python_requires=">=3.7",
    install_requires=[
        get_socivolta_package_git_requirement("svcred")
    ],
    extras_require={
        "dev": [
            "pytest>=6",
            'pytest-asyncio',
            'pycodestyle',
            'pytest-cov',
            get_socivolta_package_git_requirement("svlambda")
        ]
    },
    data_files=[
    ],
    include_package_data=True,
)