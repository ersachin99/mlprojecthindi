from fileinput import filename
import os
from pathlib import Path
import logging

# loging configuration

logging.basicConfig(level=logging.INFO)

# name of project
project_name='mlproject'

# files

list_of_file=[
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/components/data_ingestion',
    f'src/{project_name}/components/data_transformation.py',
    f'src/{project_name}/components/model_transer.py',
    f'src/{project_name}/components/model_monitering.py',
    f'src/{project_name}/pipelines/__init__.py',
    f'src/{project_name}/pipelines/training_pipeline.py',
    f'src/{project_name}/pipelines/prediction_pipeline.py',
    f'src/{project_name}/exception.py',
    f'src/{project_name}/logger.py',
    f'src/{project_name}/utils.py',
    'app.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py',
    'main.py'

]

# code for run the script

for filepath in list_of_file:
    filepath=Path(filepath)
    filedir, filename= os.path.split(filepath)


    if filedir !='':
        os.makedirs(filedir,exist_ok=True)
        logging.info(f'Creating Directory :{filedir} for the file {filename} ')


    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f'Creating Empty file :{filepath} ')


    else:
        logging.info(f'{filename} is already exists')

