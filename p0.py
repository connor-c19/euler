from math import sqrt

def sum_square(use_evens: bool, use_odds: bool, number: int) -> float:
    sum = 0
    for x in range(number+1):
        if use_evens and (x**2 % 2) == 0:
            sum += x**2
        elif use_odds and (x**2 % 2) != 0:
            sum += x**2

    return sum


if __name__=='__main__':
    while True:
        try: number = int(input("Number of squares: "))
        except: print("Enter valid int")
        else: break

    use_evens = 'y' in input("'y' to sum evens: ")
    use_odds = 'y' in input("'y' to sum odds: ")

    print(str(sum_square(use_evens, use_odds, number)))

