def adalah_prima(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

# --- TAMBAHKAN KODE DI BAWAH INI ---
print(adalah_prima(11))  # Output yang benar: True
print(adalah_prima(15))  # Output yang benar: False
print(adalah_prima(2))   # Output yang benar: True