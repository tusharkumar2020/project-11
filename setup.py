from setuptools import setup, find_packages

setup(
    name="EmotionDetection",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    description="A package for detecting emotions using Watson NLP",
    author="Your Name",
    author_email="your.email@example.com",
)
