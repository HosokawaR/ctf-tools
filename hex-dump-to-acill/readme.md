# hex dump to acill

This script convert hex dump texts to acill.  
Note this script read hex dump as little endian. 

## Usage

```bash
$ python3 decode-hex-to-acill <HEX CODE FROM MEMORY DUMP>
```

## Example

When you try Format String Attack, this script may be usefull.

```bash
Enter Token > %x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x  # Format String Attack
Your Token is: 110f7f89dc709c96180299c973509c7b46544347414c462973707d34356562fff4007df7fc4af8f75f93742  # Stack Dump
```

To get flag from above hex values, you can use this script like this.  
Note `_` stand for unvisble char or `_`...

```bash
python3 decode-hex-to-acill.py 110f7f89dc709c96180299c973509c7b46544347414c462973707d34356562fff4007df7fc4af8f75f93742
Shift width: 0
______p_____{_PsGCTF)FLA4}ps_be5_}____J__t__

Shift width: 1
____a_____)____5t4De_b__C__7_/VV___@u___B7_

Shift width: 2
_____a__5__)e____t4D7_b_VC__@_/V_____u__B7

Shift width: 3
_p_______Ps_CTF{FLAG}ps)be54}____J__t____     # CTF{FLAG} may be flag.

Shift width: 4
___ps___F{_PAGCTs)FL54}p__be__}____J_t_

Shift width: 5
_)_a__5_4De_b__t__7_/VVC__@_____B7_u

Shift width: 6
_5__De____t4_7_bVVC__@_/____7_u_B

Shift width: 7
TF{_LAGCps)Fe54}___bJ__}_____t
```
