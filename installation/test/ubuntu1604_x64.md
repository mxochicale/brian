
# Sun 10 Mar 17:27:30 GMT 2019


```

$ python
Python 3.7.1 | packaged by conda-forge | (default, Feb 26 2019, 04:48:14) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import brian2
>>> brian2.test()




Running tests in /home/tree/anaconda2/envs/brain/lib/python3.7/site-packages/brian2 for targets numpy, cython (excluding long tests)
Testing codegen-independent code 
Testing with multiple processes for numpy, codegen_independent, cython
Resetting to default preferences

Running tests that do not use code generation
..........S................S..............WARNING    Integrating equations with GSL is still considered experimental [brian2.stateupdaters.GSL]
....................WARNING    The expression "i1 / 1" divides two integer values. In previous versions of Brian, this would have used either an integer ("flooring") or a floating point division, depending on the Python version and the code generation target. In the current version, it always uses a floating point division. Explicitly ask for an  integer division ("//"), or turn one of the operands into a floating point value (e.g. replace "1/2" by "1.0/2") to no longer receive this warning. [brian2.parsing.bast.floating_point_division]
......................S............................................................................................WARNING    The SpikeGeneratorGroup contains spike times earlier than the start time of the current run (t = 5. ms), these spikes will be ignored. [brian2.input.spikegeneratorgroup.ignored_spikes]
............WARNING    The expression "(i + 1) / N" divides two integer values. In previous versions of Brian, this would have used either an integer ("flooring") or a floating point division, depending on the Python version and the code generation target. In the current version, it always uses a floating point division. Explicitly ask for an  integer division ("//"), or turn one of the operands into a floating point value (e.g. replace "1/2" by "1.0/2") to no longer receive this warning. [brian2.parsing.bast.floating_point_division]
........................................SS................................................WARNING    The 'independent' state updater is deprecated and might be removed in future versions of Brian. [brian2.stateupdaters.exact.deprecated_independent]
..........................................................................
----------------------------------------------------------------------
Ran 351 tests in 44.221s

OK (SKIP=5)
Running tests for target numpy:
SWARNING    Integrating equations with GSL is still considered experimental [brian2.stateupdaters.GSL]
WARNING    Integrating equations with GSL is still considered experimental [brian2.stateupdaters.GSL]
WARNING    Integrating equations with GSL is still considered experimental [brian2.stateupdaters.GSL]
SWARNING    Integrating equations with GSL is still considered experimental [brian2.stateupdaters.GSL]
SWARNING    Integrating equations with GSL is still considered experimental [brian2.stateupdaters.GSL]
SWARNING    Integrating equations with GSL is still considered experimental [brian2.stateupdaters.GSL]
SWARNING    Integrating equations with GSL is still considered experimental [brian2.stateupdaters.GSL]
SWARNING    Integrating equations with GSL is still considered experimental [brian2.stateupdaters.GSL]
SWARNING    Integrating equations with GSL is still considered experimental [brian2.stateupdaters.GSL]
SWARNING    Integrating equations with GSL is still considered experimental [brian2.stateupdaters.GSL]
SSWARNING    Integrating equations with GSL is still considered experimental [brian2.stateupdaters.GSL]
SWARNING    Integrating equations with GSL is still considered experimental [brian2.stateupdaters.GSL]
.SWARNING    Integrating equations with GSL is still considered experimental [brian2.stateupdaters.GSL]
WARNING    Integrating equations with GSL is still considered experimental [brian2.stateupdaters.GSL]
SWARNING    Integrating equations with GSL is still considered experimental [brian2.stateupdaters.GSL]
SSWARNING    Integrating equations with GSL is still considered experimental [brian2.stateupdaters.GSL]
WARNING    Integrating equations with GSL is still considered experimental [brian2.stateupdaters.GSL]
WARNING    Integrating equations with GSL is still considered experimental [brian2.stateupdaters.GSL]
SSWARNING    Integrating equations with GSL is still considered experimental [brian2.stateupdaters.GSL]
S.SSS.........SS.S...................................................................S..................................WARNING    The 'independent' state updater is deprecated and might be removed in future versions of Brian. [brian2.stateupdaters.exact.deprecated_independent]
..................................................................................................
----------------------------------------------------------------------
Ran 235 tests in 151.194s

OK (SKIP=25)
Running tests for target cython:
SWARNING    Integrating equations with GSL is still considered experimental [brian2.stateupdaters.GSL]
WARNING    Integrating equations with GSL is still considered experimental [brian2.stateupdaters.GSL]
.WARNING    Integrating equations with GSL is still considered experimental [brian2.stateupdaters.GSL]
.WARNING    Integrating equations with GSL is still considered experimental [brian2.stateupdaters.GSL]
.WARNING    Integrating equations with GSL is still considered experimental [brian2.stateupdaters.GSL]
.WARNING    Integrating equations with GSL is still considered experimental [brian2.stateupdaters.GSL]
.WARNING    Integrating equations with GSL is still considered experimental [brian2.stateupdaters.GSL]
.WARNING    Integrating equations with GSL is still considered experimental [brian2.stateupdaters.GSL]
.WARNING    Integrating equations with GSL is still considered experimental [brian2.stateupdaters.GSL]
.WARNING    Integrating equations with GSL is still considered experimental [brian2.stateupdaters.GSL]
WARNING    Integrating equations with GSL is still considered experimental [brian2.stateupdaters.GSL]
WARNING    Integrating equations with GSL is still considered experimental [brian2.stateupdaters.GSL]
.WARNING    Integrating equations with GSL is still considered experimental [brian2.stateupdaters.GSL]
...WARNING    Integrating equations with GSL is still considered experimental [brian2.stateupdaters.GSL]
WARNING    Integrating equations with GSL is still considered experimental [brian2.stateupdaters.GSL]
WARNING    Integrating equations with GSL is still considered experimental [brian2.stateupdaters.GSL]
...WARNING    Integrating equations with GSL is still considered experimental [brian2.stateupdaters.GSL]
WARNING    Integrating equations with GSL is still considered experimental [brian2.stateupdaters.GSL]
..SS..WARNING    Integrating equations with GSL is still considered experimental [brian2.stateupdaters.GSL]
......S.SSS.S..S..^[[6~....S.............................................S.........SS......................................WARNING    The 'independent' state updater is deprecated and might be removed in future versions of Brian. [brian2.stateupdaters.exact.deprecated_independent]
...........................................................................SS...................
----------------------------------------------------------------------
Ran 235 tests in 778.728s

OK (SKIP=15)
OK: 3/3 test suite(s) did complete successfully.
True


```



