"""
AFFINE CIPHER - Versi Sederhana
===============================
Enkripsi: C = (a * P + b) mod 26
Dekripsi: P = a^(-1) * (C - b) mod 26
"""

def gcd(a, b):
    """Menghitung Greatest Common Divisor"""
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m=26):
    """Menghitung modular inverse dari a mod m"""
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def is_valid_key(a):
    """Cek apakah kunci 'a' valid (coprime dengan 26)"""
    return gcd(a, 26) == 1

def affine_encrypt(text, a, b):
    """
    Enkripsi dengan Affine Cipher
    C = (a * P + b) mod 26
    """
    if not is_valid_key(a):
        print(f"Error: Kunci a={a} tidak valid!")
        return None
    
    result = ""
    for char in text.upper():
        if char.isalpha():
            # A=0, B=1, ..., Z=25
            p = ord(char) - ord('A')
            c = (a * p + b) % 26
            result += chr(c + ord('A'))
        else:
            result += char  # Spasi dan karakter lain tetap
    
    return result

def affine_decrypt(text, a, b):
    """
    Dekripsi dengan Affine Cipher
    P = a^(-1) * (C - b) mod 26
    """
    if not is_valid_key(a):
        print(f"Error: Kunci a={a} tidak valid!")
        return None
    
    a_inv = mod_inverse(a)
    if a_inv is None:
        print(f"Error: Tidak bisa menghitung inverse dari {a}")
        return None
    
    result = ""
    for char in text.upper():
        if char.isalpha():
            # A=0, B=1, ..., Z=25
            c = ord(char) - ord('A')
            p = (a_inv * (c - b)) % 26
            result += chr(p + ord('A'))
        else:
            result += char  # Spasi dan karakter lain tetap
    
    return result

def main():
    import sys
    
    # Cek argumen command line
    if len(sys.argv) != 5:
        print("=== AFFINE CIPHER SEDERHANA ===")
        print("Penggunaan:")
        print("  python main.py <mode> <text> <kunci_a> <kunci_b>")
        print()
        print("Mode:")
        print("  enc  - untuk enkripsi")
        print("  dec  - untuk dekripsi")
        print()
        print("Kunci 'a' yang valid: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25")
        print()
        print("Contoh:")
        print('  python main.py enc "HELLO WORLD" 5 8')
        print('  python main.py dec "RCLLA OAPLX" 5 8')
        return
    
    mode = sys.argv[1].lower()
    text = sys.argv[2]
    
    try:
        a = int(sys.argv[3])
        b = int(sys.argv[4])
    except ValueError:
        print("Error: Kunci a dan b harus berupa angka!")
        return
    
    # Validasi mode
    if mode not in ['enc', 'dec']:
        print("Error: Mode harus 'enc' atau 'dec'")
        return
    
    # Validasi kunci
    if not is_valid_key(a):
        print(f"Error: Kunci a={a} tidak valid!")
        print("Kunci 'a' yang valid: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25")
        return
    
    # Proses enkripsi atau dekripsi
    if mode == 'enc':
        result = affine_encrypt(text, a, b)
        if result:
            print(f"Plaintext: {text}")
            print(f"Kunci: a={a}, b={b}")
            print(f"Ciphertext: {result}")
    
    elif mode == 'dec':
        result = affine_decrypt(text, a, b)
        if result:
            print(f"Ciphertext: {text}")
            print(f"Kunci: a={a}, b={b}")
            print(f"Plaintext: {result}")

if __name__ == "__main__":
    main()
