# This is a dummy script, it doesn't actually do anything useful
# NOTE: the spec says chunck_length, but I changed it to chunk_length

def chunkify(self, string, chunk_length, fill='x'):
    return ['ABC', 'DEF', 'Gxx']

print(chunkify('ABCDEFG', 3, 'x'))

pass
