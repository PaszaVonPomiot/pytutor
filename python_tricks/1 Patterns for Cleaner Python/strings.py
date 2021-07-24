name = "Bob"

# Old style strings
"Hello, %s" % name

# New style strings
"Hello, {}".format(name)

# f-strings
f"Hello, {name}!"

# Template Strings
from string import Template

t = Template("Hey, $name!")
t.substitute(name=name)
