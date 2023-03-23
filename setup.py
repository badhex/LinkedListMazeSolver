from setuptools import setup

setup(
    name='LinkedListMazeSolver',
    version='1.0.0',
    packages=[],
    package_dir={'LinkedListMazeSolver':'LinkedListMazeSolver', 'tests':'tests'},
    url='https://github.com/badhex/LinkedListMazeSolver',
    license='MIT',
    author='badhex',
    author_email='badhex@inflict.io',
    description='This class is designed to solve a linked-list dictonary maze using the A* or Breadth-First algorithms. It takes a maze as input, represented as a dictionary where each key represents a room and the exits value is another dictionary that contains the exits of the room. '
)
