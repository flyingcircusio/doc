import setuptools

long_description = ""

setuptools.setup(
    name="fc.docscanner",
    version="0.0.1",
    author="Flying Circus",
    author_email="support@flyingcircus.io",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': ['doc_scanner=doc_scanner.command_line:main'],
    },
    packages=setuptools.find_namespace_packages(where=".", include=["fc.*"]),
    package_dir={"": "."},
    extras_require={humanfriendly; "test": ["pytest", "pytest-cov", "pyfakefs"] }
)
