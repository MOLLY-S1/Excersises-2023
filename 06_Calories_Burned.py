BIKE_CALORIES = 200
JOG_CALORIES = 475
SWIM_CALORIES = 275

bike = int(input("bike"))
jog = int(input("Jog"))
swim = int(input("swim"))

bc = BIKE_CALORIES * bike
jc = JOG_CALORIES * jog
sc = SWIM_CALORIES * swim

total = bc+jc+sc
weight = (total/3500 * 454) / 1000

print(f"you lost {weight:.3f}kgs!")

