'''
--- Day 1: The Tyranny of the Rocket Equation ---
Santa has become stranded at the edge of the Solar System while delivering presents to other planets! To accurately calculate his position in space, safely align his warp drive, and return to Earth in time to save Christmas, he needs you to bring him measurements from fifty stars.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

The Elves quickly load you into a spacecraft and prepare to launch.

At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper. They haven't determined the amount of fuel required yet.

Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

For example:

For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
For a mass of 1969, the fuel required is 654.
For a mass of 100756, the fuel required is 33583.
The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.

What is the sum of the fuel requirements for all of the modules on your spacecraft?
'''

with open('input.txt') as f:
    duomenys = list(f)
print(len(duomenys))
kuras = []

for mass in duomenys:
    kuras.append(int(int(mass)/3)-2)

print(kuras[0])
print(f'Viso kuro reikės {sum(kuras)}')

print('this marks the experiment zone')

kuras2 = []

for mass in duomenys:
    a = int(mass)
    b = int(mass)
    while a > 0:
        a = int(a/3)-2
        if a <= 0:
            break
        b += a
    kuras2.append(b - int(mass))
print(f'Total amount of fuel required, accounting for weight of fuel is: {sum(kuras2)}')
print(f'This is actually {sum(kuras2) - sum(kuras)} more than initially calculated')

#TESTING

'''kuras3 = []
test = [12, 14, 1969, 100756]
for mass in test:
    a = int(mass)
    b = int(mass)
    while a > 0:
        a = int(a/3)-2
        if a <= 0:
            break
        b += a
    kuras3.append(b-mass)
print(kuras3)'''