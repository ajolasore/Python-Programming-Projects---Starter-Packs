giga = int(input("enter the gigabyte: "))
mega = int(input("enter the megabyte: "))
kilo = int(input("enter the kilobyte: "))
byte = int(input("enter the byte: "))

total_bytes = byte + (10**3 * kilo) + (10**6 * mega) + (10**9 * giga)
print (f"{total_bytes}b")

gibibytes = total_bytes // (1024 * 1024 * 1024)
total_bytes %= 1024 * 1024 * 1024
mebibytes = total_bytes // (1024 * 1024)
total_bytes %= 1024 * 1024
kibibytes = total_bytes // 1024
total_bytes %= 1024
byt_e = total_bytes % 1024

print (f"{gibibytes}Gib, {mebibytes}Mib, {kibibytes}Kib, {byt_e}b")
