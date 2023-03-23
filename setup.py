from setuptools import setup

# read the contents of your README file
from pathlib import Path
from LinkedListMazeSolver import __version__

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='LinkedListMazeSolver',
    version=__version__,
    packages=['LinkedListMazeSolver'],
    package_dir={'LinkedListMazeSolver': 'LinkedListMazeSolver', 'tests': 'tests'},
    url='https://github.com/badhex/LinkedListMazeSolver',
    license='MIT',
    author='badhex',
    author_email='badhex@inflict.io',
    description='This class is designed to solve a linked-list dictonary maze using the A* or Breadth-First algorithms. It takes a maze as input, represented as a dictionary where each key represents a room and the exits value is another dictionary that contains the exits of the room. ',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
