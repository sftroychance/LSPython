# Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates all the odd-indexed characters of S with all the even-indexed characters of S, this process should be repeated N times.

# Together with the encryption function, you should also implement a decryption function which reverses the process.

# If the string S is an empty value or the integer N is not positive, return the first argument without changes.

def encrypt(text, n):
    if not text or n < 1:
        return text

    for _ in range(n):
        # odd = []
        # even = []

        # [odd.append(x) if idx % 2 == 1 else even.append(x) for idx, x in enumerate(text)]

        # text = ''.join(odd + even)
        text = text[1::2] + text[::2]
    return text

def decrypt(text, n):
    if not text or n < 1:
        return text

    last_char = text[-1] if len(text) % 2 == 1 else ''

    middle = len(text) // 2

    for _ in range(n):
        start = text[:middle]
        end = text[middle:]

        text = ''.join(a + b for a, b in zip(end, start))

    return text + last_char

print(encrypt("012345", 2) == '304152')
print(encrypt("012345", 3) == '012345')
print(decrypt("012345", 3) == '012345')
print(decrypt("304152", 2) == '012345')
