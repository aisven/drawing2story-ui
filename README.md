# drawing2story-ui

This project is a user interface to the tool drawind2story.

## TL;DR

Install poetry using the normal installer.
As of 2023-11-12 this installs Poetry 1.6.1 which is perfect.
See: https://python-poetry.org/docs/#installing-with-the-official-installer
The installation command should be something like this.

``` 
curl -sSL https://install.python-poetry.org | python3 -
```
Now to run the unit tests including reporting of coverage, do the following.

```
poetry install --no-root
poetry run pytest tests --cov=drawing2story_ui --cov-report=xml:coverage.xml
poetry run coverage report -m
```

In case you want to run code formatting.

```
poetry run black drawing2story_ui
poetry run black tests
```

In case you want to run code linting.

```
poetry run flake8 drawing2story_ui
poetry run flake8 tests
```

For more guidance and slight variations of the commands read the sections below.
Also, the sections below describe how to define dependencies and how to install dependencies.

## The python environment compatibility

### Using conda, pip, Poetry

In case you want to sync the packages in your local active python environment
to the ones defined in `pyproject.toml`, i.e. have Poetry remove any dependencies
not included in `pyproject.toml` and install any that are not yet present,
run the following command.

```
poetry install --no-root --sync
```

Note that Poetry is compatible with conda and pip in this way, i.e. if your
local active python environment has been created and activated with conda
and had been managed by pip, after this command, `pip -v list`, i.e. in case pip
refers to the same environment, should show notably the dependencies defined
in `pyproject.toml` plus relevant transitive dependencies.
If the list of packages is not exactly clean, this would not be the fault of Poetry.
You might have some additional dependencies sneaking in via some legacy backyard
which `pip -v list` considers. For example, you might have previously installed
some packages using pip which ended up in your home directory under the path
`.local/lib/python3.10/site-packages`. Note that thanks to the `-v` you can
see where exactly each package in the python environment resides and which
installer installed it.

## So this project uses poetry

### Documentation of poetry

This project is using poetry and its conventions.

Make sure you have read and understood the following pages of the poetry documentation. 15 to 20 minutes should be
enough time for a first read to get the ideas, and of course one may consult the documentation again later on demand.

[poetry Basic Usage](https://python-poetry.org/docs/basic-usage/)

[poetry pyproject.toml configuration file](https://python-poetry.org/docs/pyproject/)

[TOML](https://toml.io/en/)

[poetry Managing Dependencies](https://python-poetry.org/docs/managing-dependencies/)

While reading these pages, compare with the contents of the file `pyproject.toml` in this project, or do the comparison
after the reading. It will help you understand the features and poetry configuration sections used in this project.

## Poetry and your environment

### Check which python it is

With poetry you can just bring your own python environment. For example, if a conda environment is activated in your
shell, poetry will use that. To investigate which python poetry is currently using, use the following command.

`poetry run which python`

Note that if you did not bring a python environment, poetry can just create one using its own convention.

### Define dependencies

Usually, developers have already defined the dependencies and you can just skip this section.
However, here follows a description how to add, change, remove dependencies.

To alter the dependencies of the project if needed, you would perform three steps.

First, you would edit the sections `tool.poetry.dependencies` and `tool.poetry.group.dev.dependencies` in
`pyproject.toml` as applicable.

Second, you would run the following command.

`poetry update`

If it fails, you usually would fix the problems by further editing `pyproject.toml` and running the command again.
The command performs dependency resolutions in a detailed, exact, standardized way and updates the `poetry.lock` file.

Lastly, if all is fine, you would commit and push the files `pyproject.toml` and `poetry.lock` to the git repository.

### Install defined dependencies

To install the dependencies of the project, including the dev dependencies, without installing the project itself,
use the following command. Note that the `--no-root` tells poetry not to install the project itself.

`poetry install --no-root`

### Alternatively install only runtime dependencies

During creation of a Docker image or in other situations, you may want to only install the runtime dependencies of the
project. You can do so with the following command.

`poetry install --no-root --only main`

### Alternatively sync your environment to contain only the runtime dependencies

The following command will remove any packages from your environment that are not among the runtime dependencies of the
poetry project. This is the power of the sync option. For example, this would remove the dev dependencies if they had
previously been installed.

`poetry install --no-root --only main --sync`

### Alternatively sync your environment to contain only the dev dependencies

Occasionally, when studying the actual dev dependencies, the following command can be helpful, after which you end up
with your environment only containing the dev dependencies. Again, this is the power of the sync option.

`poetry install --no-root --only dev --sync`

## Code quality concerns

### Running code formatter

To run the code formatter on the production code, use the following command.

`poetry run black drawing2story_ui`

You are encouraged to also run it on the test sources.

`poetry run black tests`

### Running linter

To run the linter on the production code, use the following command.

`poetry run flake8 drawing2story_ui`

You are encouraged to also run it on the test sources.

`poetry run flake8 tests`

### Running the unit tests

Use the following command to execute the unit tests via pytest. Note that this will run the auto-discovery of all tests
that are in the directory `${project_root}/tests`.

`poetry run pytest`

### Running the unit tests with code coverage

To also obtain the report about coverage, run the tests using the following two commands in order.

Note that the file  name `coverage.xml` is very typical and also contained in many default `.gitignore` templates of
IDEs such as PyCharm.  If needed for example in CI, both the directory and the file name can be changed.

Also note that another file called `.coverage`, which is actally a binary formatted file, will automatically be created
and is also contained in default `.gitignore`templates.

`poetry run pytest tests --cov=drawing2story_ui --cov-report=xml:coverage.xml`

To see the report on the command line, use the following command.

`poetry run coverage report -m`
