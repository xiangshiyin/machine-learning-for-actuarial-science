from jinja2 import Environment, FileSystemLoader
import os
import typer
from typing_extensions import Annotated
import logging

# Configure the logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)
######## Utility functions ########
def render_from_jinja_template(template_path, context):
    """
    Render a Jinja template with the given context.

    Args:
    - template_path (str): The path to the Jinja template file.
    - context (dict): The context to render the template with.
        Example:
        {
            "course_name": "machine-learning-for-actuarial-science",
            "semester": "2025-spring",
            "week": "01",
        }

    Returns:
    - tuple: A tuple containing the rendered README and notebook content.
    """
    env = Environment(loader=FileSystemLoader(template_path))
    readme_template = env.get_template("readme_template.j2")
    notebook_template = env.get_template("notebook_template.j2")
    return readme_template.render(context), notebook_template.render(context)


def create_folder_if_not_exists(folder_path):
    """
    Create a folder if it does not exist.

    Args:
    - folder_path (str): The path to the folder to create.
    """
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        logger.info(f"Folder {folder_path} already exists.")
    else:
        os.makedirs(folder_path)
        logger.info(f"Folder {folder_path} created.")


def create_file_if_not_exists(file_path, content):
    """
    Create a file if it does not exist.

    Args:
    - file_path (str): The path to the file to create.
    """
    if os.path.exists(file_path) and os.path.isfile(file_path):
        logger.info(f"File {file_path} already exists.")
    else:
        with open(file_path, "w") as f:
            f.write(content)
        logger.info(f"File {file_path} created.")


######## CLI ########
app = typer.Typer()


@app.command()
def generate_folders(
    github_user_id: Annotated[str, "Your GitHub user ID."],
    semester: Annotated[str, "The semester of the course."],
    week: Annotated[str, "The week number, expecting a two-digit number."],
    notebook: Annotated[
        bool, "Whether to generate a Jupyter notebook in the week folder."
    ] = False,
):
    """
    Generate the folder structure for a new week of the course.

    Args:
    - github_user_id (str): Your GitHub user ID.
    - semester (str): The semester of the course.
    - week (str): The week number, expecting a two-digit number.
    - notebook (bool): Whether to generate a Jupyter notebook in the week folder.
    """
    week_dir_path = f"./{semester}/week{week}"
    notebook_dir_path = f"{week_dir_path}/notebook"
    data_dir_path = f"{week_dir_path}/data"
    pics_dir_path = f"{week_dir_path}/pics"
    readme_file_path = f"{week_dir_path}/README.md"
    notebook_file_path = f"{notebook_dir_path}/demo.ipynb"

    create_folder_if_not_exists(semester)
    create_folder_if_not_exists(week_dir_path)
    create_folder_if_not_exists(data_dir_path)
    create_folder_if_not_exists(pics_dir_path)

    logger.info("Generating README and notebook content...")
    template_path = os.path.join(os.getcwd(), "utils")
    readme_content, notebook_content = render_from_jinja_template(
        template_path,
        {
            "course_name": "machine-learning-for-actuarial-science",
            "semester": semester,
            "week": week,
            "github_user_id": github_user_id,
        },
    )

    create_file_if_not_exists(readme_file_path, readme_content)
    if notebook:
        create_folder_if_not_exists(notebook_dir_path)
        create_file_if_not_exists(notebook_file_path, notebook_content)


if __name__ == "__main__":
    app()
