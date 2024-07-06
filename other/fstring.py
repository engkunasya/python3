x = "Hello guys, i am coming for you in "
y= 200
z = "minutes"
f = 2.52

speech = f"sooo {x} {y} {z}"
print(f"sooo {x} {y} {z}")
print (speech)
print(f"{x}{y:15d} {z}yaa")
print(f"{x} {y:^15d} {z}yaa")
print(f"{x} {y:>15d} {z}yaa")
print(f"{x} {y:*>15d} {z}yaa")
print(f"{x} {y:*>15d} {z:<10s} yaa")
print(f"{x} min{f:10.2f} {z:<10s} yaa")
print(f"{x} min{f:.2f} {z:<10s} yaa")
print(f"{x} min{f:,.2f} {z:<10s} yaa")