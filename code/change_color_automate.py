from Leds import Leds
import time
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.248.150", username="user", password="password")

# Kombinacja, od której chcemy zacząć
start_combination = [0, 0, 1, 2, 2, 2, 0, 2]

n=8
colors = [0, 0, 1, 2, 2, 2, 0, 2]
black = [4,4,4,4,4,4,4,4]

leds = Leds()

# Funkcja do przeliczania kombinacji na numer iteracji (indeks)
def combination_to_index(combination, max_value):
    index = 0
    for value in combination:
        index = index * max_value + value
    return index
# Maksymalna wartość dla każdego miejsca (0, 1, 2)
max_value = 3

# Obliczamy indeks startowy
start_index = combination_to_index(start_combination, max_value)

# Tablica przechowująca bieżącą kombinację
table = start_combination[:]

# Liczba wszystkich kombinacji
total_combinations = max_value ** n

for _ in range(start_index, total_combinations):
    # Wypisanie bieżącej kombinacji
    #print(colors)
    leds.set_leds(colors)
    time.sleep(1)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("sudo /home/user/VisionSystemRaspberryPi/code/VENV/bin/python3 /home/user/VisionSystemRaspberryPi/code/take_photo.py " + str(colors[0])+str(colors[1])+str(colors[2])+str(colors[3])+str(colors[4])+str(colors[5])+str(colors[6])+str(colors[7]))
    time.sleep(5)

    # Aktualizacja tabeli jak licznik w systemie trójkowym
    for i in range(n - 1, -1, -1):
        colors[i] += 1  # Zwiększamy wartość w aktualnym miejscu
        if colors[i] < max_value:
            break  # Nie ma przeniesienia, zakończ
        colors[i] = 0  # Resetujemy miejsce i przenosimy dalej
