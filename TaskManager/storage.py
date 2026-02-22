import json
import sys


def loadFile(file):
    try:
        with open(file, 'r') as f:
            f_dict = json.load(f)
        return f_dict
    except FileNotFoundError:
        print("The file was not found. Creating a new one.")
        return {}
    
def saveChanges(file, f_dict):
    with open(file, 'w') as f:
        json.dump(f_dict, f, indent=4)
    print("File Saved")
    return