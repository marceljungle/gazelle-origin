import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gazelle-origin",
    version="3.0.1",
    author="x1ppy",
    author_email="",
    entry_points={
      'console_scripts': [
        'gazelle-origin = gazelleorigin.__main__:main',
      ],
    },
    description="Gazelle origin.yaml generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    include_package_data=True,
    url="https://github.com/x1ppy/gazelle-origin",
    python_requires='>=3.5.2',
    install_requires=[
        "pyyaml",
        "requests",
        "python-dotenv",
    ],
)
