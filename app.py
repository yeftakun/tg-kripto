"""
AFFINE CIPHER IMPLEMENTATION
============================

Affine Cipher adalah salah satu algoritma kriptografi klasik yang menggunakan
transformasi linear untuk enkripsi dan dekripsi.

Formula Enkripsi: C = (a * P + b) mod 26
Formula Dekripsi: P = a^(-1) * (C - b) mod 26

Dimana:
- P = plaintext (0-25, A=0, B=1, ..., Z=25)
- C = ciphertext (0-25)
- a = kunci multiplicative (harus coprime dengan 26)
- b = kunci additive (0-25)
- a^(-1) = modular inverse dari a mod 26

Kunci 'a' yang valid (coprime dengan 26):
[1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

Keamanan:
- Hanya ada 12 kunci 'a' yang valid × 26 kunci 'b' = 312 kemungkinan kunci total
- Rentan terhadap analisis frekuensi karena masih substitusi monoalfabetik
- Dapat dipecahkan dengan brute force atau known plaintext attack

Kegunaan:
- Pembelajaran konsep kriptografi
- Dasar untuk memahami transformasi linear dalam kriptografi
- Contoh sistem kriptografi yang secara matematis dapat dianalisis
"""

def gcd(a, b):
    """Menghitung Greatest Common Divisor menggunakan algoritma Euclidean"""
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    """Menghitung modular inverse dari a mod m menggunakan Extended Euclidean Algorithm"""
    if gcd(a, m) != 1:
        return None  # Tidak ada inverse jika gcd(a, m) != 1
    
    # Extended Euclidean Algorithm
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd_val, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd_val, x, y
    
    gcd_val, x, y = extended_gcd(a, m)
    return (x % m + m) % m

def is_valid_key(a, m=26):
    """Mengecek apakah kunci 'a' valid untuk Affine Cipher (gcd(a, 26) = 1)"""
    return gcd(a, m) == 1

def affine_encrypt(plaintext, a, b):
    """
    Enkripsi menggunakan Affine Cipher
    Formula: C = (a * P + b) mod 26
    
    Args:
        plaintext (str): Teks yang akan dienkripsi
        a (int): Kunci multiplicative (harus coprime dengan 26)
        b (int): Kunci additive
    
    Returns:
        str: Ciphertext hasil enkripsi
    """
    if not is_valid_key(a):
        raise ValueError(f"Kunci 'a' = {a} tidak valid. gcd({a}, 26) harus = 1")
    
    ciphertext = ""
    
    for char in plaintext.upper():
        if char.isalpha():
            # Konversi huruf ke angka (A=0, B=1, ..., Z=25)
            p = ord(char) - ord('A')
            # Aplikasikan formula Affine: C = (a * P + b) mod 26
            c = (a * p + b) % 26
            # Konversi kembali ke huruf
            ciphertext += chr(c + ord('A'))
        else:
            # Karakter non-alfabet tidak diubah
            ciphertext += char
    
    return ciphertext

def affine_decrypt(ciphertext, a, b):
    """
    Dekripsi menggunakan Affine Cipher
    Formula: P = a^(-1) * (C - b) mod 26
    
    Args:
        ciphertext (str): Teks yang akan didekripsi
        a (int): Kunci multiplicative (harus coprime dengan 26)
        b (int): Kunci additive
    
    Returns:
        str: Plaintext hasil dekripsi
    """
    if not is_valid_key(a):
        raise ValueError(f"Kunci 'a' = {a} tidak valid. gcd({a}, 26) harus = 1")
    
    # Hitung modular inverse dari a
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        raise ValueError(f"Tidak dapat menghitung inverse dari {a} mod 26")
    
    plaintext = ""
    
    for char in ciphertext.upper():
        if char.isalpha():
            # Konversi huruf ke angka (A=0, B=1, ..., Z=25)
            c = ord(char) - ord('A')
            # Aplikasikan formula dekripsi: P = a^(-1) * (C - b) mod 26
            p = (a_inv * (c - b)) % 26
            # Konversi kembali ke huruf
            plaintext += chr(p + ord('A'))
        else:
            # Karakter non-alfabet tidak diubah
            plaintext += char
    
    return plaintext

