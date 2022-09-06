# Python Algorithms & Data Structures

[![linux build & tests][13]][14]
[![codeql][15]][16]

[![python][19]][20]
[![dependabot][21]][22]

[![license MIT][9]][10]
[![style black][11]][12]
[![lint: flake8][1]][2]
[![test: pytest][3]][4]
[![codacy code quality][5]][6]
[![codefactor code quality][7]][8]

Algorithms and data structures implemented in Python. Here you'll find:

- Implementations of algorithms and data structures
- Solutions for problems, prompts, challenges, and popular interview questions

## Usage

### Installation

To install the project dependencies, you can either use [poetry][80] and
`poetry install` (recommended), or install the dependencies globally and manually using
`pip install <dependencies>` and the dependency list in `pyproject.toml`.

```bash
git clone https://github.com/JCPedroza/algorithms-and-data-structures-py.git
cd algorithms-and-data-strcutrues-py
poetry install # Install all packages in the local virtual environment
```

### Unit Testing

```bash
poetry run pytest # Run al unit tests using local virtual environment
pytest            # Run all unit tests using global environment
```

### Other Poetry Commands

```bash
poetry shell         # Activate shell inside local virtual environment
poetry run <command> # Run command inside local virtual environment
poetry check         # Validate structure of pyproject.toml
```

## Contributing

[![contributors][25]][26]
[![commit activity][27]][28]
[![issues][29]][30]
[![issues closed][31]][32]
[![issues pr][33]][34]
[![issues pr closed][35]][36]

Code reviews, pull requests, issues, and discussions are always welcome!

## Main Toolchain

- Package manager
  - [poetry][80]
- Unit testing
  - [pytest][81]
- Static type check
  - [mypy][82]
- Style, linting, formatting, and other static analysis
  - [flake8][83]
  - [black][85]
  - [prospector][84]

## Similar Resources

You can find similar repositories for other languages in the following links:

- [Haskell][103]
- [JavaScript][101]
- [SML][104]
- [OCaml][102]

---

[![total lines][51]][52]
[![code size][53]][54]
[![repo size][55]][56]

[1]: https://img.shields.io/badge/lint-flake8-blue.svg
[2]: http://flake8.pycqa.org/
[3]: https://img.shields.io/badge/test-pytest-blue.svg
[4]: https://docs.pytest.org/
[5]: https://app.codacy.com/project/badge/Grade/7ffcb99f0c674b2abab6c7ed4915a280
[6]: https://www.codacy.com/gh/JCPedroza/algorithms-and-data-structures-py/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=JCPedroza/algorithms-and-data-structures-py&amp;utm_campaign=Badge_Grade
[7]: https://www.codefactor.io/repository/github/jcpedroza/algorithms-and-data-structures-py/badge
[8]: https://www.codefactor.io/repository/github/jcpedroza/algorithms-and-data-structures-py
[9]: https://img.shields.io/github/license/jcpedroza/algorithms-and-data-structures-py
[10]: https://en.wikipedia.org/wiki/MIT_License
[11]: https://img.shields.io/badge/code%20style-black-000000.svg
[12]: https://github.com/psf/black
[13]: https://github.com/JCPedroza/algorithms-and-data-structures-py/actions/workflows/linux.yml/badge.svg
[14]: https://github.com/JCPedroza/algorithms-and-data-structures-py/actions/workflows/linux.yml
[15]: https://github.com/JCPedroza/algorithms-and-data-structures-py/actions/workflows/codeql.yml/badge.svg
[16]: https://github.com/JCPedroza/algorithms-and-data-structures-py/actions/workflows/codeql.yml

[19]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[20]: https://github.com/python/cpython
[21]: https://img.shields.io/badge/dependabot-025E8C?style=for-the-badge&logo=dependabot&logoColor=white
[22]: https://github.com/JCPedroza/algorithms-and-data-structures-py/blob/main/.github/dependabot.yml

[25]: https://img.shields.io/github/contributors/JCPedroza/algorithms-and-data-structures-py
[26]: https://github.com/JCPedroza/algorithms-and-data-structures-py/graphs/contributors
[27]: https://img.shields.io/github/commit-activity/m/JCPedroza/algorithms-and-data-structures-py
[28]: https://github.com/JCPedroza/algorithms-and-data-structures-py/graphs/commit-activity
[29]: https://img.shields.io/github/issues-raw/JCPedroza/algorithms-and-data-structures-py
[30]: https://github.com/JCPedroza/algorithms-and-data-structures-py/issues
[31]: https://img.shields.io/github/issues-closed-raw/JCPedroza/algorithms-and-data-structures-py
[32]: https://github.com/JCPedroza/algorithms-and-data-structures-py/issues
[33]: https://img.shields.io/github/issues-pr-raw/JCPedroza/algorithms-and-data-structures-py
[34]: https://github.com/JCPedroza/algorithms-and-data-structures-py/pulls
[35]: https://img.shields.io/github/issues-pr-closed-raw/JCPedroza/algorithms-and-data-structures-py
[36]: https://github.com/JCPedroza/algorithms-and-data-structures-py/pulls

[51]: https://img.shields.io/tokei/lines/github/jcpedroza/algorithms-and-data-structures-py
[52]: https://img.shields.io/tokei/lines/github/jcpedroza/algorithms-and-data-structures-py
[53]: https://img.shields.io/github/languages/code-size/jcpedroza/algorithms-and-data-structures-py
[54]: https://img.shields.io/github/languages/code-size/jcpedroza/algorithms-and-data-structures-py
[55]: https://img.shields.io/github/repo-size/jcpedroza/algorithms-and-data-structures-py
[56]: https://img.shields.io/github/repo-size/jcpedroza/algorithms-and-data-structures-py

[80]: https://python-poetry.org/
[81]: https://docs.pytest.org
[82]: http://mypy-lang.org/
[83]: https://flake8.pycqa.org/
[84]: https://prospector.landscape.io/en/master/
[85]: https://black.readthedocs.io/en/stable/the_black_code_style/index.html

[101]: https://github.com/JCPedroza/algorithms-and-data-structures-js
[102]: https://github.com/JCPedroza/algorithms-and-data-structures-ocaml
[103]: https://github.com/JCPedroza/algorithms-and-data-structures-hs
[104]: https://github.com/JCPedroza/algorithms-and-data-structures-sml
