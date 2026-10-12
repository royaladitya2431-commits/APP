
import numpy as np

# 1. Create 10 random heart rates between 82 and 149
arr = np.random.randint(82, 150, 10)

print("Heart Rate:", arr)

# 2. Get first 5 minutes
print("First 5 minutes:", arr[:5])

# 3. Find maximum, minimum and average
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Average:", np.mean(arr))

# 4. Find minutes where heart rate exceeded 120
minutes = np.where(arr > 120)[0] + 1

print("Minutes above 120 bpm:", minutes)
