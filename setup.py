from setuptools import setup, find_namespace_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='clean_folder',
    version='0.1.0',
    author='Volodymyr Kravchenko',
    author_email='vlodya@gmail.com',
    description='HW 07. Clean Folder',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VlodyaKr/Python-6-Core-HomeWork-07",
    project_urls={
        "Bug Tracker": "https://github.com/VlodyaKr/Python-6-Core-HomeWork-07/issues",
    },
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean_folder=clean_folder.clean:start']}
)