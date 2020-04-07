input = input()
ints = [int(num) for num in input.split(" ")]
list_sort = sorted(ints)

print("\n".join([str(item) for item in list_sort]))
print()
print("\n".join(input.split(" ")))
