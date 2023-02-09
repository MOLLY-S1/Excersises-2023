""" volume of concrete needed for each job and total needed for
all jobs per day
foundation  = 50
residential = 25"""

type_build = input("build type:").lower()

total = 0
r_depth = 0.5
c_depth = 0.25
while type_build != 'x':
    length = int(input("length in meters:"))
    height = int(input("length in meters:"))
    if type_build == "residential" or "r":
        volume = length * height * r_depth
        total += volume
        print(f"The volume of concrete required for a slab with length "
              f"of {length} in meters and length of {height} in meters and "
              f"a depth of {r_depth} in meters is volume {volume} in meters ")
        print(f"total:{total}")

    elif type_build == "commercial" or "c":
        volume = length * height * c_depth
        total += volume
        print(f"The volume of concrete required for a slab with length "
              f"of {length} in meters and length of {height} in meters and "
              f"a depth of {c_depth} in meters is volume {volume} in meters ")
        print(f"total:{total}")


    else:
        print("that is not a valid input")

    type_build = input("build type:").lower()

