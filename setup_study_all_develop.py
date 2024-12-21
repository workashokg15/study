#/usr/bin/env python3
import subprocess


#This script will clone all the study repos and checkout develop, please use feature branches for new develeopments.

subprocess.run(["git", "submodule", "add", "git@github.com:workashokg15/rust_study.git"])

subprocess.run(["git", "submodule", "update", "--init", "--recursive"])

subprocess.run(["git", "submodule", "foreach", "git", "checkout", "-b", "develop"])




