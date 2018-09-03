import threading


class LockedSet(set):

    def __init__(self, *args, **kwargs):
        self._lock = threading.Lock()
        super(LockedSet, self).__init__(*args, **kwargs)

    def add(self, elem):
        with self._lock:
            super(LockedSet, self).add(elem)

    def remove(self, elem):
        with self._lock:
            super(LockedSet, self).remove(elem)

    def __contains__(self, elem):
        with self._lock:
            super(LockedSet, self).__contains__(elem)
