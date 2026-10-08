


# A
# A B
# A B C
# A B C D

s="ABCD"

def design_print(s):
  seen=""
  n=input("Enter value:")
  for ch in s:
    seen+=ch
    print(seen)
design_print(s)
