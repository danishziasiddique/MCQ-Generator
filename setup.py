from setuptools import find_packages,setup

setup(
    name='mcq_generator',
    version='0.0.1',
    author='Danish Zia',
    author_email='zia.danishz@ymail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)