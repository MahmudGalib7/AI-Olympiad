from setuptools import setup, find_packages

setup(
    name='numpy-data-analyzer',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A project for analyzing and visualizing data using NumPy.',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'pandas',
        'seaborn',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)