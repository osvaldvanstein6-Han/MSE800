def calc_sums(x, y):
    return x + y 

def calc_mean(x, y):
    return x ** y

def calc_complex(x, y):
    return x - y

def main():
    x = int(input("Please enter an integer valut x: "))
    y = int(input("Please enter an integer value y: "))
    print(f"{x} + {y} =", calc_sums(x, y))
    print(f"power({x},{y}) =", calc_mean(x, y))
    a = 1 + 2j
    b = 3 + 4J
    print(f"{a} - {b} =", calc_complex(a, b))


if __name__ == "__main__":
    main()
    



