"""
    MrTopo - util.iofunctor - functors for validation of user input
"""


# default validator
def vald_def(u_in):
    return True


# valid yes or no
def vald_y_n(u_in):
    if (u_in == 'y' or u_in == 'n'):
        return True
    return False
