import string

ciph = string.ascii_uppercase + " ?./!\'\"_-+:;*@#₹&()\\1234567890~÷×¶∆^°=%[]©®™"
max = len(ciph)

cod = input("Encipher or Decipher? (E/d) ")

shift = input(f"Shift ({max},0): ")

if not shift.isdigit():
   print("Integral shift only")
   exit(1)


shift = int(shift)

if shift not in range(0,max):
   print("Shift out of range", 0, max)
   exit(1)

if cod.lower() == "d":
  shift = max - shift
  print("Decipher")
else:
  print("Encipher")

msg = input(f"Message: ")

enc = []
msg = msg.upper()
for m in msg:
  ind = ciph.index(m)
  cind = ind + shift
  if cind > max-1:
     cind -= max
  enc.append(ciph[cind])

print("".join(enc))

