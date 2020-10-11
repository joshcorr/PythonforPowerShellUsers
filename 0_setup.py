# install WSL2 and register distro (ubuntu)

# install pyenv
# Follow https://github.com/pyenv/pyenv-installer
# sudo apt-get update; suod apt-get install --no-install-recommends ...

# install python version and set global
# pyenv install 3.8.5
# pyenv global 3.8.5

# Setup pipx (for executing python pacakges)
# installs for use for the specific user
# python3 -m pip install --user pipx
# pipx install pycowsay
# now able to execute pycowsay from cmdline

# all other pacakges use Setup venv for pip
# python3 -m venv testenv
# source testenv/bin/activate
# pip install <packagename>