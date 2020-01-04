import setuptools

with open("README.rst", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="django-essence",
    version="0.1.0",
    author="Caio Carrara",
    author_email="eu@caiocarrara.com.br",
    description="Django reusable app with generic and essencial resources.",
    long_description=long_description,
    url="https://github.com/cacarrara/django-essence",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content ",
    ],
)
