# OiAK-LNS
Project for WUST course OiAK. Tried to implement solution of article "Half-Precision Logarithmic Arithmetic Unit Based on the Fused Logarithmic and Antilogarithmic Converter".
https://ieeexplore.ieee.org/document/9667268

# Status 
The current state of project is implementation of of basic Half-Precision (FP16) converter, and Logarithmic Number System (LNS) converter for representing given floating point number.
LNS implementation is using at the moment only Logarithmic converter, thus no antilogarithmic implementation can slower down current calculation process.

# Usage
Currently it is possible to use it as CLI tool with given params:

```
usage: main.py [-h] a {mul,div,sr,isr} b

IEEE754 and LNS arithmetic

positional arguments:
  a                 First number
  {mul,div,sr,isr}  Operation
  b                 Second number

options:
  -h, --help        show this help message and exit
```
