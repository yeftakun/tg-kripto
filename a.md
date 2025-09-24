# Laporan Implementasi Affine Cipher

**Nama:** [Nama Mahasiswa]  
**NIM:** [NIM Mahasiswa]  
**Mata Kuliah:** Kriptografi  
**Topik:** Implementasi Affine Cipher dalam Python

---

## 1. Pendahuluan

Yang terhormat Bapak/Ibu Dosen, saya akan mendemonstrasikan implementasi algoritma **Affine Cipher** yang telah saya buat dalam bahasa Python. Affine Cipher adalah salah satu algoritma kriptografi klasik yang menggunakan transformasi linear untuk proses enkripsi dan dekripsi.

### Formula Matematis:
- **Enkripsi:** `C = (a × P + b) mod 26`
- **Dekripsi:** `P = a⁻¹ × (C - b) mod 26`

Dimana:
- `P` = nilai numerik plaintext (A=0, B=1, ..., Z=25)
- `C` = nilai numerik ciphertext
- `a` = kunci multiplicative (harus coprime dengan 26)
- `b` = kunci additive (0-25)
- `a⁻¹` = modular inverse dari a modulo 26

---

## 2. Struktur Program

Program yang saya buat memiliki beberapa fungsi utama:

### 2.1 Fungsi Matematika Dasar

```python
def gcd(a, b):
    """Menghitung Greatest Common Divisor"""
```
Fungsi ini menggunakan algoritma Euclidean untuk menghitung GCD, yang diperlukan untuk validasi kunci.

```python
def mod_inverse(a, m=26):
    """Menghitung modular inverse dari a mod m"""
```
Fungsi ini mencari modular inverse dengan metode brute force, mencoba semua kemungkinan dari 1 hingga m-1.

```python
def is_valid_key(a):
    """Cek apakah kunci 'a' valid (coprime dengan 26)"""
```
Validasi kunci sangat penting karena hanya kunci yang coprime dengan 26 yang memiliki modular inverse.

### 2.2 Fungsi Enkripsi dan Dekripsi

Program memiliki dua fungsi utama untuk proses kriptografi:
- `affine_encrypt(text, a, b)` - untuk enkripsi
- `affine_decrypt(text, a, b)` - untuk dekripsi

---

## 3. Demonstrasi Program

Sekarang saya akan menjalankan program untuk menunjukkan cara kerjanya:

### 3.1 Menjalankan Program

```bash
python main.py
```

**Output yang dihasilkan:**

```
=== AFFINE CIPHER SEDERHANA ===
Kunci 'a' yang valid: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25

Plaintext: HELLO WORLD
Kunci a: 5, b: 8

Hasil Enkripsi: RCLLA OAPLX
Hasil Dekripsi: HELLO WORLD
✓ Enkripsi dan dekripsi berhasil!

=== MODE INTERAKTIF ===

Pilihan:
1. Enkripsi
2. Dekripsi
3. Keluar
Masukkan pilihan (1-3):
```

### 3.2 Penjelasan Output Awal

Program pertama menampilkan daftar kunci `a` yang valid. Ini penting karena tidak semua angka 1-25 bisa digunakan sebagai kunci multiplicative.

**Mengapa hanya 12 kunci yang valid?**
- Angka 26 = 2 × 13
- Kunci `a` harus coprime dengan 26, artinya gcd(a, 26) = 1
- Jadi `a` tidak boleh memiliki faktor 2 atau 13
- Yang valid: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25

Program kemudian melakukan demo otomatis dengan:
- Plaintext: "HELLO WORLD"
- Kunci a = 5, b = 8

### 3.3 Proses Enkripsi Manual

Mari saya tunjukkan perhitungan manual untuk huruf pertama "H":

1. H = 7 (dalam sistem A=0, B=1, ..., Z=25)
2. C = (5 × 7 + 8) mod 26 = (35 + 8) mod 26 = 43 mod 26 = 17
3. 17 = R

Sehingga "H" dienkripsi menjadi "R". Proses ini diulang untuk setiap huruf.

### 3.4 Demonstrasi Mode Interaktif

#### Pengujian Enkripsi

Saya akan memilih opsi 1 (Enkripsi) dan mencoba dengan teks "MATEMATIKA":

```
Masukkan pilihan (1-3): 1
Masukkan teks untuk dienkripsi: MATEMATIKA
Masukkan kunci a: 7
Masukkan kunci b: 3
Hasil enkripsi: JDGFJDGHVD
```

#### Pengujian Dekripsi

Sekarang saya akan mendekripsi hasil tersebut:

```
Masukkan pilihan (1-3): 2
Masukkan teks untuk didekripsi: JDGFJDGHVD
Masukkan kunci a: 7
Masukkan kunci b: 3
Hasil dekripsi: MATEMATIKA
```

**Penjelasan Proses Dekripsi:**
1. Pertama, program menghitung modular inverse dari a=7 mod 26
2. Inverse dari 7 adalah 15 (karena 7 × 15 = 105 ≡ 1 mod 26)
3. Untuk setiap huruf cipher, gunakan formula: P = 15 × (C - 3) mod 26

#### Pengujian Error Handling

Mari saya coba dengan kunci yang tidak valid:

```
Masukkan pilihan (1-3): 1
Masukkan teks untuk dienkripsi: TEST
Masukkan kunci a: 4
Masukkan kunci b: 5
Error: Kunci a=4 tidak valid!
```