def get_valid_keys():
    """Mengembalikan daftar kunci 'a' yang valid untuk Affine Cipher"""
    valid_keys = []
    for i in range(1, 26):
        if is_valid_key(i):
            valid_keys.append(i)
    return valid_keys

def demo_affine_cipher():
    """Demonstrasi penggunaan Affine Cipher"""
    print("=== DEMO AFFINE CIPHER ===")
    print()
    
    # Tampilkan kunci yang valid
    valid_keys = get_valid_keys()
    print(f"Kunci 'a' yang valid (coprime dengan 26): {valid_keys}")
    print()
    
    # Contoh enkripsi dan dekripsi
    plaintext = "HELLO WORLD"
    a = 5  # Kunci multiplicative
    b = 8  # Kunci additive
    
    print(f"Plaintext: {plaintext}")
    print(f"Kunci a: {a}")
    print(f"Kunci b: {b}")
    print()
    
    try:
        # Enkripsi
        ciphertext = affine_encrypt(plaintext, a, b)
        print(f"Ciphertext: {ciphertext}")
        
        # Dekripsi
        decrypted = affine_decrypt(ciphertext, a, b)
        print(f"Decrypted: {decrypted}")
        print()
        
        # Verifikasi
        if plaintext.replace(" ", "") == decrypted.replace(" ", ""):
            print("✓ Dekripsi berhasil!")
        else:
            print("✗ Dekripsi gagal!")
            
    except ValueError as e:
        print(f"Error: {e}")

def interactive_affine():
    """Mode interaktif untuk Affine Cipher"""
    print("=== AFFINE CIPHER INTERAKTIF ===")
    print()
    
    while True:
        print("Pilihan:")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Lihat kunci valid")
        print("4. Keluar")
        
        choice = input("Masukkan pilihan (1-4): ").strip()
        
        if choice == "1":
            plaintext = input("Masukkan plaintext: ").strip()
            try:
                a = int(input("Masukkan kunci a (multiplicative): "))
                b = int(input("Masukkan kunci b (additive): "))
                
                if not is_valid_key(a):
                    print(f"Error: Kunci 'a' = {a} tidak valid. Harus coprime dengan 26.")
                    continue
                
                ciphertext = affine_encrypt(plaintext, a, b)
                print(f"Ciphertext: {ciphertext}")
                
            except ValueError as e:
                print(f"Error: {e}")
            print()
            
        elif choice == "2":
            ciphertext = input("Masukkan ciphertext: ").strip()
            try:
                a = int(input("Masukkan kunci a (multiplicative): "))
                b = int(input("Masukkan kunci b (additive): "))
                
                if not is_valid_key(a):
                    print(f"Error: Kunci 'a' = {a} tidak valid. Harus coprime dengan 26.")
                    continue
                
                plaintext = affine_decrypt(ciphertext, a, b)
                print(f"Plaintext: {plaintext}")
                
            except ValueError as e:
                print(f"Error: {e}")
            print()
            
        elif choice == "3":
            valid_keys = get_valid_keys()
            print(f"Kunci 'a' yang valid: {valid_keys}")
            print(f"Total kunci valid: {len(valid_keys)}")
            print()
            
        elif choice == "4":
            print("Terima kasih!")
            break
            
        else:
            print("Pilihan tidak valid!")
            print()

def brute_force_affine(ciphertext, expected_word=None):
    """
    Memecahkan Affine Cipher dengan brute force
    
    Args:
        ciphertext (str): Teks terenkripsi
        expected_word (str): Kata yang diharapkan muncul dalam plaintext (opsional)
    
    Returns:
        list: Daftar kemungkinan dekripsi dengan kunci yang digunakan
    """
    valid_keys = get_valid_keys()
    results = []
    
    print(f"Mencoba memecahkan: {ciphertext}")
    print("=" * 50)
    
    for a in valid_keys:
        for b in range(26):
            try:
                decrypted = affine_decrypt(ciphertext, a, b)
                
                # Jika ada kata yang diharapkan, cek apakah ada dalam hasil dekripsi
                if expected_word:
                    if expected_word.upper() in decrypted.upper():
                        results.append((a, b, decrypted, True))  # True = cocok dengan expected_word
                        print(f"*** KEMUNGKINAN KUAT *** a={a}, b={b}: {decrypted}")
                    else:
                        results.append((a, b, decrypted, False))
                else:
                    results.append((a, b, decrypted, False))
                    print(f"a={a}, b={b}: {decrypted}")
                    
            except ValueError:
                continue
    
    return results

