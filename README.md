# CULT

## About CULT

![CULT Mascot](CULT.png)

CULT is a project name for a collaborative quantum mechanics simulation. The goal of CULT is to simulate environments and their objects using quantum mechanics to predict the future state of a system. The name is intentionally whimsical.

This project will focus on leveraging the power of both classical computing and quantum computing to simulate the future state of a system. Initially, the project will focus on simulating very small systems of 2-level qauntum systems such as the spin of an electron, energy levels of an atom, or polarization states of a photon, as these objects exhibit quantum properties that qubits in quantum computers are able to simulate. Additionally, such systems are small enough that they can be simulated on classical computers.

The project is currently in a research-heavy phase. While CULT members (humor intended) determine the current limitations of quantum computing and classical computing quantum simulations and their frameworks, tangible action items will be added to the project roadmap.

Thanks for reading!

## Environment Setup

To ensure consistency across various development environments, this project's instructions will use `pyenv` for Python version management and `pyenv-virtualenv` for handling virtual environments. This project assumes you'll be using WSL with Ubuntu or a similar Linux distribution (like Debian).

### Installation and Setup

- **Pre-steps**: navigate to the root of this project's directory, and run the following command to make sure your Linux has the required dependencies for `pyenv`:

    ```bash
    sudo apt-get update
    sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev wget curl llvm libncursesw5-dev xz-utils \
    tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
    ```

1. Install `pyenv`, which will also install `pyenv-virtualenv`:

    ```bash
    curl https://pyenv.run | bash
    ```

2. Add the following to your `~/.bashrc` (if you're using WSL Ubuntu):

    ```bash
    export PYENV_ROOT="$HOME/.pyenv"
    [[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init -)"
    ```

3. Restart your terminal or run `source ~/.bashrc` to reload your `~/.bashrc` file.

4. Install Python 3.11.7 (or latest version):

     ```bash
    pyenv install 3.11.7
    ```

5. Set Python 3.11.7 as your global Python version:

    ```bash
    pyenv global 3.11.7
    ```

    - You can check your Python version by running `python --version`.

6. Create a virtual environment for this project:

    ```bash
    pyenv virtualenv 3.11.7 cult
    ```

7. Activate the virtual environment:

    ```bash
    pyenv activate cult
    ```

    - You should see `(cult)` at the beginning of your terminal prompt, which indicates that you're in the virtual environment.

8. Update pip and install the project's dependencies:

    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

That's it! You're done with the setup. Make sure to activate your virtual environment (cult) every time you work on this project.

![CULT Mascot](CULT2.png)
