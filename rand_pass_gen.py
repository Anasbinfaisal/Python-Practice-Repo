
import secrets
import string

alphabet_string = string.ascii_lowercase

alps = list(alphabet_string)
seq = [n for n in range(0, 10)]


punctuation = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(',
               '-', '"', '*', '|', ',', '&', '<', '`', '}', '.',
               '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']

pass_gen = []

for n in range(5):
    num = secrets.choice(seq)
    alp = secrets.choice(alps)
    punch = secrets.choice(punctuation)
    pass_gen.append(num)
    pass_gen.append(alp)
    pass_gen.append(punch)

pass_str = ''.join([str(elem) for elem in pass_gen])

print(pass_str)

