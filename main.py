def get_full_name():
    first_name = input("Bitte geben Sie Ihren Vornamen ein: ")
    last_name = input("Bitte geben Sie Ihren Nachnamen ein: ")
    return first_name + " " + last_name

# Rufen Sie die Funktion hier auf und drucken Sie das Ergebnis
full_name = get_full_name()
print(full_name)
