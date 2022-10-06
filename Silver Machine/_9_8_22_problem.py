#tarting time
hours = 6
minis = 52
seconds = 0
#after first mile
minis += 8
seconds += 15
#3mile stem
for i in range(3):
    minis += 7
    seconds += 12
#final mile
minis += 8
seconds += 12
#math
extramin = seconds / 60
seconds = seconds % 60
minis = minis + extramin 
extrahr = int(minis /60)
minis = int(minis % 60)
hours = hours + extrahr
#output
print("You get home at  " + str(hours) + ":" + str(minis) + ":" + str(seconds) + " AM")

def time(hourz, miniz , secondz):
