# x = "Hello World"
y = 6
# print(f"{x} {y}")
#
z = 25
a = -10.5
#
# print(int(a))

# for i in range(abs(z * int(a))):
#     print(f"{i}:{x}")
#
bedragen = [15, -100, 30, -2, y, z, a]
lijst = []
lengte = len(bedragen)
# print(f"lengte: {lengte}")

for bedrag in bedragen:

    kosten = -1 * (abs(bedrag))
    print(f":: {kosten}")

    if kosten <= -15:
        if kosten == -25:
            kosten = "pause"
        lijst.append(kosten)
    else:
        kosten *= 1000
        lijst.append(kosten)

print(lijst)

