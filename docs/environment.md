# Environment Setup
---

**Table of Contents**
- [Environment Setup](#environment-setup)
  - [`Python` Environment](#python-environment)
    - [General Requirements](#general-requirements)
    - [Installations](#installations)
      - [`Anaconda` \[Recommended\]](#anaconda-recommended)
      - [`Python` and `Poetry` \[Advanced Users\]](#python-and-poetry-advanced-users)
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

## IDE Setup
In addition to Jupyter Notebook, you may also want to set up an Integrated Development Environment (IDE) for writing and running Python code, such as [Visual Studio Code](https://code.visualstudio.com/). In fact, you could use Jupyter Notebook within Visual Studio Code by installing the [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) ([check here](https://code.visualstudio.com/docs/python/jupyter-support-py) for more details).

## Online Coding Environment
You can also open and run the Jupyter Notebooks in this repository directly in your browser using Google Colab by clicking the ![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg) button at the top of each notebook. 
- For general information on Google Colab, check https://colab.research.google.com/
