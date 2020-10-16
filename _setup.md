# install WSL2 and register distro (ubuntu)
 - https://docs.microsoft.com/en-us/windows/wsl/install-win10
 - https://www.microsoft.com/store/productId/9NBLGGH4MSV6
 - wsl --set-default-version 2

# install pyenv
 - Follow https://github.com/pyenv/pyenv-installer
 - sudo apt update -y; sudo apt upgrade -y; sudo apt-get install ...

# install python version and set global
 - pyenv install 3.8.6
 - pyenv install 3.9.0
 - pyenv global 3.9.0


# Setup pipx (for executing python pacakges)
 - installs for use for the specific user
 - python3 -m pip install --user pipx
 - python3 -m pipx ensurepath
 - pipx install pycowsay
 - now able to execute pycowsay from cmdline

# all other pacakges use Setup venv for pip
 - python3 -m venv testenv
 - source testenv/bin/activate
 - https://pypi.org/project/tablib/
 - pip install tablib
