import pandas as pd 
from download import download
import json

class Load_json :
    def __init__(self,url_totem,target_name):
        download(url_totem,target_name,replace=True)
    @staticmethod
    def save_as_df(path_target):
        totem = pd.read_json(target_name)
        return totem