import random

pilihan = ["gunting", "batu", "kertas"]

while True:
    komputer = random.choice(pilihan)
    player = input("Pilih gunting, batu, atau kertas: ").lower()

    if player not in pilihan:
        print("Pilihan tidak valid.")
        continue

    print("Komputer memilih:", komputer)

    if player == komputer:
        print("Seri!")
    elif (player == "gunting" and komputer == "batu") or (player == "batu" and komputer == "kertas") or (player == "kertas" and komputer == "gunting"):
        print("Anda kalah!")
    else:
        print("Anda menang!")

    ulang = input("Ingin bermain lagi? (ya/tidak): ").lower()
    if ulang != "ya":
        break

print("Terima kasih telah bermain!")

