import numpy as np

# Lower and Upper ranges of the HSV colorspace of RED
lower_red = np.array([0, 66, 100])
upper_red = np.array([0, 255, 255])

# Lower and Upper ranges of the HSV colorspace of GREEN
lower_green = np.array([40, 120, 203])
upper_green = np.array([79, 255, 255])

# Lower and Upper ranges of the HSV colorspace of YELLOW
lower_yellow = np.array([21, 121, 172])
upper_yellow = np.array([40, 198, 255])

# Lower and Upper ranges of the HSV colorspace of GRAY
lower_gray = np.array([0, 0, 170])
upper_gray = np.array([0, 255, 243])

# Lower and Upper ranges of the HSV colorspace of MVP
lower_MVP = np.array([49, 156, 83])
upper_MVP = np.array([179, 255, 255])

# Regex pattern
pattern = r'\b[a-zA-Z]+\b(?![^\[]*\])'
