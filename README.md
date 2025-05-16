Simpliest way to setup a python uv workspace

```bash
uv venv # create virtual environment
source .venv/bin/activate # very important

uv build
uv sync --all-packages # have to run sync after every build

python packages/my-app/main.py
```

## IDE

In VSCode, make sure Python extension is installed, and select Python interpreter from command palattee once virtual env is created.
