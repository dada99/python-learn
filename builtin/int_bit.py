# example for int's bitwise operation
a = 1
a_bin = "0b00000001"
b = 2
b_bin = "0b00000010"

print("a: "+str(a))
print("a_bin: "+str(int(a_bin,2)))
print("b: "+str(b))
print("b_bin: "+str(int(b_bin,2)))

print("a|b: "+str(a|b))
print("a^b: "+str(a^b))
print("a&b: "+str(a&b))
print("b << 2: "+str(b << 2))
print("b >> 1: "+str(b >> 1))