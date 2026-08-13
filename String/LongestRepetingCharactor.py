def repeting(s , k):
  ans =0
  length = 0
  max_length =0

  for i in range(len(s)):
    count = {}

    for j in range( i , len(s)):
      count[s[j]] = count.get(s[j],0)+1

      length = j-i+1
      max_length = max(count.values())

      if length - max_length <= k:
        ans = max(ans , length)

  return ans  
print(repeting("AABBBBAAAA", 1))