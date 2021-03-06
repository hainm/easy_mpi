Embarrassing parallel for beginner

Notes
=====

package's name might be changed.

Usage
=====

```python
# make my-script.py filename
# then run: mpirun -n 8 python my-script.py
# change '-n 8' to whatever core number

from map_mpi import pmap

# write your function with given command list
# then call

data = pmap(func, commands)
if data is not None:
    # do whatever
```

Install
=======

```bash
pip install git+https://github.com/amber-md/map_mpi
# require: numpy, mpi4py
# conda install numpy mpi4py
```

Examples
========

Write code
----------

$ cat my-script.py

```python
import subprocess
from map_mpi import pmap
import time

def func(sub_commands):
    for cm in sub_commands:
        # fake expensive calculation
        time.sleep(1.)
        subprocess.check_call(cm.split())

commands = ['echo "hello"' for _ in range(8)]
# you can also replace commands by another list of commands
# e.g.: minimize 100 snapshorts in parallel, (rst7 intput filename is inp.{1, 2, 3,...}.rst7
# commands = ['sander -i min.in -o min.{i}.out -p prmtop -c inp.{i}.rst7 -r min.{i}.rst7'.format(i=index)
#             for index in range(100)]
pmap(func, commands)
```

Run code
--------

```bash
# serial
time python my-script.py

# parallel
time mpirun -n 8 python my-script.py
```

Output
------

# serial

```bash
$ time python my-script.py 
"hello"
"hello"
"hello"
"hello"
"hello"
"hello"
"hello"
"hello"

real    0m8.268s
user    0m0.173s
sys 0m0.086s
```

# parallel

```bash
$ time mpirun -n 8 python my-script.py 
"hello"
"hello"
"hello"
"hello"
"hello"
"hello"
"hello"
"hello"

real    0m1.496s
user    0m1.431s
sys 0m0.421s
```
