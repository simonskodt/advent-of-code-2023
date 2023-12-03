import sys

convert_numbers = {
    "zero":  "0",
    "one":   "1",
    "two":   "2",
    "three": "3",
    "four":  "4",
    "five":  "5",
    "six":   "6",
    "seven": "7",
    "eight": "8",
    "nine":  "9",
}

total_sum = 0

def extract_letters(numbers, line):
    f_idx, s_idx = 100_000, -1
    fst, snd = "", ""
    for s in numbers:
        i = line.find(s)
        j = line.rfind(s)
        if i != -1 and i < f_idx:
            f_idx = i
            fst = s
            
        if j != -1 and j > s_idx:
            s_idx = j
            snd = s
    return f_idx, s_idx, fst, snd

def extract_numbers(line):
    f_idx, s_idx = 100_000, -1
    fst, snd = "", ""
    for c in line:
        if c.isdigit():
            s_idx = line.rindex(c)
            snd = c
        if c.isdigit() and not fst:
            f_idx = line.index(c)
            fst = c
    return f_idx, s_idx, fst, snd

try:
    while 1:
        line = sys.stdin.readline().strip()
        if not line:
            break

        f_spell_idx, s_spell_idx, f_spell, s_spell = extract_letters(convert_numbers, line)
        f_idx, s_idx, fst, snd = extract_numbers(line)

        f_final = convert_numbers.get(f_spell) if f_spell_idx < f_idx else fst
        s_final = convert_numbers.get(s_spell) if s_spell_idx > s_idx else snd

        total_sum += int(f_final + s_final)
except EOFError:
    pass

print(total_sum)
