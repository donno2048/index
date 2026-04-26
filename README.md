# Index

A personal python package index (all my packages except _spamcmd_)

UPDATE:
> Every non python 3.14 compatible package was removed in the latest run, will not fix as I'm not really using this.

## Install requirement

`pip3 install tqdm pydonno --no-cache-dir --force-reinstall --no-build-isolation`

## Usage

To create it (all the folders and the main _index.html_) run `python3 main.py`

To create it and run it locally run `python3 main.py run`

To install a package from the index run `pip3 install PACKAGE_NAME --index-url INDEX_URL` if the index is local it will be <http://localhost:8000/>

I'm using GitHub pages to allow such usage: `pip3 install PACKAGE_NAME --index-url https://donno2048.github.io/index/`
