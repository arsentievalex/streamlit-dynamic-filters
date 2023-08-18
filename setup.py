from setuptools import setup, find_packages

VERSION = '0.1'
DESCRIPTION = "Dynamic multiselect filters for Streamlit"
LONG_DESCRIPTION = 'This custom components allows users to create dynamic multiselect filters in Streamlit.'

setup(
    name="streamlit-dynamic-filters",
    version=VERSION,
    author="Oleksandr Arsentiev",
    author_email="<arsentiev9393@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['streamlit', 'pandas'],
    keywords=['streamlit', 'custom', 'component'],
    license="MIT",
    url="https://github.com/arsentievalex/streamlit-dynamic-filters",
)