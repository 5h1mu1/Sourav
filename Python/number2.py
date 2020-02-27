import re
f = open("/mnt/2CC3EF1562FE8B46/CODE_ZONE/Mern/project3/Python/Given data.txt", "r")
# if you face any problem in reading the file you should just tweak your file path
lines = f.readlines()
f2 = open("output data.txt", "w+")
for line in lines:
    if line[-2] == 'u':
        modified1 = line.replace('u', '^-6')
        f2.write(re.sub(r'data0_', '', modified1.replace("  ", '')))
    if line[-2] == 'm':
        modified1 = line.replace('m', '^-3')
        f2.write(re.sub(r'data0_', '', modified1))
    if line[-2] == 'f':
        modified1 = line.replace('f', '^-15')
        f2.write(re.sub(r'data0_', '', modified1))
    if line[-2] == 'p':
        modified1 = line.replace('p', '^-12')
        f2.write(re.sub(r'data0_', '', modified1))
    if line[-2] == 'n':
        modified1 = line.replace('n', '^-9')
        f2.write(re.sub(r'data0_', '', modified1))
