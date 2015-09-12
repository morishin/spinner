# spinner

## Install
`pip install git+ssh://git@github.com/morishin/spinner.git`

## Usage
This module shows spinner animation during the process within `with` block

```python
from spinner import Spin

with Spin():
    while True:
        pass
```

![](https://i.gyazo.com/7e82d3638f2ad65a2b745a5ec4e4436f.gif)

## Option
```python
from spinner import Spin, SpinnerType

with Spin(type=SpinnerType.shobon):
    while True:
        pass
```

![](https://i.gyazo.com/6aeaab5b3d3e729da143852498c84057.gif)

KAWAII!!!!!!!!

## License
MIT
