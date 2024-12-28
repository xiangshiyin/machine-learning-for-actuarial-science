# Environment Setup
---

**Table of Contents**
- [Environment Setup](#environment-setup)
  - [`Python` Environment](#python-environment)
    - [General Requirements](#general-requirements)
    - [Installations](#installations)
      - [`Anaconda` \[Recommended\]](#anaconda-recommended)
      - [`Python` and `Pip` \[Intermediate Users\]](#python-and-pip-intermediate-users)
      - [`Python` and `Poetry` \[Advanced Users\]](#python-and-poetry-advanced-users)
      - [`Docker` \[If you are interested in containerization\]](#docker-if-you-are-interested-in-containerization)
  - [IDE Setup](#ide-setup)
  - [Online Coding Environment](#online-coding-environment)

---

## `Python` Environment
In order to run the code examples in this repository, you need to set up a Python environment with all the necessary libraries installed. Below are the requirements and installation instructions for setting up the environment.

### General Requirements
- Python 3.9 or later
- [Jupyter Notebook](https://jupyter.org/) - All lecture notes and code examples are provided as Jupyter Notebooks.
- Common Python libraries for data analysis (e.g., `notebook`, `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, etc.)

### Installations
#### `Anaconda` [Recommended]
The easiest way to set up a Python environment is to install the [Anaconda Distribution](https://www.anaconda.com/download/success), which comes with all common libraries and tools for data science and machine learning and the Python executable. This should be sufficient for most of the code examples in this repository. Please make sure to choose the correct version for your operating system.

#### `Python` and `Pip` [Intermediate Users]
If you prefer to set up a Python environment from scratch, you can install Python and the necessary libraries using the `pip` package manager. Below are the steps.
1. Install Python 3.9 or later from the [official Python website](https://www.python.org/downloads/).
   - You can also use `pyenv` to manage multiple Python versions on your machine https://github.com/pyenv/pyenv
2. To install the current version of the required libraries, run the following command in your terminal:

    ```bash
    pip install -r https://raw.githubusercontent.com/xiangshiyin/machine-learning-for-actuarial-science/refs/heads/main/requirements.txt
    ```
3. To start the Jupyter Notebook server, run the following command in your terminal:

    ```bash
    jupyter notebook
    ```
4. Open the Jupyter Notebook in your browser and navigate to the desired notebook file to run the code examples.
5. When you are done, deactivate the virtual environment:

    ```bash
    exit
    ```

#### `Python` and `Poetry` [Advanced Users]
If you prefer to set up a Python environment from scratch, you can install Python and the necessary libraries using the `Poetry` package manager. Below are the steps to set up the environment using `Poetry`.

1. Install Python 3.9 or later from the [official Python website](https://www.python.org/downloads/).
   - You can also use `pyenv` to manage multiple Python versions on your machine https://github.com/pyenv/pyenv
2. Install `Poetry` by following the instructions on the [official Poetry website](https://python-poetry.org/docs/).
3. Clone this repository to your local machine.
4. Navigate to the root directory of the repository and run the following command to install the required dependencies:

    ```bash
    # run the following command if you want to create a virtual environment in the project directory
    poetry config virtualenvs.in-project true
    # run the following command to install the dependencies
    poetry install
    ```
5. Activate the virtual environment created by `Poetry`:

    ```bash
    poetry shell
    ```
6. Start the Jupyter Notebook server:

    ```bash
    jupyter notebook
    ```
7. Open the Jupyter Notebook in your browser and navigate to the desired notebook file to run the code examples.
8. When you are done, deactivate the virtual environment:

    ```bash
    exit
    ```
9. You can also run individual notebooks without activating the virtual environment by running the following command:

    ```bash
    poetry run jupyter notebook
    ```

#### `Docker` [If you are interested in containerization]
>>The first time you run the Docker container, it will download the image from the Docker Hub, which may take some time depending on your internet connection speed. Subsequent runs will be faster as the image will be cached on your machine.
1. Install Docker Desktop from the [official Docker website](https://www.docker.com/products/docker-desktop).
2. Clone this repository to your local machine.
3. Navigate to the root directory of the repository and run the following command
    ```bash
    docker run -it --rm -p 8888:8888 -v "${PWD}":/home/jovyan/work jupyter/scipy-notebook
    ```
4. Open the Jupyter Notebook in your browser by following the instructions in the terminal.
5. When you are done, stop the Docker container by pressing `Ctrl+C` in the terminal.
6. You can also run the Docker container in the background by running the following command:
    ```bash
    docker run -d --rm -p 8888:8888 -v "${PWD}":/home/jovyan/work jupyter/scipy-notebook
    ```
7. To stop the Docker container running in the background, run the following command:
    ```bash
    docker ps
    docker stop <CONTAINER_ID>
    ```
    - Replace `<CONTAINER_ID>` with the actual container ID from the output of the `docker ps` command.

## IDE Setup
In addition to Jupyter Notebook, you may also want to set up an Integrated Development Environment (IDE) for writing and running Python code, such as [Visual Studio Code](https://code.visualstudio.com/). In fact, you could use Jupyter Notebook within Visual Studio Code by installing the [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) ([check here](https://code.visualstudio.com/docs/python/jupyter-support-py) for more details).

## Online Coding Environment
You can also open and run the Jupyter Notebooks in this repository directly in your browser using Google Colab by clicking the ![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg) button at the top of each notebook. 
- For general information on Google Colab, check https://colab.research.google.com/
