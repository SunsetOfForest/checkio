def long_repeat(line):
    if not line:
        return 0
    elif len(line) == 1:
        return 1
    else:
        count = 0
        if line[0] == line[1]:
            for j in line[1:]:
                if j == line[0]:
                    count += 1
                else:
                    break   
            return max(count+1,long_repeat(line[1:]))
        else:
            return long_repeat(line[1:])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(long_repeat('sdsffffse'))
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
