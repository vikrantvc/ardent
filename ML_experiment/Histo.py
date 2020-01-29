import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [1,2,3,4,5,6,7,8,9,10,20]
plt.hist(x, bins = [1,5,10,20],rwidth=0.8)

# import matplotlib.pyplot as plt
# blood_sugar = [113, 85, 90, 150, 149, 88, 93, 115, 135, 80, 77, 82, 129]
# plt.hist(blood_sugar, rwidth=0.8)
plt.show()