Program dengan benar menolak kunci a=4 karena gcd(4, 26) = 2 ≠ 1.

---

## 4. Analisis Keamanan

### 4.1 Kekuatan Affine Cipher

1. **Ruang Kunci:** 12 × 26 = 312 kemungkinan kunci
2. **Transformasi Linear:** Memberikan distribusi yang berbeda dari Caesar Cipher

### 4.2 Kelemahan Affine Cipher

1. **Ruang kunci terbatas:** Hanya 312 kemungkinan, mudah untuk brute force
2. **Substitusi monoalfabetik:** Masih rentan terhadap analisis frekuensi
3. **Pola terjaga:** Huruf yang sama selalu dienkripsi menjadi huruf yang sama

### 4.3 Demonstrasi Kelemahan

Mari saya tunjukkan dengan teks yang memiliki huruf berulang:

```
Masukkan pilihan (1-3): 1
Masukkan teks untuk dienkripsi: HELLO HELLO
Masukkan kunci a: 5
Masukkan kunci b: 8
Hasil enkripsi: RCLLA RCLLA
```

Perhatikan bahwa pola "HELLO" yang berulang menghasilkan pola "RCLLA" yang sama, menunjukkan kelemahan substitusi monoalfabetik.

---

## 5. Implementasi Teknis

### 5.1 Penanganan Karakter Non-Alfabet

Program saya menangani spasi dan karakter khusus dengan mempertahankan posisinya:

```
Masukkan pilihan (1-3): 1
Masukkan teks untuk dienkripsi: HELLO, WORLD!
Masukkan kunci a: 5
Masukkan kunci b: 8
Hasil enkripsi: RCLLA, OAPLX!
```

### 5.2 Konversi Case

Program secara otomatis mengkonversi input ke huruf kapital untuk konsistensi.

### 5.3 Validasi Input

Program memiliki error handling yang robust:
- Validasi kunci multiplicative
- Penanganan input non-numerik
- Pengecekan modular inverse

---

## 6. Kesimpulan

Pak/Bu Dosen, dari demonstrasi ini dapat disimpulkan:

1. **Implementasi Berhasil:** Program dapat melakukan enkripsi dan dekripsi dengan benar
2. **Validasi Matematis:** Semua operasi modular dan inverse berjalan sesuai teori
3. **Error Handling:** Program menangani input invalid dengan baik
4. **User Interface:** Interface sederhana dan intuitif

### 6.1 Pembelajaran yang Diperoleh

1. **Pentingnya Validasi Kunci:** GCD dan coprimality sangat krusial
2. **Modular Arithmetic:** Operasi modulo 26 untuk alphabet mapping
3. **Kelemahan Klasik:** Affine Cipher rentan untuk teks panjang

### 6.2 Contoh Hasil Pengujian Aktual

Berikut adalah hasil pengujian yang saya lakukan:

| Input | Kunci (a,b) | Output | Verifikasi |
|-------|-------------|---------|------------|
| MATEMATIKA | (7,3) | JDGFJDGHVD | ✓ Berhasil |
| HELLO HELLO | (5,8) | RCLLA RCLLA | ✓ Pola terlihat |
| HELLO, WORLD! | (5,8) | RCLLA, OAPLX! | ✓ Tanda baca dipertahankan |
| TEST | (4,5) | Error | ✓ Kunci invalid ditolak |

### 6.3 Pengembangan Selanjutnya

Untuk meningkatkan keamanan, bisa dikombinasikan dengan:

- Transposisi cipher (mengacak posisi huruf)
- Polyalphabetic substitution (kunci berubah per huruf)
- Block cipher modes (enkripsi per blok)

---

## 7. Analisis Kompleksitas

### 7.1 Kompleksitas Waktu

- **Enkripsi/Dekripsi:** O(n) dimana n = panjang teks
- **Pencarian Modular Inverse:** O(m) dimana m = 26
- **Validasi GCD:** O(log min(a,b))

### 7.2 Kompleksitas Ruang

- **Memori:** O(n) untuk menyimpan hasil
- **Variabel tambahan:** O(1)

---

## 8. Referensi Kode

Program lengkap tersedia di file `main.py` dengan struktur yang modular dan dokumentasi yang jelas. Setiap fungsi memiliki docstring dan komentar untuk memudahkan pemahaman.

### 8.1 Struktur File

```text
main.py
├── gcd(a, b)              # Fungsi matematis dasar
├── mod_inverse(a, m=26)   # Pencarian modular inverse
├── is_valid_key(a)        # Validasi kunci
├── affine_encrypt(text, a, b)  # Fungsi enkripsi
├── affine_decrypt(text, a, b)  # Fungsi dekripsi
└── main()                 # Program utama
```

### 8.2 Fitur Program

- ✅ Enkripsi dan dekripsi yang akurat
- ✅ Validasi kunci otomatis
- ✅ Error handling yang robust
- ✅ Interface yang user-friendly
- ✅ Penanganan karakter non-alfabet
- ✅ Konversi case otomatis

**Terima kasih atas perhatian Bapak/Ibu Dosen. Saya siap menjawab pertanyaan terkait implementasi ini.**

---

*Catatan: Demonstrasi ini menunjukkan pemahaman teoritis dan praktis tentang Affine Cipher, termasuk aspek matematis, implementasi, dan analisis keamanannya. Program telah diuji dengan berbagai kasus dan menunjukkan hasil yang konsisten dengan teori kriptografi.*