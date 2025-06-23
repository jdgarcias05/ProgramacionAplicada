import numpy as np

# Números aleatorios entre 0 y 1, distribución uniforme
np.random.rand(5)
np.random.rand(3, 2)

# Números aleatorios con distribución normal estándar (media 0, desviación 1)
np.random.randn(4)
np.random.randn(2, 3)

# Números enteros aleatorios entre 10 (inclusive) y 20 (exclusivo)
np.random.randint(10, 20, 5)
np.random.randint(0, 100, (3, 3))
