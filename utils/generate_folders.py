from jinja2 import Environment, FileSystemLoader
import os
import typer
from typing_extensions import Annotated


######## Utility functions ########
def create_folder_if_not_exists(folder_path):
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        print(f"Folder {folder_path} already exists.")
    else:
        os.makedirs(folder_path)
        print(f"Folder {folder_path} created.")


def create_file_if_not_exists(file_path, content):
    if os.path.exists(file_path) and os.path.isfile(file_path):
        print(f"File {file_path} already exists.")
    else:
        with open(file_path, "w") as f:
            f.write(content)
        print(f"File {file_path} created.")


######## CLI ########
app = typer.Typer()


@app.command()
def generate_folders(
    semester: Annotated[str, "The semester of the course."],
    week: Annotated[str, "The week number, expecting a two-digit number."],
    notebook: Annotated[
        bool, "Whether to generate a Jupyter notebook in the week folder."
    ] = False,
):
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
    create_file_if_not_exists(
        readme_file_path, f"# Week {week}\n\nThis week's content."
    )
    if notebook:
        create_folder_if_not_exists(notebook_dir_path)
        create_file_if_not_exists(notebook_file_path, "")


if __name__ == "__main__":
    app()
