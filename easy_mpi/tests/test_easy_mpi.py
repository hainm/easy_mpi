import time
import subprocess
from map_mpi import pmap

def test_map_mpi():
    def func(commands):
        for cm in commands:
            # fake expensive calculation
            time.sleep(1.)
            subprocess.check_call(cm.split())

    commands = ['echo "hello"' for _ in range(8)]

    pmap(func, commands)

test_map_mpi()
