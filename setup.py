from setuptools import setup, find_packages

setup(
    name="EmotionDetection",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    author="Edson Ramirez",
    author_email="ramirez_edson@hotmail.com",
    description="A package for detecting emotions from text using Watson API",
    url="https://github.com/yourusername/EmotionDetection",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
