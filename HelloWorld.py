from ntpath import join


print("Hello World!")
age=25
items=4
print(age*items)
price=19.99
quantity=3
total=price*quantity
print(total)
z=3+4j
print(z.real)
print(z.imag)
name="Brandon"
print("Hello "+name)
is_logged_in=True
if is_logged_in:
 print("Welcome back!")
fruits=["apples","bananas"]
print(fruits)
fruits.append("cherrys")
print(fruits)
location=(40.7128,-74.0060)
print(location[0], location[1])
for i in range(1):
 print(i)



user={"name":"Brandon","age":25,"email":"brandon@example.com","roles":["admin","user"]}
print(user["name"],user["age"],user["email"],user["roles"])

constant=frozenset([3.14,2.718])
data=bytes([5])
print(data)

msg = "Hello, World! The sky is blue asf."
print(len(msg))
print(msg[2:6]) #'H'

name = "ALICE"

print(name.lower()) 
pass

print(r"C:\Users\jupit\Desktop\it-dashboard\requirements.txt".lower())
pass
line = "apples,bananas,cherrys"
print(line.split("a"))
print(line)
pass
word = ["Hello", "there"]
print(" ".join(word))

pass
name = "Brandon"
print(f"Hello, {name}!")

name = "Carl"
print("Hello, {name}!")
pass 

a = 5000
b = 10000
c = 39274739
print(f"sum is {a+b+c:,}")
pass

msg2 = '''This is a multi-line comment 
this is more line
more line
more line
stop here'''
print(msg2)

