from Butler.Baito.BoxCutter import BoxCutter
from Butler.Baito.listener import Listener


def runningLoop() -> None:
    bc = BoxCutter()
    with bc.GetBox() as gb:
        ls = Listener()
        ls.ListenInMode(ls.GetListenerMode(), gb)
            
    runningLoop()

runningLoop()