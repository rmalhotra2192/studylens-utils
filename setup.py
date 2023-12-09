from setuptools import setup, find_packages

setup(
    name="studylens-utils",
    version="0.3.1",
    author="Rishabh Malhotra",
    author_email="therishabhmalhotra@gmail.com",
    description="Internal Backend Models for Studylens Project, defined as seperately installable python package for re-use between web backend and data ingestion pipelines. ",
    long_description="Internal Backend Models for Studylens Project, defined as seperately installable python package for re-use between web backend and data ingestion pipelines. ",
    long_description_content_type="text/markdown",
    url="https://github.com/rmalhotra2192/studylens-models",
    packages=find_packages(),
    install_requires=[
        "Django==4.2.6",
        "google-cloud-secret-manager",
        "django-environ",
        "psycopg2-binary==2.9.9",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
