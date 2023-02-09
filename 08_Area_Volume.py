AREA = 4*3.14159
VOLUME = (4/3)*3.14159

radius = int(input("radius:"))

s_area = radius * radius * AREA
s_vol = radius * radius * radius * VOLUME

print(f"The surface area is {s_area:.2f} and the volume is {s_vol:.2f}")

