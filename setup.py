from setuptools import setup, find_packages

setup(
    name="foo_parameterization",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'foo_parameterization=foo_parameterization.cli:main',
        ],
    },
    author="Vanshika Mehrotra",
    description="A package to calculate the Foo et al. parameterization for the volume of a sphere.",
    url="https://github.com/yourusername/foo_parameterization",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
