'''
TO CHEAK IF THE 2 STRINGS HAVE ANY SUBSTRING,LIKE IN BELOW EXAMPLE 'HELLO' AND 'WORLD' HAS O,L SUBSTRINGS.
'''
def twoStrings(s1,s2):
  return 'YES' if set(s1)&set(s2) else 'NO'
twoStrings('Hello','world')
