import hashlib
import sys

def create_hash(value):
    md5hash = hashlib.md5(value.encode()).hexdigest()
    print(md5hash)

create_hash(sys.argv[1])

