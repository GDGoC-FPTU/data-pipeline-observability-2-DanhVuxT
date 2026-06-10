# Experiment Report: Data Quality Impact on AI Agent

**Student ID:** 2A202600606
**Name:** Vu Thanh Danh
**Date:** 2026-06-10

---

## 1. Ket qua thi nghiem

Chay `agent_simulation.py` voi 2 bo du lieu va ghi lai ket qua:

| Scenario | Agent Response | Accuracy (1-10) | Notes |
|----------|----------------|-----------------|-------|
| Clean Data (`processed_data.csv`) | Agent finds the best electronics item from the cleaned dataset and returns a stable answer. | 9/10 | Dữ liệu sạch, giá trị hợp lệ, category chuẩn hóa giúp agent trả lời đúng mục tiêu. |
| Garbage Data (`garbage_data.csv`) | Agent may fail or produce unreliable results because the source contains duplicate IDs, invalid text price, outliers, and missing values. | 3/10 | Dữ liệu rác làm giảm độ tin cậy của phản hồi và dễ gây lỗi trong logic tìm kiếm. |

---

## 2. Phan tich & nhan xet

### Tai sao Agent tra loi sai khi dung Garbage Data?

Khi dữ liệu chứa duplicate ID, wrong data type, outlier và null values, thuật toán của agent không còn dựa trên nền tảng đúng chuẩn nữa. Ví dụ, giá trị 'ten dollars' không phải số nên không thể so sánh hoặc sắp xếp đúng; outlier như 999999 làm cho điểm tốt nhất bị lệch; null values và ID trùng lặp gây nhiễu và làm giảm độ tin cậy của kết quả. Vì vậy, dù prompt có tốt đến đâu, nếu dữ liệu đầu vào bị hỏng thì agent vẫn dễ trả lời sai hoặc thậm chí thất bại hoàn toàn.

---

## 3. Ket luan

**Quality Data > Quality Prompt?** Đồng ý. Chất lượng dữ liệu là nền tảng quan trọng hơn nhiều so với câu prompt. Một prompt tốt chỉ có thể tối ưu hóa cách suy luận, nhưng nếu nguồn dữ liệu đã sai, thiếu hoặc không nhất quán thì kết quả cuối cùng vẫn sẽ bị sai.
