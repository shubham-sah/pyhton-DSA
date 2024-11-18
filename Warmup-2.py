def string_times(str, n):
    new_str = ""
    for i in range(n):
        new_str += str
    return new_str


def string_splosion(str):
    new_str = ""
    length = len(str)
    for i in range(length):
        new_str += str[:i+1]
    return new_str



def array_front9(nums):
    length = len(nums)
    cnt = 0
    for i in range(length):
        cnt += 1
        if cnt > 4:
            return False
        if nums[i] == 9:
            return True
    return False


def front_times(str, n):
    length = len(str)
    if(length < 3):
        return str*n
    else:
        return str[:0+3] * n


def last2(str):
    length = len(str)
    if length < 2:
        return 0
    
    end_str = str[length-2:]
    count = 0

    for i in range(length - 2):
        if str[i:i+2] == end_str:
            count += 1
    return count


def array123(nums):
  length = len(nums)
  for i in range(length-2):
    if nums[i] == 1:
      if nums[i+1] == 2 and nums[i+2] == 3:
        return True
  return False


def string_bits(str):
  length = len(str)
  return (str[0:length:2])


def array_count9(nums):
  length = len(nums)
  cnt = 0
  for i in range(length):
    if nums[i] == 9:
      cnt += 1
  return cnt



def string_match(a, b):
  min_len = min(len(a), len(b))
  cnt = 0
  for i in range(min_len-1):
    if(a[i:i+2] == b[i:i+2]):
      cnt += 1
  return cnt