def demo_brute_force():
    """Demonstrasi brute force attack pada Affine Cipher"""
    print("=== DEMO BRUTE FORCE ATTACK ===")
    print()
    
    # Buat ciphertext dari plaintext yang diketahui
    original_text = "ATTACK AT DAWN"
    a, b = 7, 10
    
    print(f"Plaintext asli: {original_text}")
    print(f"Kunci yang digunakan: a={a}, b={b}")
    
    ciphertext = affine_encrypt(original_text, a, b)
    print(f"Ciphertext: {ciphertext}")
    print()
    
    # Sekarang coba pecahkan tanpa mengetahui kunci
    print("Memecahkan dengan brute force (mencari kata 'ATTACK'):")
    results = brute_force_affine(ciphertext, "ATTACK")
    
    print()
    print(f"Total kemungkinan yang dicoba: {len(results)}")
    
    # Tampilkan hanya yang mengandung kata kunci
    likely_results = [r for r in results if r[3]]  # r[3] adalah flag cocok
    print(f"Kemungkinan yang mengandung 'ATTACK': {len(likely_results)}")

def frequency_analysis(text):
    """
    Analisis frekuensi huruf dalam teks
    
    Args:
        text (str): Teks yang akan dianalisis
    
    Returns:
        dict: Dictionary dengan huruf sebagai key dan frekuensi sebagai value
    """
    # Hitung frekuensi setiap huruf
    freq = {}
    text = text.upper().replace(" ", "")  # Hapus spasi dan ubah ke uppercase
    
    for char in text:
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1
    
    # Urutkan berdasarkan frekuensi (tertinggi ke terendah)
    sorted_freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
    
    return sorted_freq

def print_frequency_analysis(text, title=""):
    """Cetak hasil analisis frekuensi dalam format yang rapi"""
    freq = frequency_analysis(text)
    total_chars = sum(freq.values())
    
    print(f"=== ANALISIS FREKUENSI {title} ===")
    print(f"Total huruf: {total_chars}")
    print()
    print("Huruf | Jumlah | Persentase")
    print("------|--------|----------")
    
    for char, count in freq.items():
        percentage = (count / total_chars) * 100
        print(f"  {char}   |   {count:2d}   |   {percentage:5.1f}%")
    print()

def demo_frequency_analysis():
    """Demonstrasi analisis frekuensi pada Affine Cipher"""
    print("=== DEMO ANALISIS FREKUENSI ===")
    print()
    
    # Teks contoh yang cukup panjang
    plaintext = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
    a, b = 5, 12
    
    print(f"Plaintext: {plaintext}")
    print(f"Kunci: a={a}, b={b}")
    
    ciphertext = affine_encrypt(plaintext, a, b)
    print(f"Ciphertext: {ciphertext}")
    print()
    
    # Analisis frekuensi plaintext vs ciphertext
    print_frequency_analysis(plaintext, "PLAINTEXT")
    print_frequency_analysis(ciphertext, "CIPHERTEXT")
    
    print("CATATAN:")
    print("- Pola frekuensi tetap sama, hanya huruf yang berubah")
    print("- Ini menunjukkan kelemahan substitusi monoalfabetik")
    print("- Huruf yang paling sering muncul di plaintext tetap paling sering di ciphertext")

if __name__ == "__main__":
    # Jalankan demo
    demo_affine_cipher()
    print()
    
    # Demo brute force
    demo_brute_force()
    print()
    
    # Demo analisis frekuensi
    demo_frequency_analysis()
    print()
    
    # Jalankan mode interaktif
    interactive_affine()
