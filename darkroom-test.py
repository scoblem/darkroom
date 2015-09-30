import darkroom

# Test to validate actor positions

def test(grid, n):
    count = 0
    total = 0
    for i in range(n):
        items = darkroom.get_position(grid)

        for i in items:
            total += 1
            if items.count(i) > 1:
                count +=1

    duplicates = count / 2
    print("{0} Duplicated Tuples of {1} Detected".format(duplicates, total))

# x = tester(room, 1000000)
test(darkroom.make_grid(3), 1000)
