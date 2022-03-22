import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 6))
wedgeprops = {'width':0.3, 'edgecolor':'black', 'linewidth':1}
ax.pie([87,13], wedgeprops=wedgeprops, startangle=90, colors=['#5DADE2', '#515A5A'])
plt.title('MDD', fontsize=24, loc='center')
plt.text(0, 0, "87%", ha='center', va='center', fontsize=42)
fig.savefig("./plot_image/proba.png")
# plt.show()