import heapq
from Butler.extensions.typeCompare_dict import typeCompareDict

from Butler.Baito.KeyList import KeyList

class KeyListWorker():
    def WrangleKeyList(data: dict) -> KeyList:
        try:
            KeyList.CompareDictMinimum(data)
        except Exception as e:
            raise Exception('Object in list not in proper form:'
                            + e.args)
        
        return KeyList(**data)
    
    def combine(protagonist: KeyList, antagonist: KeyList) -> KeyList:
        if protagonist is None:
            return antagonist
        if antagonist is None:
            return protagonist
        
        if protagonist.key != antagonist.key:
            raise Exception("Cannot combine Keylists with different keys")
        
        supertagonist = KeyList(
            key=protagonist.key,
            occurances=protagonist.occurances + antagonist.occurances,
            occurancesTotal=protagonist.occurancesTotal + antagonist.occurancesTotal,
            colleagues=protagonist, 
            aliases=protagonist.aliases | antagonist.aliases
            )
        for colleaguesKey in antagonist.colleagues.keys():
            supertagonist.colleagues[colleaguesKey] += 1
        
        # currently not calculating top colleagues in-state
        return supertagonist
    
    def PlaceKeyListsInBooks(key: str, book: dict, data: KeyList) -> dict:
        book[key] = KeyListWorker.combine(data, book[key]) \
            if key in book else data
        return book
    
    def UpdateArchivesWithGossip(gossip: dict[str, int], archive: dict) -> dict:
        for gossipKey in gossip.keys():
            data = KeyList(
                key=gossipKey,
                occurances=1,
                occurancesTotal=gossip[gossipKey],
                colleagues={key: gossip[key] for key in gossip.keys() if key != gossipKey},
            )
            archive = KeyListWorker.PlaceKeyListsInBooks(gossipKey, archive, data)
        return archive
        
    def PackageKeyList(thneed: KeyList) -> dict:
        thwant = {}
        
        thwant['key'] = thneed.key
        thwant['occurances'] = thneed.occurances
        thwant['occurancesTotal'] = thneed.occurancesTotal
        thwant['colleagues'] = thneed.colleagues
        
        # Get top colleagues
        sortedColleagues = []
        for ockey, ocval in thneed.colleagues.items():
            heapq.heappush(sortedColleagues, (ocval, ockey))
        thwant['top_colleagues'] = heapq.nlargest(3, sortedColleagues)
        
        thwant['aliases'] = thneed.aliases
        
        return thwant
        
        
