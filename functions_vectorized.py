import numpy as np


def prod_non_zero_diag(x):
    X = np.array([[5, 0, 1], [2, 0, 2], [3, 0, 3], [4, 4, 4]])
    np.prod(np.diag(X)[np.diag(X)!=0])

    pass


def are_multisets_equal(x, y):
    x = np.array([1,2,2,4])
    x = np.sort(x, axis=0)
    y = np.array([4, 2, 1, 2])
    y = np.sort(y, axis=0)
    print (np.array_equal(x,y))
    
    pass


def max_after_zero(x):
    x = np.random.randint (20, size=(1000000))
    print(np.max(x[1:][(x==0)[:-1]]))

    pass


def convert_image(img, coefs):
    """Sum up image channels with weights from coefs array

    input:
    img -- 3-d numpy array (H x W x 3)
    coefs -- 1-d numpy array (length 3)
    output:
    img -- 2-d numpy array

    Vectorized implementation.
    """

    pass


def run_length_encoding(x):
    """Make run-length encoding.

    input:
    x -- 1-d numpy array
    output:
    elements, counters -- integer iterables

    Vectorized implementation.
    """

    pass


def pairwise_distance(x, y):
    """Return pairwise object distance.

    input:
    x, y -- 2d numpy arrays
    output:
    distance array -- 2d numpy array

    Vctorized implementation.
    """

    pass
