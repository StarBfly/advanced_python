import os
from setuptools import setup


def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


setup(
    name="Knapsack solution",
    version="1.0",
    description="Small util to solve 0/1 knapsack problem",
    author="Marharyta Hancharenka",
    author_email="Marharyta_Hancharenka@epam.com",
    packages=["knapsack_solution", ],
    long_description=read('README.md'),
    python_requires='>=3.6',
    entry_points={'console_scripts': [
        'knapsack_solution = knapsack_solution.homework_10:main',
    ],
    }
)
