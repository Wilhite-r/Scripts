import json
import os
import pathlib
import sys

from Butler.Baito.GossipBox import GossipBox
from Butler.Tools.Exceptions import OpenCancellation, OpenException


DEFAULT_NAME = './BaitoBox.json'

class BoxCutter():
    def __newFilePath(path: str) -> pathlib.Path:
        if path.split('.')[-1] != 'json':
            path += ".json"
        if os.path.isfile(path):
            for permissionCheck in [
                'File already exists. Overwrite?',
                'Are you sure?',
            ]:
                nput = "_"
                print(f"{permissionCheck} (Y/N)")
                while nput not in ['Y','N']:
                    nput = input("(Y/N) >> ")
            
                if nput == 'N':
                    raise OpenCancellation('File Overwrite Declined.')
            
        #Erase File
        with open(path,'w') as f:
            f.write(json.dumps([]))
        
        return pathlib.Path(path)
        
    def __openFilePath(path: str) -> pathlib.Path:
        if os.path.isfile(path):
            if path.split('.')[-1] != 'json':
                raise OpenException("File is not json.")
            return pathlib.Path(path)
        
        raise OpenException("File does not exist. Exiting.")
        
    __getFileKeys = {
        'n': __newFilePath,
        'o': __openFilePath,
    }
    def GetBox(self) -> GossipBox:
        print("n - new file\no - open file\nx - exit\n")
        nput = "_"
        while nput not in ['x',*self.__getFileKeys.keys()]:
            nput = input("Command >> ")
        if nput == 'x':
            sys.exit()
            
        print(f"Type file name, leave blank for {DEFAULT_NAME}\ntype exit() to go back\n")
        jnput = input("FileName >> ")

        try:
            if nput == 'exit()':
                raise OpenCancellation("Filename entry exitted.")
            return GossipBox(
                self.__getFileKeys[nput](DEFAULT_NAME if not jnput else jnput)
                )
        except OpenException as e:
            print("Could not perform file execution: " + e.problem)
            return self.GetBox()
        except OpenCancellation as e:
            print("Open Cancelled: " + e.statement)
            return self.GetBox()

