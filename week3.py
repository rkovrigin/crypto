import codecs
from Cryptodome.Hash import SHA256

h0 = codecs.decode("03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8", 'hex')
path = "data/6.1.intro.mp4_download"
block_size = 1024

f = open(path, 'br')

blocks = []
block = f.read(block_size)

while block:
    blocks.append(block)
    block = f.read(block_size)

h = SHA256.new(blocks[-1])

for block in reversed(blocks[:-1]):
    h = SHA256.new(block + h.digest())

print(h.hexdigest())