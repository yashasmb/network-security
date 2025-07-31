import yaml
import os, sys
import numpy as np
import dill
import pickle 
from networksecurity.exception.exception import NetworksecurityException 
from networksecurity.logging.logger import logging


def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise NetworksecurityException(e, sys) from e
    
def write_yaml_file(file_path :)