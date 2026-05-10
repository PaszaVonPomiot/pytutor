"""
Information hiding
- data hiding is isolating the client from a part of program implementation
- process of hiding the details of an object or function
- hiding of these details results in an abstraction
- information hiding effectively decouples the calling code from the internal workings of the object or function being called, which makes it possible to change the hidden portions without having to also change the calling code
- some objects in the module are kept internal, invisible, and inaccessible to the user
- encapsulation is a common technique programmers use to implement information hiding
- class data members can be hidden by using double underscore prefix - `__hidden_data`
"""

class VisibleTemp:
    temp = 25
    __temp = 35

visible_temp = VisibleTemp()
print(visible_temp.temp)
print(visible_temp._VisibleTemp__temp)  # name mangling prevents direct access to t.__temp

class HiddenTemp:
    temp = 25
    __temp = 35

hidden_temp = HiddenTemp()
print(hidden_temp.__temp)  # this data is hidden
