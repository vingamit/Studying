first_set = list(map(int, input().split()))
second_set = list(map(int, input().split()))
def intersection(first, second):
    return sorted(set(first) & set(second))
print(*intersection(first_set, second_set))