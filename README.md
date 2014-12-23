spinner
=======

Installation
------------
1. `git clone https://github.com/morishin/spinner.git`
2. `cd spinner`
3. `pip install .`

Usage
-------
This module shows spinner animation during the process within `with` block
```python
import time
from spinner import Spin

print('Showing spinner animation for 3 seconds...')
with Spin():
    time.sleep(3)
```
![](http://i.gyazo.com/1cd5905920b538f1de68d20d3a3f663f.gif)

License
-------
MIT