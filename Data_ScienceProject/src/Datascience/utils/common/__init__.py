import os 
import yaml 
from src.Datascience import logger
import json 
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    """
    read yaml file and return 

    Args:
    path_to_yaml (Path): path like input 
    Raises:
    ValueError : if yaml format not intialized 
    e:empty file 

    Returns:
    ConfigBox:ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError(f"yaml file: {path_to_yaml} is empty or not intialized")
    except Exception as e:
        raise e
        
    
@ensure_annotations
def save_json(path_to_json:Path,data:dict):
    """
    save json file
    Args:
    path_to_json (Path): path like input 
    data (dict): json data 
    """
    os.makedirs(path_to_json,exist_ok=True)
    with open(path_to_json,"w") as json_file:
        json.dump(data,json_file,indent=4)
        logger.info(f"json file: {path_to_json} saved successfully")    


@ensure_annotations
def load_json(path_to_json:Path)->ConfigBox:
    """
    load json file
    Args:
    path_to_json (Path): path like input 
    Returns:
    ConfigBox:ConfigBox type
    """    
    with open(path_to_json) as json_file:
        content=json.load(json_file)
        logger.info(f"json file: {path_to_json} loaded successfully")
        return ConfigBox(content)

@ensure_annotations
def save_bin(path_to_bin:Path,data:Any):
    """
    save bin file
    Args:
    path_to_bin (Path): path like input 
    data (Any): bin data 
    """    
    os.makedirs(path_to_bin,exist_ok=True)
    with open(path_to_bin,"wb") as bin_file:
        joblib.dump(data,bin_file)
        logger.info(f"bin file: {path_to_bin} saved successfully")   


@ensure_annotations
def load_bin(path_to_bin:Path)->ConfigBox:
    """
    load bin file
    Args:
    path_to_bin (Path): path like input 
    Returns:
    ConfigBox:ConfigBox type
    """    
    with open(path_to_bin,"rb") as bin_file:
        content=joblib.load(bin_file)
        logger.info(f"bin file: {path_to_bin} loaded successfully")
        return ConfigBox(content)