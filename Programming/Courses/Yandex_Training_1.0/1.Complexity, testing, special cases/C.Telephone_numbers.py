numb = input()


def to_num(num):
    d = ''
    for nu in num:
        if nu.isdigit():
            d += nu
    return d


numb = to_num(numb)
if len(numb) < 8:
    numb = '8495' + numb

for i in range(3):
    nums = input()
    nums = to_num(nums)
    if len(nums) < 8:
        nums = '8495' + nums
    if nums[1:] == numb[1:]:
        print('YES')
    else:
        print('NO')
