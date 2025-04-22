x = 3

# range(start, stop, step),
# x is the start, -1 means go up to but not including -1,
# -1 is the step (go down by 1).

for i in range(x, -1, -1):
    print(i, end = ' ' ) # Normally, print() adds a new line after each print.
                         # But with end=' ', you're telling it: “Instead of a new line, just put a space.”
