# This script is the first real attempt at solving the chunkify problem
#
# NOTE: partial solution from https://stackoverflow.com/questions/13673060/split-string-into-strings-by-length
#       and built upon to meet the understanding I have of the specifications for chunkify
#
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
