# dev-conventions-toolkit-examples
规范化开发：使用 pre-commit、Black formatter、isort、clang-format 和 git-cz 工具来实现规范化的开发流程和代码风格。

## Tooling
### pre-commit

```shell
pre-commit install
```

### Black
Enforce [PEP8](https://www.python.org/dev/peps/pep-0008/) formatting of Python code by using the uncompromising Black formatter.

`Black` is run automatically with `pre-commit` .

Run Black manually with

```shell
black .
```

### isort
Use [isort](https://github.com/PyCQA/isort) to sort imports in Python code.

`isort` is run automatically with `pre-commit` .

Run isort manually with

```shell
isort --profile=black --thirdparty="nest" .
```
### clang-format
Use [clang-format](http://clang.llvm.org/docs/ClangFormat.html) to format C/C++ code. Clang-format configuration is specified in the `.clang-format` file.

`clang-format` is run automatically with `pre-commit` .


### git-cz

- Install

```shell
npm install -g --force git-cz
```

- Use `git-cz` instead of `git commit` .
