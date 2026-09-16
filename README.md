# Space-Time FEM for Optimal Control of Advection-Diffusion Equations

Đồ án tốt nghiệp — repo code kèm theo.

Repo chứa các thí nghiệm kiểm chứng số cho phương pháp phần tử hữu hạn không-thời gian (Petrov-Galerkin), áp dụng cho phương trình advection-diffusion và bài toán điều khiển tối ưu.

Có hai nghiên cứu hội tụ: một cho phương trình trạng thái và một cho bài toán điều khiển tối ưu. Code được viết bằng FreeFEM++, kết quả được xử lý và vẽ bằng Python.


## Yêu cầu

- [FreeFEM++](https://freefem.org/) v4.14 — để chạy các file `.edp`
- Python >= 3.9, cài package qua:
  ```
  pip install -r requirements.txt
  ```

## Cấu trúc thư mục

```
state/
    state_convergence.edp                  # nghiên cứu hội tụ cho phương trình trạng thái
optimal_control/
    optimal_control_convergence.edp        # nghiên cứu hội tụ cho bài toán điều khiển tối ưu
scripts/
    plot_state_convergence.py              # vẽ kết quả từ state/
    plot_optimal_control_convergence.py    # vẽ kết quả từ optimal_control/
results/
    state_convergence.dat / .png
    optimal_control_convergence.dat / .png
```

## Cách chạy

Chạy từng file `.edp` từ chính thư mục chứa nó (đường dẫn trong script là tương đối theo đó):

```
cd state
FreeFem++ state_convergence.edp

cd ../optimal_control
FreeFem++ optimal_control_convergence.edp
```

Mỗi lần chạy sẽ ghi file `.dat` vào `results/`. Sau đó vẽ hình:

```
cd ../scripts
python plot_state_convergence.py
python plot_optimal_control_convergence.py
```

Mỗi script vẽ sẽ ghi file `.png` vào `results/` và hiển thị luôn.

## Định dạng file kết quả

**`state_convergence.dat`** — các cột: `N`, `h`, `||u-uh||_Y`, `EOC`

**`optimal_control_convergence.dat`** — các cột: `Gamma`, `N`, `||u-uh||_Y`, `EOC_u`, `||p-ph||_Y`, `EOC_p`, `totalError`, `EOC_total`,
trong đó `totalError = sqrt(gamma * ||u-uh||_Y^2 + ||p-ph||_Y^2)`.
