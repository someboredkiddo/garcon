from garcon import activity
from garcon import decider
from threading import Thread
import boto.swf.layer2 as swf
import time

import test_flow
print('start')
swf.WorkflowType(
    name=test_flow.name, domain=test_flow.domain,
    version='1.0', task_list=test_flow.name).start()
