import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Illustrated_MBTI",
    version="0.0.1",
    author="MasumotoAmika",
    author_email="s2222094@stu.musashino-u.ac.jp",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/a-chon/DS_SD",
    project_urls={
        "Bug Tracker": "https://github.com/a-chon/DS_SD/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    py_modules=["MBTI"],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "MBTI=MBTI:main",
        ]
    },
)
