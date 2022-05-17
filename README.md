# Python Algorithms & Data Structures

[![lint: flake8][1]][2] [![test: pytest][3]][4] [![codacy code quality][5]][6] [![codefactor code quality][7]][8]

This repository is dedicated to the study of algorithms, data structures,
Python, and to our love for programming and software engineering!

## Contributing

[![contributors][25]][26] [![commit activity][27]][28] [![issues][29]][30]
[![issues closed][31]][32] [![issues pr][33]][34] [![issues pr closed][35]][36]

Code reviews, pull requests, issues, and discussions are always welcome!

## Main Toolchain

- Package manager
  - [poetry][80]
- Unit testing
  - [pytest][81]
- Static type check
  - [mypy][82]
- Style, linting, and other static analysis
  - [flake8][83]
  - [prospector][84]

## Dependency Management with Poetry

Poetry is our package manager. These are some important commands.

```bash
poetry install          # Install all dependencies included in pyproject.toml
poetry update           # Update dependencies to latest versions
poetry add <dependency> # Install new dependency

poetry show           # List all available packages
poetry show -o        # List all outdated packages
poetry show <package> # See package details

poetry shell         # Activate virtual envvironment
poetry run <command> # Run command inside virtual environment

poetry check            # Validate structure of pyproject.toml
poetry search <package> # Search packages on remote index
```

## Similar Resources

You can find similar repositories for other languages in the following links:

- [Haskell][103]
- [JavaScript][101]
- [OCaml][102]

---

[![total lines][51]][52] [![code size][53]][54] [![repo size][55]][56]

[1]: https://img.shields.io/badge/lint-flake8-blue.svg
[2]: http://flake8.pycqa.org/
[3]: https://img.shields.io/badge/test-pytest-blue.svg
[4]: https://docs.pytest.org/
[5]: https://app.codacy.com/project/badge/Grade/7ffcb99f0c674b2abab6c7ed4915a280
[6]: https://www.codacy.com/gh/JCPedroza/algorithms-and-data-structures-py/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=JCPedroza/algorithms-and-data-structures-py&amp;utm_campaign=Badge_Grade
[7]: https://www.codefactor.io/repository/github/jcpedroza/algorithms-and-data-structures-py/badge
[8]: https://www.codefactor.io/repository/github/jcpedroza/algorithms-and-data-structures-py

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

[101]: https://github.com/JCPedroza/algorithms-and-data-structures-js
[102]: https://github.com/JCPedroza/algorithms-and-data-structures-ocaml
[103]: https://github.com/JCPedroza/algorithms-and-data-structures-hs
