# print("Half Pyramid Pattern of Stars (*):")
# n = int(input("Enter the number of rows for the half pyramid: "))
# for i in range(n):
#     for j in range(i + 1):
#         print("*", end="")
#     print()

print("Floyds Traingle")
rows = int(input("Enter the number of rows for Floyd's triangle: "))
num = 1
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()