# let's get some regular expressions for this
import re

def chunkify(string, chunck_length, fill='x'):
    pad = chunck_length - (len(string) % chunck_length)
    string = string + "".join((fill,) * pad)
    sre = re.compile(rf'(.{{{chunck_length}}})')
    return [x for x in re.split(sre, string) if x]

print(chunkify("ABCDEFG", 3, 'x'))
print(chunkify("xyzCDQplm", 4, 'y'))

pass
