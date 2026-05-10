"""
Dictionaries, Maps, and Hashtables

collections.OrderedDict
Remembers the insertion order of keys added to it. Standard `dict()` also remembers order but only for Python >= 3.6
"""

from collections import OrderedDict

od = OrderedDict(one=1, two=2, three=3)
od.keys()

# collections.defaultdict
#
# Syntax: `defaultdict(default_factory)`
#
# Uses factory function as a default value instead of throwing `KeyError`

from collections import defaultdict

def def_value():
    return "zero"

function_default_dict = defaultdict(def_value)
function_default_dict["test"]

lambda_default_dict = defaultdict(lambda: "minus")
lambda_default_dict["test"]

int_default_dict = defaultdict(int)
int_default_dict["test"]

# collections.ChainMap
# Groups multiple dictionaries. Allows searching through all of them at the same time.

from collections import ChainMap

dict1 = {'one': 1, 'two': 2}
dict2 = {'three': 3, 'four': 4}
chain = ChainMap(dict1, dict2)

chain['three']

# types.MappingProxyType
# Provides read-only view of standard dictionary without copying it.

from types import MappingProxyType

writable = {'one': 1, 'two': 2}
read_only = MappingProxyType(writable)
print(read_only['one'])
read_only['one'] = 23
