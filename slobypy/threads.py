from threading import Thread
from queue import Queue


class QueuedThread(Thread):
    def __init__(self, queue: Queue, metadata: dict, group=None, target=None, name=None,
                 *args, **kwargs):
        Thread.__init__(self, group, target, name, *args, **kwargs)
        self._return = None
        self.metadata = metadata
        self.queue = queue

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,
                                        **self._kwargs)
            self.metadata["data"] = self._return
            self.queue.put(self.metadata)

    def join(self):
        Thread.join(self)
        return self.metadata
