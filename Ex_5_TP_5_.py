#Ex_5_TP_5_
import numpy as np
import matplotlib.pyplot as plt

# 1. Tableau de données et matrice de covariance
print("1. Matrice de covariance:")
data = np.random.rand(100, 3)  # 100 lignes, 3 colonnes de valeurs aléatoires
cov_matrix = np.cov(data, rowvar=False)  # Calcul de la matrice de covariance
print(cov_matrix)

# 2. Transformation de Fourier sur des données sinusoïdales
print("\n2. Transformation de Fourier:")
# Création d'un signal sinusoïdal
t = np.linspace(0, 1, 1000)
freq = 5  # Fréquence du signal
signal = np.sin(2 * np.pi * freq * t)

# Transformation de Fourier
fourier = np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(signal), d=t[1]-t[0])

# Affichage du spectre de fréquences
plt.figure()
plt.plot(frequencies[:len(frequencies)//2], np.abs(fourier[:len(fourier)//2]))
plt.title("Spectre de fréquences")
plt.xlabel("Fréquence (Hz)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

# 3. Simulation de lancers de dés et histogramme
print("\n3. Histogramme des sommes de dés:")
# Simulation de 1000 lancers de deux dés
dice1 = np.random.randint(1, 7, 1000)
dice2 = np.random.randint(1, 7, 1000)
sums = dice1 + dice2

# Affichage de l'histogramme
plt.figure()
plt.hist(sums, bins=range(2, 14), align='left', rwidth=0.8)
plt.title("Histogramme des sommes de deux dés")
plt.xlabel("Somme des dés")
plt.ylabel("Nombre d'occurrences")
plt.xticks(range(2, 13))
plt.grid(axis='y')
plt.show()