#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

extras_require = {
    "test": [  # `test` GitHub Action jobs uses this
        "pytest>=6.0",  # Core testing package
        "pytest-xdist",  # multi-process runner
        "pytest-cov",  # Coverage analyzer plugin
        "pytest-mock",  # For creating mocks
        "eip712",
        "hypothesis>=6.2.0,<7.0",  # Strategy-based fuzzer
    ],
    "lint": [
        "black>=22.12.0",  # auto-formatter and linter
        "mypy>=0.991",  # Static type analyzer
        "types-setuptools",  # Needed due to mypy typeshed
        "flake8>=5.0.4",  # Style linter
        "isort>=5.10.1",  # Import sorting linter
        "mdformat>=0.7.16",  # Auto-formatter for markdown
        "mdformat-gfm>=0.3.5",  # Needed for formatting GitHub-flavored markdown
        "mdformat-frontmatter>=0.4.1",  # Needed for frontmatters-style headers in issue templates
    ],
    "release": [  # `release` GitHub Action job uses this
        "setuptools",  # Installation tool
        "wheel",  # Packaging tool
        "twine",  # Package upload tool
    ],
    "dev": [
        "commitizen",  # Manage commits and publishing releases
        "pre-commit",  # Ensure that linters are run prior to committing
        "pytest-watch",  # `ptw` test watcher/runner
        "IPython",  # Console for interacting
        "ipdb",  # Debugger (Must use `export PYTHONBREAKPOINT=ipdb.set_trace`)
    ],
}

# NOTE: `pip install -e .[dev]` to install package
extras_require["dev"] = (
    extras_require["test"]
    + extras_require["lint"]
    + extras_require["release"]
    + extras_require["dev"]
)

with open("./README.md") as readme:
    long_description = readme.read()


setup(
    name="ape-ledger",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    description="""ape-ledger: Plugin for Ledger Hardware Wallet""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="ApeWorX Ltd.",
    author_email="admin@apeworx.io",
    url="https://github.com/ApeWorX/ape-ledger",
    include_package_data=True,
    install_requires=[
        "click",  # Use same version as eth-ape
        "eth-ape>=0.6.0,<0.7",
        "hidapi>=0.13.1,<0.14",
        "importlib-metadata",
        "rlp>=3.0.0",
        # EF Dependencies
        "eth-account",  # Use same version as eth-ape
        "eth-typing",  # Influenced by eth-ape
        "eth-utils",  # Use same version as eth-ape
        "hexbytes",  # Use same version as eth-ape
    ],
    entry_points={
        "ape_cli_subcommands": [
            "ape_ledger=ape_ledger._cli:cli",
        ],
    },
    python_requires=">=3.8,<4",
    extras_require=extras_require,
    py_modules=["ape_ledger"],
    license="Apache-2.0",
    zip_safe=False,
    keywords="ethereum",
    packages=find_packages(exclude=["tests", "tests.*"]),
    package_data={"ape_ledger": ["py.typed"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
