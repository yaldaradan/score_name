import string

file_path = "/Users/yaldaradan/Downloads/names.txt"
with open(file_path, 'r') as file:
    content = file.read()
arr = [name.strip("\"") for name in content.split(",")]
print(arr)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def find_score(namee, arr):
    for name in arr:
        if (name == namee):
            return score_dict[namee]
    return -1

arr = merge_sort(arr)
print(arr)

score = 0
score_dict={}
alpha_dict={}
counter = 1
index=0

for letter in string.ascii_uppercase:
    alpha_dict[letter] = counter
    counter +=1

print(alpha_dict['C'])
for name in arr:
    index+=1
    for character in name:
        score += alpha_dict[character]
    if (name == "COLIN"):
        print(score)
        print(index)
    score_dict[name] = score*index
    score = 0


print(find_score("COLIN", arr))









