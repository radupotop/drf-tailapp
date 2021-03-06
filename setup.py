from pathlib import Path

from setuptools import find_packages, setup


def read_requirements(filename):
    contents = Path(filename).read_text().strip('\n')
    return [line for line in contents.split('\n') if not line.startswith('-')]


setup(
    name='football_team',
    version='0.1',
    packages=find_packages(),
    install_requires=read_requirements('requirements.txt'),
    # extras_require=dict(tests=read_requirements('requirements.test.txt')),
)
