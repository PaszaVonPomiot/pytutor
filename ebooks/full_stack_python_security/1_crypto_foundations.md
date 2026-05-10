# Cryptography Foundations

## Hashing

Message -> hash function -> hash value

- Variable-length input, fixed-length output
- Deterministic
- Avalanche effect: a small input change causes a large output change

Python's `hash()` is not a cryptographic hash.

### Cryptographic Hash Properties

- One-way: input should be hard to recover from output
- Weak collision resistance: hard to find a second message with the same hash as a given message
- Strong collision resistance: hard to find any two messages with the same hash

```python
print(hash("dupa"))
print(hash("dupa"))
print(hash("dupa2"))
```

## `hashlib`

- `MD5` and `SHA1` are not suitable for integrity protection
- Prefer `SHA2`, `SHA3`, or `Blake`
- Strings must be encoded to `bytes` before hashing

```python
import hashlib
from hashlib import sha256

print(hashlib.algorithms_available)
print(hashlib.algorithms_guaranteed)

hash1 = hashlib.sha256(b"duuupa")
hash2 = hashlib.sha256("duuupa".encode())

print(hash1.digest_size, "bytes")
print(hash1.hexdigest())
print(hash2.hexdigest())
print(hash1.digest())
print(hash2.digest())

many = sha256()
many.update(b"m")
many.update(b"e")
many.update(b"s")
many.update(b"s")
print(many.hexdigest())

print(sha256(b"mess").hexdigest())
```

## Checksums

- Checksums like CRC and Adler-32 are fast and useful for error detection
- They are not strong enough for cryptographic integrity checks

```python
import zlib

print(zlib.crc32(b"gnu"))
print(zlib.crc32(b"codding"))
print(zlib.adler32(b"gnu"))
print(zlib.adler32(b"codding"))
```

## Key Generation

- Use `secrets` for secret values
- Do not use `random` for keys

```python
import os
from secrets import token_bytes, token_hex, token_urlsafe

print(os.urandom(16))
print(token_bytes(16))
print(token_hex(16))
print(token_urlsafe(16))
```

### Passphrases

```python
import secrets
from pathlib import Path

words = Path("wordlist.txt").read_text().splitlines()
passphrase = " ".join(secrets.choice(words) for _ in range(4))
print(passphrase)
```

## Keyed Hashing

- A keyed hash depends on both message and key
- The same message hashed with different keys produces different results

```python
from hashlib import blake2b

m = b"message"
x = b"key x"
y = b"key y"

print(blake2b(m, key=x).hexdigest())
print(blake2b(m, key=y).hexdigest())
```

## HMAC

- HMAC turns a hash function into a keyed message authentication mechanism
- Inputs: message, key, hash function

```python
import hashlib
import hmac

xx = hmac.new(key=b"key", msg=b"message", digestmod=hashlib.sha3_256)
print(xx.name)
print(xx.hexdigest())
```

### Authenticating a Message

```python
import hashlib
import hmac
import json

outbound_hmac_sha256 = hmac.new(b"shared_key", digestmod=hashlib.sha256)
outbound_message = b"from Bob to Alice"
outbound_hmac_sha256.update(outbound_message)
outbound_hash_value = outbound_hmac_sha256.hexdigest()

outbound_authenticated_msg = {
    "message": list(outbound_message),
    "hash_value": outbound_hash_value,
}
outbound_msg_to_alice = json.dumps(outbound_authenticated_msg)

inbound_msg_from_bob = outbound_msg_to_alice
inbound_authenticated_msg = json.loads(inbound_msg_from_bob)
inbound_message = bytes(inbound_authenticated_msg["message"])

inbound_hmac_sha256 = hmac.new(b"shared_key", digestmod=hashlib.sha256)
inbound_hmac_sha256.update(inbound_message)
inbound_hash_value = inbound_hmac_sha256.hexdigest()

if inbound_hash_value == inbound_authenticated_msg["hash_value"]:
    print("trust message")
```

## Timing Attacks

- Comparing hashes with `==` can leak timing information
- Use `compare_digest()` instead

```python
from hmac import compare_digest

compare_digest("abc", "abcd")
```

## Symmetric Encryption

- Encryption provides confidentiality
- Decryption reverses it
- `Fernet` provides authenticated symmetric encryption

```python
from cryptography.fernet import Fernet

fernet_key = Fernet.generate_key()
print(fernet_key)

fernet = Fernet(fernet_key)
token = fernet.encrypt(b"duuupa")
print(token)
```

## Key Rotation

- Replace an old key with a new one
- Decrypt old ciphertext and re-encrypt with the new key

```python
from cryptography.fernet import Fernet, MultiFernet

old_key = Fernet.generate_key()
old_fernet = Fernet(old_key)
old_token1 = old_fernet.encrypt(b"dupa")
old_token2 = old_fernet.encrypt(b"krowa")

new_key = Fernet.generate_key()
new_fernet = Fernet(new_key)

multi_fernet = MultiFernet([new_fernet, old_fernet])
old_tokens = [old_token1, old_token2]
new_tokens = [multi_fernet.rotate(token) for token in old_tokens]

for new_token in new_tokens:
    rotated_plaintext = new_fernet.decrypt(new_token)
    print(rotated_plaintext)
```
