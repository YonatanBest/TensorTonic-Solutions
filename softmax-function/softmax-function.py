import numpy as np

def softmax(x: list) -> np.ndarray:
    """
    Returns stable softmax probabilities as a NumPy array matching the shape of x.
    """
    # Write code here
    upper = np.exp(x)
    if upper.ndim == 2:
        base = np.sum(upper, axis=1)
        res = upper / base[:, np.newaxis]
    else:
        base = np.sum(upper)
        res = np.divide(upper, base)
    return np.where(np.isnan(res), 1, res)