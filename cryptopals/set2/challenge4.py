import base64
import secrets

from cryptopals.set1.challenge7 import aes_ecb_decrypt, aes_ecb_encrypt
from cryptopals.set2.challenge1 import pcks7_pad

KEY = secrets.token_bytes(16)


def consistent_ecb_encrypt(s: bytes) -> bytes:
    suffix = """
        Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
        aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
        dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
        YnkK
    """
    suffix = base64.b64decode(
        "".join(map(lambda x: x.strip(), suffix.split("\n"))))
    s += suffix

    return aes_ecb_encrypt(pcks7_pad(s, 16), KEY)


def main():
    # Detect block size by checking for two exact ciphertext sequences
    block_size = 0
    for i in range(1, 128 + 1):
        result = consistent_ecb_encrypt(("a" * i * 2).encode("utf-8"))
        index = result[1:i*2].find(result[:i])
        if index != -1:
            block_size = i
            break

    # Brute-force one byte at a time
    decrypted = bytearray()
    for block in range(1, 17):
        detected_bytes = bytearray()
        for i in range(block_size - 1, -1, -1):
            plaintext = ("a" * i).encode("utf-8")
            result = consistent_ecb_encrypt(plaintext)

            for x in range(256):
                guess = consistent_ecb_encrypt(
                    plaintext + decrypted + detected_bytes + bytes([x])
                )
                if result[:block_size * block] == guess[:block_size * block]:
                    detected_bytes.append(x)
                    break

        decrypted.extend(detected_bytes)

    print(decrypted)


if __name__ == "__main__":
    main()
