input_str = "Hello World! My name is Nuri!"

frq = {}
for c in input_str:
    if c in frq:
        frq[c] += 1
    else:
        frq[c] = 1

print(frq)

