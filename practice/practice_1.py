from collections import defaultdict

def two_sum(nums, k):
  seen = {}
  
  for index, num in enumerate(nums):
    left_num = k - num
    
    if left_num in seen:
      return [seen[left_num], index]
      
    seen[num] = index
    
  return []
  

def best_buy_sell_stock(nums):
  max_profit = 0
  min_buy = float('inf')
  
  for index in range(len(nums)):
    min_buy = min(nums[index], min_buy)
    max_profit = max(max_profit, nums[index] - min_buy)
    
  return max_profit
  
  
def prod_arr_except_self(nums):
  output = [1 for num in nums]
  
  # prefix products
  pref = 1 
  for i in range(1, len(nums)):
    output[i] = pref * nums[i-1]
    pref *= output[i]
    
  print(output)
  
  # suffix products
  suff = 1
  for i in range(len(nums) - 1, -1, -1):
    output[i] *= suff
    suff *= nums[i]
    
  # output
  return output
  

def max_subarr_sum(nums):
  
  max_sum = float('-inf')
  curr_max_sum = 0
  
  for i in range(len(nums)):
    curr_max_sum = max(nums[i], curr_max_sum + nums[i])
    max_sum = max(max_sum, curr_max_sum)
    
  
  return max_sum
  

def long_substr(s=""):
  seen = {}
  max_len = 0
  left = 0
  
  for right, char in enumerate(s):

    if char in seen and seen[char] >= left:
      left = seen[char] + 1
      
    seen[char] = right
    max_len = max(right - left + 1, max_len)
    
  return max_len
  

def groupAnagram(str_arr = []):
  seen = defaultdict(list)
  
  for s in str_arr:
    sort_word = "".join(sorted(s))
    seen[sort_word].append(s)
    
  return list(seen.values())
  
# print(groupAnagram(["tan","atn","pan"]))

def long_pallindrome(s=""):
  result = ""
  
  def expand(left, right):
    while left >= 0  and right < len(s) and s[left] == s[right]:
      left -= 1
      right += 1
    
    return s[left + 1: right]
  
  for i in range(len(s)):
    
    # Odd
    s1 = expand(i, i)
    
    # Even
    s2 = expand(i , i+1)
    
    if len(s1) > len(result):
      result = s1

    if len(s2) > len(result):
      result = s2
    
  return result
  
print(long_pallindrome("abdbafdsd"))
    
  
      
  
    