import iniparser
from iniparser import parse, isSection, isKey, isSkippable, getKeyValue, getKeyName, getSection

data = parse("a.ini")
print(data)

assert data['owner']['name'] == 'John Doe'
assert data['owner']['organization'] == 'Acme Widgets Inc.'
assert data['database']['server'] == '192.0.2.62'
assert len(data) == 2
assert len(data['owner']) == 2
assert len(data['database']) == 3

assert isSection("[ab]") == True
assert isSection("[]") == True
assert isSection("[ab") == False

assert isSkippable("") == True
assert isSkippable(";this is a comment") == True
assert isSkippable("[owner]") == False

assert isKey("name=v=a=l=u=e") == True
assert isKey("name=value") == True
assert isKey("namevalue") == False

assert getSection("[title]") == "title"
assert getSection("[a[b]]") == "a[b]"
assert getSection("[]") == ""

assert getKeyName("name=value") == "name"
assert getKeyName("name=v=a=l=u=e") == "name"
assert getKeyName("na=m=e=value") == "na"
assert getKeyName("=value") == ""

assert getKeyValue("name=value") == "value"
assert getKeyValue("name=v=a=l=u=e") == "v=a=l=u=e"
assert getKeyValue("na=m=e=value") == "m=e=value"
assert getKeyValue("name=") == ""