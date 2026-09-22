import numpy as np
import math
def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # Write code here
    return np.divide(1, 1  + np.exp(np.multiply(-1, x)))