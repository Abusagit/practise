class Matrix:  # Cоздание класса матрицы
    def __init__(self, matrix: list):
        self.matrix = matrix  # Запись матрицы в атрибут экземпляра класса
        self.determinant = Matrix.determ(self.matrix) if len(matrix) == len(matrix[0]) else None  # Проверка
        # на квадратность

    def __str__(self):  # Перегрузка для удобства отображения
        s = ''
        for row in self.matrix:
            s += f'{row}\n'
        s = s.strip()
        return s

    @staticmethod
    def determ(mtx) -> int:  # Эта функция вызывается при присваивании переменной определителя квадратной матрицы
        if len(mtx) == 2:
            return mtx[0][0] * mtx[1][1] - mtx[0][1] * mtx[1][0]  # рекурсивный случай - определитель 2*2 матрицы
        det = 0
        for col in range(len(mtx[0])):  # В других случаях - считаем определитель матрицы меньшего разряда с умножением
            # на константу, которая высчитывается по формуле
            # (-1)^(номер колонны + номер строки)*(число в этой колонне и строке)

            det += (-1) ** (col + 2) * mtx[0][col] * Matrix.determ([[value for index, value
                                                                     in enumerate(mtx[row]) if index != col]
                                                                    for row in range(1, len(mtx))])
            # У этой матрицы будут колонны и строки без той строки и той колонны,
            # в которой есть элемент, на который мы умножаем
            # И того - рекурсивный спуск и подсчёт
        return det


if __name__ == '__main__':
    A = [[1, 2, 3, 4],
         [1, 0, 2, 0],
         [0, 1, 2, 3],
         [2, 3, 0, 0]
         ]
    B = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

    C = [[1, 2, 4],
         [2, -1, 3],
         [4, 0, 1]]
    D = [[1, 2, 4],
         [2, -1, 3],
         [4, 0, -1]]
    N = [[1, 2, 3],
         [4, 5, 6]]
    for x in (A, B, C, D, N):
        a = Matrix(x)
        print(a)
        print(a.determinant)
