from setuptools import find_packages, setup

with open("README.md", "r", encoding="UTF-8") as readme_file:
    readme = readme_file.read()

requirements = ["opencv-python==4.6.0.66"]

setup(
    name="planetary_image_processor",
    version="0.0.1",
    author="Gero Bergk",
    author_email="grbergk@gmail.com",
    description="Planetary Image Processor",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Gero-B/Planetary-Image-Processor",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
