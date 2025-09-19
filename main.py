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
    print("=== AFFINE CIPHER SEDERHANA ===")
    print("Kunci 'a' yang valid: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25")
    print()
    
    # Contoh penggunaan
    plaintext = "HELLO WORLD"
    a = 5  # Kunci multiplicative
    b = 8  # Kunci additive
    
    print(f"Plaintext: {plaintext}")
    print(f"Kunci a: {a}, b: {b}")
    print()
    
    # Enkripsi
    ciphertext = affine_encrypt(plaintext, a, b)
    if ciphertext:
        print(f"Hasil Enkripsi: {ciphertext}")
        
        # Dekripsi
        decrypted = affine_decrypt(ciphertext, a, b)
        if decrypted:
            print(f"Hasil Dekripsi: {decrypted}")
            
            # Verifikasi
            if plaintext == decrypted:
                print("✓ Enkripsi dan dekripsi berhasil!")
            else:
                print("✗ Ada kesalahan!")
    
    print()
    print("=== MODE INTERAKTIF ===")
    
    while True:
        print("\nPilihan:")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Keluar")
        
        pilihan = input("Masukkan pilihan (1-3): ").strip()
        
        if pilihan == "1":
            text = input("Masukkan teks untuk dienkripsi: ").strip()
            try:
                a = int(input("Masukkan kunci a: "))
                b = int(input("Masukkan kunci b: "))
                
                result = affine_encrypt(text, a, b)
                if result:
                    print(f"Hasil enkripsi: {result}")
            except ValueError:
                print("Error: Masukkan angka yang valid!")
        
        elif pilihan == "2":
            text = input("Masukkan teks untuk didekripsi: ").strip()
            try:
                a = int(input("Masukkan kunci a: "))
                b = int(input("Masukkan kunci b: "))
                
                result = affine_decrypt(text, a, b)
                if result:
                    print(f"Hasil dekripsi: {result}")
            except ValueError:
                print("Error: Masukkan angka yang valid!")
        
        elif pilihan == "3":
            print("Terima kasih!")
            break
        
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
