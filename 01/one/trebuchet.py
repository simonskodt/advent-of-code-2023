import sys

total_sum = 0
try:
    while 1:
        line = sys.stdin.readline().strip()
        if not line:
            break

        fst, snd = "", ""
        for c in line:
            if c.isdigit() and not fst:
                fst = c
            if c.isdigit():
                snd = c

        num = int(fst * 2) if not snd else int(fst + snd)
        total_sum += num
except EOFError:
    pass

print(total_sum)
