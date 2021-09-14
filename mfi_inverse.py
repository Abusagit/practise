class Solver:
    def __init__(self):
        self.a, self.b, self.c, self.d, self.f = self.obtain_coefficients()

    def give_concentration(self):
        MFI = float(input("Insert MFI: "))
        if MFI > 0:
            result = (((self.b - self.a) / (MFI - self.a)) ** (1 / self.f) - 1) ** (1 / self.d) * self.c
            return round(result, 3) if isinstance(result, (float, int)) else "NA"
        return 0

    @staticmethod
    def obtain_coefficients():
        MFI_plus_coefficients = map(float, (input(f"{letter} coefficient: ") for letter in "abcdf"))
        return MFI_plus_coefficients

    def __repr__(self):
        return f"a = {self.a}\nb = {self.b}\nc = {self.c}\nd = {self.d}\nf = {self.f}"


if __name__ == '__main__':
    eq = Solver()
    print(eq.give_concentration())