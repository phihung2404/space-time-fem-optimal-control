import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Đường dẫn dựa trên vị trí file .py, không phụ thuộc cwd
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / '../results/optimal_control_convergence.dat'
OUTPUT_FILE = BASE_DIR / '../results/optimal_control_convergence.png'

GAMMA_TARGET = 1e-5

# Cột trong .dat: Gamma, N, ||u-uh||Y, EOC_u, ||p-ph||Y, EOC_p, totalError, EOC_total
# totalError = sqrt(gamma * ||u-uh||_Y^2 + ||p-ph||_Y^2), khớp optimal_control_convergence.edp
data = np.loadtxt(DATA_FILE, skiprows=1)

mask = np.abs(data[:, 0] - GAMMA_TARGET) < 1e-10
data = data[mask]

if data.size == 0:
    raise ValueError(f'Không có dữ liệu cho gamma = {GAMMA_TARGET:g}')

gamma, n, state_error, _, adjoint_error, _, total_error, _ = data.T

h = 1.0 / n
reference = (h / h[0]) * total_error[0]  # O(h) tham chiếu, neo theo total_error

plt.figure(figsize=(7, 5))
plt.loglog(n, state_error, 'o-', markersize=6, label=r'$\|u-u_h\|_Y$')
plt.loglog(n, adjoint_error, 's-', markersize=6, label=r'$\|p-p_h\|_Y$')
plt.loglog(n, total_error, '^-', markersize=6, label='Total error')
plt.loglog(n, reference, 'k--', linewidth=1.5, label=r'$\mathcal{O}(h)$')

plt.xlabel(r'$N$')
plt.ylabel('Error')
plt.title(rf'Optimal control convergence ($\gamma={GAMMA_TARGET:g}$)')
plt.legend()
plt.grid(True, which='both', linestyle='--', alpha=0.6)
plt.xticks(n, labels=[f'$2^{{{int(np.log2(v))}}}$' for v in n])

plt.savefig(OUTPUT_FILE, dpi=300, bbox_inches='tight')
plt.show()