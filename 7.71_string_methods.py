all_low = "there are no capitals here."
print(all_low.upper())  # metoda upper powoduje że wszystkie litery są duże
print(all_low)          # metody nie zmieniają oryginalnego stringa

all_up = "THIS IS SHOUTING TEXT!"
print(all_up.lower())   # metoda lower powoduje że litery są małe

print("Mixed Case".isupper())  # metoda sprawdza czy w stringu są same duże litery i zwraca True lub False
print("ALL CAPS".isupper())

print("AAAHHH!".islower())
print("testtesttest=1".islower())

print("".isupper())
print("37&8.,?\"".islower())


print("SHOUT!".lower().isupper())

# pozostałe metody
# .isalpha()   - tylko litery
# .isalnum()   - tylko cyfry i litery
# .isdecimal() - tylko cyfry
# .isspace()   - tylko spacje
# .istitle()   - tylko stringi gdzie pierwsza litera każdego wyrazu jest pisana dużą literą

print("Batman".isalpha())
print("Batman123".isalpha())

print("Batman123".isalnum())
print("Batman".isalnum())
print("123".isalnum())

print("123".isdecimal())
print("3.14159".isdecimal())

print("  ".isspace())
print("                            ".isspace())
print("not just spaces".isspace())
print("not just spaces"[3].isspace())

print("The Empire Strikes Back".istitle())
print("Super Smash Broters: Ultimate!".istitle())  # działa również ze znakami interpunkcyjnymi i znakami specjalnymi

print("th great gatsby".title())