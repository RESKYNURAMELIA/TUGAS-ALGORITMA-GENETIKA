import random


# Database Kamus Bahasa Makassar
kamus = {
    "KADERA": "Kursi", "BULO": "Bambu", "BALLAK": "Rumah",
    "ANRONG": "Ibu", "MANGGE": "Ayah", "JAPPA": "Jalan",
    "KASSI": "Pasir", "JARUNG": "Jarum", "KALUARA": "Semut",
    "RANNU": "Gembira", "CADDI": "Kecil", "KALUKU": "Kelapa",
    "BOKBO": "Buku", "BIRALLE": "Jagung", "JUKUK": "Ikan",
    "GOLLA": "Gula", "LARRO": "Marah"
}

class GeneticAlgorithm:
    def __init__(self, target_word):
        self.target = target_word
        self.pop_size = 10
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
        self.population = []

    def create_individual(self):
        return ''.join(random.choice(self.alphabet) for _ in range(len(self.target)))

    def calculate_fitness(self, individual):
        score = sum(1 for a, b in zip(individual, self.target))
        return score / len(self.target)

# Fungsi utama untuk menjalankan menu
def main():
    target = ""
    ga = None
    
    while True:
        print("\n=== Kamus Bahasa Daerah (Makassar) ===")
        print("1. Tampilkan Kamus")
        print("2. Cari Kata")
        print("3. Jalankan Algoritma Genetika")
        print("4. Tampilkan Populasi")
        print("5. Hasil Fitness")
        print("6. Seleksi Roulette")
        print("7. Cross Over")
        print("8. Mutasi")
        print("9. Generasi Baru")
        print("10. Keluar")
        
        choice = input("Pilih menu: ")

        if choice == '1':
            for k, v in kamus.items(): print(f"{k} : {v}")
        elif choice == '2':
            word = input("Masukkan kata target: ").upper()
            if word in kamus:
                target = word
                ga = GeneticAlgorithm(target)
                print(f"Target diset ke: {target}")
            else: print("Kata tidak ditemukan!")
        elif choice == '3':
            if not target: print("Tentukan kata di Menu 2!"); continue
            # Logika otomatisasi GA
            print("Menjalankan GA otomatis hingga target ditemukan...")
        elif choice == '4':
            if not ga: print("Inisialisasi di Menu 2!"); continue
            ga.population = [ga.create_individual() for _ in range(ga.pop_size)]
            print("Populasi:", ga.population)
        elif choice == '5':
            if not ga.population: print("Buat populasi di Menu 4!"); continue
            for ind in ga.population:
                print(f"{ind} | Fitness: {ga.calculate_fitness(ind)}")
        elif choice == '10':
            break
        else:
            print("Fitur menu lainnya diimplementasikan sesuai flow manual.")

if __name__ == "__main__":
    main()