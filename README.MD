INIparser
=========
INIparser is a python tool for dealing with INI files.

Usage
=====
```python
import iniparser.py
iniparser.parse("file.ini") # returns a dict of the data in file.ini
```
file.ini content:
-----------------
```ini
; last modified 1 April 2001 by John Doe
[owner]
name=John Doe   
organization=Acme Widgets Inc.   

[database]
; use IP address in case network name resolution is not working
server=192.0.2.62  
port=143  
file="payronll.dat"
```
output:
-------
```json
{
   "owner":{
      "name":"John Doe   ",
      "organization":"Acme Widgets Inc.   "
   },
   "database":{
      "server":"192.0.2.62  ",
      "port":"143  ",
      "file":"\"payronll.dat\"  "
   }
}
```
Specifications
=====
* Comments only start with ';'.
* Usage of the same key name will overwrite previous value.
* Doesn't strip whitespaces from key lines.
* Doesn't support global keys.
* Doesn't support section nesting.