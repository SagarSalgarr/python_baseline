generator_exp = (i * 5 for i in range(5) if i % 2 == 0)

for i in generator_exp:
    print(i)

def simple_gen():
    for x in range(3):
        yield x

g = simple_gen()
g = iter(g)
try:
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))  # This will raise a StopIteration error
except StopIteration:
    print("End of generator reached.")