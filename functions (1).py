def prod_non_zero_diag(x):
    X = list([[5, 0, 1], [2, 0, 2], [3, 0, 3], [4, 4, 4]])
    j = 0
    i = 0
    summ = 1
    while(i<len(X) and j<len(X[0])):
        if(X[i][j] != 0):
            summ *= X[i][j]
        i+= 1
        j+= 1
    print(summ)

    pass


def are_multisets_equal(x, y):
    x = list([1, 2, 2, 4])
    y = list([4, 2, 1, 2]) 
    x.sort()
    y.sort()
    if(len(x) != len(y)):
        print('False')
    else:
        for i in range(0, len(x)):
            if(x[i] != y[i]):
                print("False")
                break
            if(i == len(x) - 1):
                print("True")

    pass


def max_after_zero(x):
    x = list([6, 2, 0, 3, 0, 0, 5, 7, 0])
    zero = x==0
    print (x[1:][zero[:-1]].max())

    pass


def convert_image(img, coefs):
    """Sum up image channels with weights from coefs array

    input:
    img -- 3-d numpy array (H x W x 3)
    coefs -- 1-d numpy array (length 3)
    output:
    img -- 2-d numpy array

    Not vectorized implementation.
    """

    pass


def run_length_encoding(x):
    """Make run-length encoding.

    input:
    x -- 1-d numpy array
    output:
    elements, counters -- integer iterables

    Not vectorized implementation.
    """

    pass


def pairwise_distance(x, y):
    """Return pairwise object distance.

    input:
    x, y -- 2d numpy arrays
    output:
    distance array -- 2d numpy array

    Not vectorized implementation.
    """

    pass
