# Switching from raising exceptions to asserts... seems a better solution
# as it will catch issues in test environments, and can be easily disabled
# by running the command with -O or -OO to disable debug messages
#
# let's get some regular expressions for this
import re

def chunkify(string, chunk_length, fill='x'):
    assert len(string) > 0, "var string must be at least one char"
    assert chunk_length > 0, "var chunk_length must be at least 1"
    assert len(fill) == 1, "var fill must be one char"
    pad = chunk_length - (len(string) % chunk_length)
    string = string + "".join((fill,) * pad)
    sre = re.compile(rf'(.{{{chunk_length}}})')
    return [x for x in re.split(sre, string) if x]

print(chunkify("ABCDEFG", 3, 'x'))
print(chunkify("xyzCDQplm", 4, 'y'))
print(chunkify("AB", 16))
print(chunkify("", 16))

pass
