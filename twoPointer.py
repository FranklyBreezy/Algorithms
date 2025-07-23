def twoPointer(arr, target):
    lf = 0
    rt = len(arr) - 1
    arr.sort()
    while lf < rt:
        add = arr[lf] + arr[rt]
        if add == target:
            return (lf, rt)
        if add < target:
            lf += 1
        if add > target:
            rt -= 1
    return (-1, -1)

n = int(input("Length of array: "))
murray = []
for j in range(n):
    murray.append(int(input("Int value to be inserted: ")))
trgt = int(input("Target value: "))
print(twoPointer(murray, trgt))
