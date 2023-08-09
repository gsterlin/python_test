# An attempt to add in some checking and raise errors if there are issues
#
# NOTE: This is making some potentially gross assumptions about the specs
#       for the definition of the project
#
# Assumptions:
#    * the string must be at least one character long
#    * renaming chunck_length to chunk_length is okay
#    * chunk_length must be at least 1, splitting on zero may not make sense
#    * fill must be a single character
#
# let's get some regular expressions for this
import re

def chunkify(string, chunk_length, fill='x'):
    if (len(string) < 1):
        raise ValueError("string must be at least one character")
    if (chunk_length < 1):
        raise ValueError("chunk_length must be at least 1")
    if (len(fill) != 1):
        raise ValueError("fill must be one character")
    pad = chunk_length - (len(string) % chunk_length)
    string = string + "".join((fill,) * pad)
    sre = re.compile(rf'(.{{{chunk_length}}})')
    return [x for x in re.split(sre, string) if x]

print(chunkify("ABCDEFG", 3, 'x'))
print(chunkify("xyzCDQplm", 4, 'y'))
