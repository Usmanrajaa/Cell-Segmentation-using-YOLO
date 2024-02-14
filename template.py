import os
from pathlib import Path
import logging

# Setting up basic configuration for logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(message)s:')

project_name = "cellSegmentation"

# List of file paths you want to create
list_of_files = [
    ".github/workflows/.gitkeep",
    "data/.gitkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/constants/training_pipeline/__init__.py",
    f"{project_name}/constants/application.py",
    f"{project_name}/entity/config_entity/__init__.py",
    f"{project_name}/entity/artifact_entity/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "research/trials.ipynb",
    "template/index.html",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
]

# Creating directories and files based on the list above
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    # If the directory path is not empty, create directories
    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")
    
    # If the file does not exist or is empty, create it
    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, "w") as f:
            pass  # Just creating an empty file
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")
