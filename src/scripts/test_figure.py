
# Ensure ~/bin is in the PATH so matplotlib can find latex
import os
from pathlib import Path
os.environ["PATH"] += os.pathsep + str(Path.home() / "bin")

import matplotlib.pyplot as plt
import paths
plt.rcParams.update({"text.usetex": True})
fig = plt.figure(figsize=(7, 6))
plt.plot([0, 1], [0, 1])
plt.xlabel(r'$\alpha \beta \frac{1}{2} \exp{-x^2}$')
fig.savefig(paths.figures / 'test_figure.pdf', bbox_inches='tight')

