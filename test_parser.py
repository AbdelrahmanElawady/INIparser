import iniparser
from iniparser import parse, is_section, is_key, is_skippable, get_section, get_key_value, get_key_name

data = parse("a.ini")
print(data)

assert data['owner']['name'] == 'John Doe'
assert data['owner']['organization'] == 'Acme Widgets Inc.'
assert data['database']['server'] == '192.0.2.62'
assert len(data) == 2
assert len(data['owner']) == 2
assert len(data['database']) == 3

assert is_section("[ab]") == True
assert is_section("[]") == True
assert is_section("[ab") == False

assert is_skippable("") == True
assert is_skippable(";this is a comment") == True
assert is_skippable("[owner]") == False

assert is_key("name=v=a=l=u=e") == True
assert is_key("name=value") == True
assert is_key("namevalue") == False

assert get_section("[title]") == "title"
assert get_section("[a[b]]") == "a[b]"
assert get_section("[]") == ""

assert get_key_name("name=value") == "name"
assert get_key_name("name=v=a=l=u=e") == "name"
assert get_key_name("na=m=e=value") == "na"
assert get_key_name("=value") == ""

assert get_key_value("name=value") == "value"
assert get_key_value("name=v=a=l=u=e") == "v=a=l=u=e"
assert get_key_value("na=m=e=value") == "m=e=value"
assert get_key_value("name=") == ""