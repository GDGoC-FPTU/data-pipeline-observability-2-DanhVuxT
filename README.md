[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=24112859&assignment_repo_type=AssignmentRepo)
# Day 10 Lab: Data Pipeline & Data Observability

**Student Email:** vudanh1107@gmail.com
**Name:** Vu Thanh Danh

---

## Mo ta

Bài lab này xây dựng một pipeline ETL đơn giản bằng Python và pandas để đọc dữ liệu JSON, loại bỏ bản ghi không hợp lệ, chuẩn hóa category, tính giá sau khi giảm 10% và xuất ra file CSV. Tôi cũng thực hiện kiểm tra observability bằng cách in ra số bản ghi được giữ và bị loại bỏ để dễ theo dõi quá trình xử lý.

---

## Cach chay (How to Run)

### Prerequisites
```bash
pip install pandas
```

### Chay ETL Pipeline
```bash
python solution.py
```

### Chay Agent Simulation (Stress Test)
```bash
python generate_garbage.py
python agent_simulation.py
```

---

## Cau truc thu muc

```
├── solution.py              # ETL Pipeline script
├── processed_data.csv       # Output cua pipeline
├── experiment_report.md     # Bao cao thi nghiem
└── README.md                # File nay
```

---

## Ket qua

Pipeline xử lý 5 bản ghi đầu vào, loại bỏ các bản ghi có giá <= 0 hoặc category rỗng, sau đó tạo file `processed_data.csv` với các cột `discounted_price` và `processed_at`. Kết quả cho thấy workflow ETL đã hoạt động ổn định và có thể dùng làm nền tảng cho các bài kiểm thử observability tiếp theo.
