import subprocess

#/usr/bin/python3


git submodule add git@github.com:workashokg15/rust_study.git

subprocess.run(["git", "submodule", "update", "--init", "--recursive"])
