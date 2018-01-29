from json import load

pop = load(open('population.json'))

s = 0
for key, value in pop.items():
    if key != "united kingdom":
        s += value
pop_per_seat = s/750
print(f"Population in the EU withou the UK: {round(s)}")
print(f"Population per MEP: {pop_per_seat}")

data = {}
seats = 0
for key, value in pop.items():
    if key != "united kingdom":
        print(f'Country: {key}\t Seats: {round(value/pop_per_seat)}')
        seats += round(value/pop_per_seat)
        data[key] = round(value/pop_per_seat)

print(seats)

print(dict(sorted(data.items(), key=lambda a: a[1], reverse=True)))
