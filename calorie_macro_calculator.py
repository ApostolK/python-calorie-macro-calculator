
def bmr_szamitas(nem, suly, magassag, kor):
    if nem.lower() == "férfi":
        bmr = 88.362 + (13.397 * suly) + (4.799 * magassag) - (5.677 * kor)
    else:
        bmr = 447.593 + (9.247 * suly) + (3.098 * magassag) - (4.330 * kor)
    return round(bmr, 2)

def napi_kaloria_szukseglet(bmr, aktivitas_szint):
    szorzok = {
        "ulomunka": 1.2,
        "enyhe": 1.375,
        "kozepes": 1.55,
        "aktiv": 1.725,
        "nagyon_aktiv": 1.9
    }
    szorzo = szorzok.get(aktivitas_szint, 1.2)
    return round(bmr * szorzo, 2)

def makrotapanyag_szamitas(kaloria):
    szenhidrat_kcal = kaloria * 0.55
    feherje_kcal = kaloria * 0.15
    zsir_kcal = kaloria * 0.30

    szenhidrat_g = szenhidrat_kcal / 4
    feherje_g = feherje_kcal / 4
    zsir_g = zsir_kcal / 9

    return {
        "Szénhidrát (g)": round(szenhidrat_g, 2),
        "Fehérje (g)": round(feherje_g, 2),
        "Zsír (g)": round(zsir_g, 2)
    }

# --- Főprogram ---
print("Kalóriaszükséglet és makrotápanyag kalkulátor")
print("-------------------------------------------")

nem = input("Add meg a nemed (férfi/nő): ")
suly = float(input("Add meg a súlyod (kg): "))
magassag = float(input("Add meg a magasságod (cm): "))
kor = int(input("Add meg az életkorod (év): "))

print("\nAktivitási szintek: ulomunka, enyhe, kozepes, aktiv, nagyon_aktiv")
aktivitas_szint = input("Add meg az aktivitási szinted: ")

# Számítások
bmr = bmr_szamitas(nem, suly, magassag, kor)
fenntartasi_kaloria = napi_kaloria_szukseglet(bmr, aktivitas_szint)
makrok = makrotapanyag_szamitas(fenntartasi_kaloria)

# Eredmények kiírása
print("\n--- EREDMÉNYEK ---")
print(f"BMR (Alapanyagcsere): {bmr} kcal/nap")
print(f"Napi kalóriaszükséglet: {fenntartasi_kaloria} kcal/nap")
print("\nMakrotápanyag eloszlás:")
for nev, ertek in makrok.items():
    print(f"  {nev}: {ertek} g")
