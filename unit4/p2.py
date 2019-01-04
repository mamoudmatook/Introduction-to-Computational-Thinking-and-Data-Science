import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
import numpy as np
def r_squared(y, estimated):
    """
    Calculate the R-squared error term.
    Args:
        y: list with length N, representing the y-coords of N sample points
        estimated: a list of values estimated by the regression model
    Returns:
        a float for the R-squared error term
    """
    # TODO
    yo=np.array(y)
    ys=np.array(estimated)
    ss=((yo-ys)**2).sum()
    mn=sum(yo)/float(len(yo))
    bb=((yo-mn)**2).sum()
    return 1-(ss/bb)


