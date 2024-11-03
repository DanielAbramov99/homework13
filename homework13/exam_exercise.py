students: int = int(input("how many students are in the school:"))
classroom: int = students // 30
last_classroom: int = students % 30
print(f"the amount of classes that are full is {classroom}")
if students != 0:
    print(f"the amount of students that in the last classroom are {last_classroom}")

while True:
    try:
        number: int = int(input("enter a number between 10-99:"))
        if not 10 <= number <= 99 or number == int:
            print("the number is not in range")
        else:
            ahadot: int = number % 10
            asarot: int = number // 10
            new_number: int = ahadot * 10 + asarot * 1
            if ahadot > asarot:
                print(new_number)
            else:
                print(number)
                break
    except ValueError:
        print("the number is not in range")

list_prime: list[int] = []
for num in range(2, 200 + 1):
    list_divs: list[int] = []
    for num2 in range(2, num):
        list_divs.append(num % num2)
    if all(list_divs):
        list_prime.append(num)
print(list_prime)

question: list[str] = []

while True:
    answer: str = str(input("enter your answer:"))
    if answer == "x":
        break
    if answer == "a" or answer == "b" or answer == "c" or answer == "d":
        question.append(answer)
    else:
        print("invalid answer,try again")

print(
    f"the amount of student that are answered a:{question.count("a")}, b:{question.count("b")},"
    f" c:{question.count("c")} and d:{question.count("d")}")
