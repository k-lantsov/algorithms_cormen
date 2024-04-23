def search(input_list, elem):
    for i in range(len(input_list)):
        if elem == input_list[i]:
            return i
    return None

input_list = list(map(int, input().split()))
elem = int(input())
index = search(input_list, elem)
print(index)