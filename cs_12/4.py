def even_numbers(n):
    num = [str(i) + "\n" for i in range(2, n + 1, 2)]
    f = open("even_numbers.txt", "w")
    f.writelines(num)
    f.close()
    print("Even numbers from 1 to", n, "saved in even_numbers.txt")

n = int(input("Enter a number : "))
even_numbers(n)


