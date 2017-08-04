from garcon import activity
from garcon import decider
from threading import Thread
import boto.swf.layer2 as swf
import time

import test_flow

deciderworker = decider.DeciderWorker(test_flow)

while(True):
    deciderworker.run()
    time.sleep(1)
