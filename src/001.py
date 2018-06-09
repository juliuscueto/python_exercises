import numpy as np

if __name__ == "__main__":
    l = np.arange(2000, 3201)
    l_7 = np.equal(l % 7, np.zeros_like(l))
    l_5 = np.equal(l % 5, np.zeros_like(l))
    l_a = np.multiply(l_7, np.logical_not(l_5))
    print(l[l_a])
