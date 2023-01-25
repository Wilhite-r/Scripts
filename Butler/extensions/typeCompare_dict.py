class typeCompareDict(dict):
    """Type Compare
    Type compare in the down direction. This means the data must have all the fields of the compared type
    All Extra fields will be dropped.
    """
    def compareTypeDown(self, compare: type) -> bool:
        for key, value in compare.__dict__.items():
            if key not in self.keys() or not isinstance(value, type(getattr(compare, key))):
                    raise (f'The following field is missing or an invalid type: ({key}, {type(self[key])})\n'
                           "Object at fault: \n" + "\n".join([f"({k},{v})" for k, v in self.items()])
                           )
        
    