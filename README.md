spinner
=======

Installation
------------
`pip install git+ssh://git@github.com/morishin/spinner.git`

Usage
-------
This module shows spinner animation during the process within `with` block
```python
from spinner import Spin

with Spin():
    while True:
        pass
```
![](http://i.gyazo.com/1cd5905920b538f1de68d20d3a3f663f.gif)

License
-------
MIT
