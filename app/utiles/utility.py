from hashlib import sha3_512


def hash_value(value):
    val = value.encode()
    hash_val = sha3_512(val).hexdigest()
    return hash_val
