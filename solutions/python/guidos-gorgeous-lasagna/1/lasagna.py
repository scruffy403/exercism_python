# TODO: define the 'EXPECTED_BAKE_TIME' constant
EXPECTED_BAKE_TIME = 40
# TODO: consider defining the 'PREPARATION_TIME' constant 
#       equal to the time it takes to prepare a single layer
PREPARATION_TIME = 2


# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

# TODO: define the 'preparation_time_in_minutes()' function
#       and consider using 'PREPARATION_TIME' here
def preparation_time_in_minutes(layers):
    """
    :param layers: int number of layers being prepared.
    :return: int preparation time in minutes derived from PREPARATION_TIME layers.

    Function that takes in layers and multiplies this by PREPARATION_TIME to calculate total
    amount of time needed to prepare the layers. 
    """
    return PREPARATION_TIME * layers

# TODO: define the 'elapsed_time_in_minutes()' function
def elapsed_time_in_minutes(layers, cooking_time):
    """
    :param layers: int number of layers in the lasagna
    :param cooking_time: int the amount of time the lasagn has been cooking so far
    :return: int elapsed time derived from layers and cooking time.
    
    Function that takes the number of layers multiplied by preparation time for a layer
    and adds this product to the cooking time to calculate the elapsed time. 
    """
    return (layers * PREPARATION_TIME) + cooking_time
