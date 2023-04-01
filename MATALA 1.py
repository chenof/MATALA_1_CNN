import os

current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)

#### question 1 ###

def my_func(x1, x2, x3):
    try:
        x1 = float(x1)
        x2 = float(x2)
        x3 = float(x3)
    except ValueError:
        return None

    if not all(isinstance(x, float) for x in [x1, x2, x3]):
        print("Error: parameters should be float")
        return None

    denominator = x1 + x2 + x3

    if denominator == 0:
        print("Not a number - denominator equals zero")
        return None

    return (x3 * (x2 + x3) * (x1 + x2 + x3)) / denominator

#num1 = input("x1:")
#num2 = input("x2:")
#num3 = input("x3:")
#print(my_func(num1, num2, num3))

#### question 2 ###

def revword(word: str) -> str:
    return word.lower()[::-1]

def countword() -> int:
    with open('text.txt', 'r') as f:
        lines = f.readlines()
        word = lines[0].strip()
        count = 0
        for line in lines[1:]:
            words = line.strip().split()
            for w in words:
                if revword(w) == word:
                    count += 1
        return count + 1


#file = open('text.txt', 'r')
#data = file.read()
#print(data)

count = countword()
print("The word appeared", count, "times in the document.")