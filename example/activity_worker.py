from garcon import activity
from garcon import decider
from threading import Thread
import boto.swf.layer2 as swf
import time

import logging
import test_flow

logging.basicConfig(level=logging.INFO)

activity.ActivityWorker(test_flow).run()
