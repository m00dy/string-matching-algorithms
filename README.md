# string-matching-algorithms
Popular string matching algorithms &amp; comparison &amp; charts


This repository is all about string searching algorithms.

Algorithms have been tested so far are, **BOM**, **BruteForce**, **Horspool**, **BNDM**.

Algorithms implementations are taken from http://www-igm.univ-mlv.fr/~lecroq/string/

Testing data is taken from http://www.ncbi.nlm.nih.gov/genome

![alt tag](https://raw.github.com/m00dy/string-matching-algorithms/master/string_search_algorithms.png)
Y axis represents time in seconds.
X axis represents input size which is basically a python string


Build
--------------

**Building test data.**


```
bash /data/data_builder.bash
```

This will download around 2gb genome files and merge them to one file.

**Building searching algorithms**


```
bash build
```

will try to compile matching algorithms as shared library.


Run the tests
--------------


```
python run_and_test.py
```


This will generate random input set and run each algorithm according to random input. 
Plot.ly integration is required to draw the plot afterward.

