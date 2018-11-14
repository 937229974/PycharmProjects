from apscheduler.schedulers.blocking import BlockingScheduler

from test_shudel.test1 import *
sched = BlockingScheduler()
sched.add_job(save_images, 'interval', seconds=5)
sched.start()