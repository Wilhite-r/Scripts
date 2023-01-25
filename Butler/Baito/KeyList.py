from collections import defaultdict


class KeyList(object):
    key: str
    occurances: int
    occurancesTotal: int #TODO add occurance functionality
    colleagues: defaultdict(lambda: 0)
    aliases: set[str] #TODO add alias functionality
    # top_occurances: list[(int, list[str])]
    
    def __init__(
        self, 
        key: str, 
        occurances: int, 
        occurancesTotal: int,
        colleagues: dict = {}, 
        aliases: set[str] = ()
    ):
        self.key = key
        self.occurances = occurances
        self.occurancesTotal = occurancesTotal
        self.colleagues = defaultdict(lambda: 0, colleagues)
        self.aliases = aliases
        # currently not calculating top occurances in-state
        
    @classmethod
    def CompareDictMinimum(cls, compare: dict) -> None:
        for key, keyType in [(cls.key, type(cls.key)), (cls.occurances, type(cls.occurances))]:
            if key not in compare.keys() or not isinstance(compare[key], keyType):
                    raise(f'The following field is missing or an invalid type: ({key}, {keyType})\n'
                           "Object at fault: \n" + "\n".join([f"({k},{v})" for k, v in self.items()])
                    )
        