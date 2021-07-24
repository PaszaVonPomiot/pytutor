# Cohesion and coupling are good software metrics
# Tight cohesion and loose coupling indicates high software quality

# cohesion refers to the degree to which the elements inside a module belong together
# The SRP (Single Responsiblity Principle) will lead to cohesive module
# Cohesion refers to how closely all the routines in a class or all the code in a routine support a central purpose. 
# Classes that contain strongly related functionality are described as having strong cohesion

def do_things(a, b, c):
    """Loose cohesion - function tries to do many things"""
    s = a + b
    status = 1
    display_something(s)
    print(s)


# solution
def sum_things(a, b):
    """Tight cohesion - function tries to do one thing only"""
    s = a + b



# coupling is the degree of interdependence between software modules
# a measure of how closely connected two routines or modules are
# the strength of the relationships between modules
def check_email(email):
    ''' Tight coupling - function accesses data that is deep in the object structure; problematic when email object changes structure '''
    if email.header.bearer.invalid():
        raise Exception
    if email.header.received:
        raise Exception

# solution 1 - pass only the data that function needs
def check_email2(is_invalid, received):
    ''' data directly as parameters '''
    if is_invalid:s
        raise Exception
    if received:
        raise Exception

# solution 2 - move this function to email object
class Email:
    def check_email(self, ...)
        if self.header.received:
            raise Exception
