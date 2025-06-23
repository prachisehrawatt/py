def mul_table(n):
    lst = []
    for i in range(1, 11):
        line = f"{n} x {i} = {n * i}\n"
        lst.append(line)
    return lst

def main():
    try:
        num = int(input("Enter a number: "))
        table = mul_table(num)

        f=open("table.txt", "w")
        f.writelines(table)
        print(f"Multiplication table of [num] saved in table.txt")

    except ValueError:
        print("Please enter a valid integer.")

main()
