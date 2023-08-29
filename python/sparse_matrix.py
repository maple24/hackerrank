from typing import List, Dict, Tuple


class SparseMatrix:
    def __init__(self, shape: Tuple[int, int], data: Dict[Tuple[int, int], int]):
        self.rows, self.cols = shape
        self.elements: Dict[Tuple[int, int], int] = data

    def set(self, row: int, col: int, value: int) -> None:
        if row < self.rows and col < self.cols:
            if value != 0:
                self.elements[(row, col)] = value
        else:
            raise ValueError("Index out of bounds")

    def get(self, row: int, col: int) -> int:
        return self.elements.get((row, col), 0)

    def add(self, other: "SparseMatrix") -> "SparseMatrix":
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions do not match")

        result = SparseMatrix((self.rows, self.cols), {})

        for (row, col), value in self.elements.items():
            result.set(row, col, value + other.get(row, col))

        return result

    def subtract(self, other: "SparseMatrix") -> "SparseMatrix":
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions do not match")

        result = SparseMatrix((self.rows, self.cols), {})

        for (row, col), value in self.elements.items():
            result.set(row, col, value - other.get(row, col))

        return result

    def display(self) -> None:
        for row in range(self.rows):
            row_str = ""
            for col in range(self.cols):
                row_str += str(self.get(row, col)) + "\t"
            print(row_str)

    @classmethod
    def from_dense_matrix(cls, dense_matrix: List[List[int]]) -> "SparseMatrix":
        shape = (len(dense_matrix), len(dense_matrix[0]))
        data = {
            (row, col): value
            for row, row_data in enumerate(dense_matrix)
            for col, value in enumerate(row_data)
            if value != 0
        }
        return cls(shape, data)


if __name__ == "__main__":
    # Example usage
    dense_matrix1 = [[0, 1, 2], [1, 2, 0]]
    dense_matrix2 = [[3, 0, 0], [0, 4, 5]]

    # Creating sparse matrices from dense matrices
    sparse_matrix1 = SparseMatrix.from_dense_matrix(dense_matrix1)
    sparse_matrix2 = SparseMatrix.from_dense_matrix(dense_matrix2)

    # Displaying sparse matrices
    print("Sparse Matrix 1:")
    sparse_matrix1.display()

    print("Sparse Matrix 2:")
    sparse_matrix2.display()

    # Adding two sparse matrices
    add_matrix = sparse_matrix1.add(sparse_matrix2)
    print("Matrix Addition:")
    add_matrix.display()

    dense_matrix3 = [[1, 0], [0, 2], [3, 0]]
    dense_matrix4 = [[0, 0], [4, 0], [0, 5]]

    # Creating sparse matrices from dense matrices
    sparse_matrix3 = SparseMatrix.from_dense_matrix(dense_matrix3)
    sparse_matrix4 = SparseMatrix.from_dense_matrix(dense_matrix4)

    # Displaying sparse matrices
    print("Sparse Matrix 3:")
    sparse_matrix3.display()

    print("Sparse Matrix 4:")
    sparse_matrix4.display()

    # Adding two sparse matrices
    add_matrix2 = sparse_matrix3.add(sparse_matrix4)
    print("Matrix Addition 2:")
    add_matrix2.display()

    dense_matrix5 = [[0, 0, 0, 0], [1, 0, 2, 0], [0, 3, 0, 4], [0, 0, 0, 0]]

    dense_matrix6 = [[0, 1, 0, 0], [0, 0, 2, 0], [3, 0, 0, 4], [0, 0, 5, 0]]

    # Creating sparse matrices from dense matrices
    sparse_matrix5 = SparseMatrix.from_dense_matrix(dense_matrix5)
    sparse_matrix6 = SparseMatrix.from_dense_matrix(dense_matrix6)

    # Displaying sparse matrices
    print("Sparse Matrix 5:")
    sparse_matrix5.display()

    print("Sparse Matrix 6:")
    sparse_matrix6.display()

    # Adding two sparse matrices
    add_matrix3 = sparse_matrix5.add(sparse_matrix6)
    print("Matrix Addition 3:")
    add_matrix3.display()
