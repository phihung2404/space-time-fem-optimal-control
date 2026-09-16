import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / '../results/state_convergence.dat'
OUTPUT_FILE = BASE_DIR / '../results/state_convergence.png'

# Offset đường tham chiếu O(h) để tách khỏi dữ liệu khi vẽ (chỉ dịch trục dọc, không đổi độ dốc)
REFERENCE_OFFSET = 2.0

# Cột trong .dat: N, h, ||u-uh||_Y, EOC
data = np.loadtxt(DATA_FILE, skiprows=1)
n, h, error, eoc = data.T

reference = REFERENCE_OFFSET * (h / h[0]) * error[0]

plt.figure(figsize=(7, 5))
plt.loglog(n, error, 'o-', markersize=6, label=r'$\|u-u_h\|_Y$')
plt.loglog(n, reference, 'k--', linewidth=1.5, label=r'$\mathcal{O}(h)$')

plt.xlabel(r'$N$')
plt.ylabel('Error')
plt.title('State equation convergence')
plt.legend()
plt.grid(True, which='both', linestyle='--', alpha=0.6)
plt.xticks(n, labels=[f'$2^{{{int(np.log2(v))}}}$' for v in n])

plt.savefig(OUTPUT_FILE, dpi=300, bbox_inches='tight')
plt.show()