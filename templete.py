import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name="textSummarizer"

list_of_files = [
    ".github/workflow/.gitkeep",# This is a dummy file to keep the folder structure
    f"src/{project_name}/__init__.py",# This is a dummy file to keep the folder structure 
    f"src/{project_name}/components/__init__.py",# This is a dummy file to keep the folder structure
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/entity/__init__.py", 
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
    
]


for filepath in list_of_files:
    filepath=Path(filepath) #Path Function Is Automated Path With Your Operating System , Like In Windows It Will Be Like C:\Users\Username\Desktop\Project
    filedirc, filename=os.path.split(filepath) #os.path.split Function Split The Path Into Directory And File Name
    if filedirc !="":
        os.makedirs(filedirc, exist_ok=True) #os.mkdir Function Create Directory If Not Exist
        logging.info(f"Creating Directory {filedirc} for the file {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0): #os.path.exists Function Check If File Exist And os.path.getsize Function Check The Size Of File
        with open(filepath, "w") as f:  #open Function Open The File In Write Mode
            pass
            logging.info(f"Creating File {filename} at {filepath}")
    else:
        logging.info(f"{filename} is already exists at {filepath}")