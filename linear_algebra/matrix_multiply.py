# Matrix multiplication using NumPy
import numpy as np

def mat_mult(a: np.ndarray, b: np.ndarray):
    if a.shape[1] != b.shape[0]:
        raise ValueError("Dimension mismatch for matrix multiplication")
    return a @ b

if __name__ == "__main__":
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    C = mat_mult(A, B)
    print("Matrix A x B =")
    print(C)
