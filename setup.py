from setuptools import setup, find_packages

setup(
    name="Soltak",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "paho-mqtt",
        "lynx",
        "pytest"
    ],
    entry_points={
        'console_scripts': [
            'run_calculations=scripts.run_calculations:main',
        ],
    },
)