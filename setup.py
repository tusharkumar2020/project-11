from setuptools import setup, find_packages

setup(
    name='EmotionDetection',
    version='0.1',
    packages=find_packages(),
    install_requires=[
       'requests>=2.25.1',
        'json>=3.13'
    ],
    entry_points={
        'console_scripts': [
            'import emotion_detection'
        ],
    },
)