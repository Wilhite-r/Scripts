from collections import defaultdict
import json
import pathlib
from Butler.Baito.KeyList import KeyList

from Butler.Baito.KeyListWorker import KeyListWorker


class GossipBox(object):
    path = pathlib.Path()
    
    def resetKeyLists() -> dict:
        return {}
    
    bookOfKeyLists = resetKeyLists()
    
    def __init__(self, path: pathlib.Path) -> None:
        self.path = path
        
    def __enter__(self):
        with open(self.path, 'r') as f:
            data_box = json.loads(f.read())
            if not isinstance(data_box, list):
                raise Exception("File formatted improperly. Contents should be in list form.")
                
            for data in data_box:
                keylist = KeyListWorker.WrangleKeyList(data)
                self.bookOfKeyLists = KeyListWorker.PlaceKeyListsInBooks(
                    keylist.key,
                    self.bookOfKeyLists,
                    keylist
                    )
        return self
    
    def __insertKeys(keys: list[str]) -> None:
        for key in keys:
            self.bookOfKeyLists = KeyListWorker.PlaceKeyListsInBooks(
                key,
                self.bookOfKeyLists,
                None
            )
        
        if len(keys) == 1:
            print(keys[0] + " added as a key.")
        else:
            print(f"[{', '.join(keys)}] added as keys.")
        
    def __removeKeys(keys: list[str]) -> None:
        for key in keys:
            self.bookOfKeyLists = KeyListWorker.PlaceKeyListsInBooks(
                key,
                self.bookOfKeyLists,
                None
            )
        
        if len(keys) == 1:
            print(keys[0] + " added as a key.")
        else:
            print(f"[{', '.join(keys)}] added as keys.")
        
    def __addAliases(key: str, aliases: List[str]) -> None:
        
    def __removeAliases(key: str, aliases: List[str]) -> None:
    
    __getFileKeys = {
        'i': __insertKeys,
        'r': __removeKeys,
        'a': __addAliases,
        'ra': __removeAliases,
    }
    def ListenForKeys(self) -> None:
        print("Dump list of keys here. Submit 'exit()' to leave.\n")
        print(f'Current Keys: ["{",".join(self.bookOfKeyLists.keys())}"]')
        print(f'"i key0 key1 key2 . . ." to insert keys')
        print(f'"r key0 key1 key2 . . ." to remove keys')
        print(f'"a key alias1 alias2 . . ." to add aliases')
        print(f'"ra key alias1 alias2 . . ." to remove aliases')
        print(f'"exit()." to exit input')
        nput = input("Dump Key Here >> ")
        while nput != "exit()":
            nput = nput.strip().lower().split(' ')
            if nput[0] in self.__getFileKeys.keys():
                self.__getFileKeys(nput[1:])
            else:
                print("//\!ComMAnd NoT RecoGNized!/! ER50R")
            print(f'Current Keys: ["{",".join(self.bookOfKeyLists.keys())}"]')
            nput = input("Dump Key Here >> ")
        return
    
    
    def ParseGossipForFamiliarity(self, gossipHeard: str, gossipList: defaultdict) -> defaultdict:
        #This function could use some work
        discretizedGossip = gossipHeard.split(' ')
        i = 0
        while i < len(discretizedGossip):
            if discretizedGossip[i] in self.bookOfKeyLists:
                shelfOfKnowledge = self.bookOfKeyLists[discretizedGossip[i]]
                familiarGossip = discretizedGossip[i]
                while i + 1 < len(discretizedGossip) and discretizedGossip[i+1] in shelfOfKnowledge:
                    i += 1
                    shelfOfKnowledge = shelfOfKnowledge[discretizedGossip[i]]
                    familiarGossip += " " + discretizedGossip[i]
                    
                if familiarGossip:
                    gossipList[familiarGossip] += 1
                    
            i += 1
        
        return gossipList
            
    
    def ListenForText(self) -> None:
        print("Dump text here and I'll match it to my book collection. Submit 'exit()' to leave.\n")
        nput = "_"
        while nput != "exit()":
            nput = input("Dump Text Here >> ")
            recognizedGossip = self.ParseGossipForFamiliarity(
                nput.strip().lower(), 
                defaultdict(lambda: 0)
            )
            self.bookOfKeyLists = KeyListWorker.UpdateArchivesWithGossip(
                recognizedGossip,
                self.bookOfKeyLists
            )
            self.WriteBookToFile()
            print("Updated my archives with this new knowledge!")
        return

    def close(self):
        pass
    
    def ListifyBook(book: dict) -> list[KeyList]:
        listOfKeyLists = []
        if ' ' in book and book[' ']:
            listOfKeyLists.append(
                KeyListWorker.PackageKeyList(book[' '])
            )
        for bookey, bookValue in book.items():
            if bookey != ' ':
                listOfKeyLists += GossipBox.ListifyBook(bookValue)
        return listOfKeyLists
    
    def WriteBookToFile(self):
        with open(self.path, 'w') as f:
            f.write(json.dumps(GossipBox.ListifyBook(self.bookOfKeyLists)))
    
    def __exit__(self, *args):
        self.WriteBookToFile()
        self.bookOfKeyLists = GossipBox.resetKeyLists()

