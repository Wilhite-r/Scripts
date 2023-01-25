from typing import Callable
from Butler.Baito.GossipBox import GossipBox


class Listener():
    def __listenForKeys(gb: GossipBox) -> int:
        gb.ListenForKeys()
        return 0

    def __listenForText(gb: GossipBox) -> int:
        gb.ListenForText()
        return 0
            
    def LeaveBox(gb: GossipBox) -> int:
        gb.close()
        return 1
            
    __getListenerModeKeys = {
        'a': __listenForKeys,
        'd': __listenForText,
        'x': LeaveBox,
    }
    def GetListenerMode(self) -> Callable[[GossipBox], int]:
        print("a -> add keys\nd -> drop text\nx -> exit\n")
        nput = "_"
        while nput not in ['x', *self.__getListenerModeKeys.keys()]:
            nput = input("Command >> ")
            
        return self.__getListenerModeKeys[nput]
            
    def ListenInMode(self, listenFunc: Callable[[GossipBox], int], roomMic: GossipBox) -> None:
        if listenFunc(roomMic) == 1:
            return
        self.ListenInMode(self.GetListenerMode(), roomMic)

