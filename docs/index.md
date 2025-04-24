---
title: Hồi quy Logistic và Toán học của nó
layout: default
nav_order: 5
math: katex # Đảm bảo cài đặt này để bật render công thức toán
---

# Hồi quy Logistic

Hồi quy Logistic (Logistic Regression) là một thuật toán cơ bản trong học máy được sử dụng cho các bài toán phân loại nhị phân. Mặc dù có tên là "Hồi quy", đây là một thuật toán phân loại chứ không phải hồi quy. Nó mô hình hóa xác suất một đầu vào nhất định thuộc về một danh mục cụ thể (thường là lớp dương tính).

## Hàm Sigmoid

Trọng tâm của Hồi quy Logistic là **hàm sigmoid** (còn được gọi là hàm logistic). Hàm này lấy bất kỳ số thực nào và ánh xạ nó tới một giá trị nằm giữa 0 và 1. Điều này làm cho nó lý tưởng để biểu diễn xác suất.

Hàm sigmoid, ký hiệu là $\sigma(z)$, được định nghĩa như sau:

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

Trong đó, $z$ là sự kết hợp tuyến tính của các đặc trưng đầu vào, các trọng số và hệ số chệch của mô hình:

$$
z = \mathbf{w}^T \mathbf{x} + b
$$

Trong đó:
*   $$\mathbf{w}$$ là vector trọng số.
*   $$\mathbf{x}$$ là vector đặc trưng đầu vào.
*   $$b$$ là hệ số chệch (bias term).
*   $$\mathbf{w}^T \mathbf{x}$$ là tích vô hướng của trọng số và đặc trưng.

Đầu ra của hàm sigmoid, $$\sigma(z)$$, được hiểu là xác suất mà trường hợp $$\mathbf{x}$$ thuộc về lớp dương tính (lớp 1). Chúng ta có thể biểu diễn xác suất dự đoán là:

$$
P(y=1 | \mathbf{x}; \mathbf{w}, b) = \sigma(\mathbf{w}^T \mathbf{x} + b)
$$

và xác suất của lớp âm tính (lớp 0) là:

$$
P(y=0 | \mathbf{x}; \mathbf{w}, b) = 1 - \sigma(\mathbf{w}^T \mathbf{x} + b)
$$

## Hàm Chi phí (Hàm Mất mát)

Để huấn luyện một mô hình Hồi quy Logistic, chúng ta cần một hàm chi phí đo lường mức độ phù hợp giữa các dự đoán của chúng ta với nhãn thực tế. Đối với phân loại, **cross-entropy** (hay log loss) thường được sử dụng. Nó phạt nặng mô hình khi nó tự tin vào một dự đoán sai.

Đối với một mẫu huấn luyện đơn lẻ $$(\mathbf{x}^{(i)}, y^{(i)})$$, trong đó $$y^{(i)}$$ là nhãn thực tế (0 hoặc 1), mất mát là:

$$
L(\hat{y}^{(i)}, y^{(i)}) = - y^{(i)} \log(\hat{y}^{(i)}) - (1 - y^{(i)}) \log(1 - \hat{y}^{(i)})
$$

Ở đây, $$\hat{y}^{(i)}$$ là xác suất dự đoán cho mẫu thứ $$i$$: $$\hat{y}^{(i)} = \sigma(\mathbf{w}^T \mathbf{x}^{(i)} + b)$$.

Tổng chi phí $$J(\mathbf{w}, b)$$ trên tất cả $$m$$ mẫu huấn luyện là trung bình cộng của các mất mát cá nhân:

$$
J(\mathbf{w}, b) = - \frac{1}{m} \sum_{i=1}^{m} \left[ y^{(i)} \log(\hat{y}^{(i)}) + (1 - y^{(i)}) \log(1 - \hat{y}^{(i)}) \right]
$$

Mục tiêu của chúng ta trong quá trình huấn luyện là tìm ra các giá trị của $$\mathbf{w}$$ và $$b$$ sao cho hàm chi phí này được cực tiểu hóa.

## Gradient Descent

Để cực tiểu hóa hàm chi phí $$J(\mathbf{w}, b)$$, chúng ta thường sử dụng thuật toán tối ưu hóa như **gradient descent** (giảm gradient). Gradient descent cập nhật lặp lại các trọng số và hệ số chệch theo hướng làm giảm chi phí mạnh nhất.

Công thức cập nhật cho một trọng số $$w_j$$ và hệ số chệch $$b$$ là:

$$
w_j := w_j - \alpha \frac{\partial J}{\partial w_j}
$$

$$
b := b - \alpha \frac{\partial J}{\partial b}
$$

Trong đó $$\alpha$$ là tốc độ học (learning rate), kiểm soát kích thước của các bước nhảy.

Các đạo hàm riêng của hàm chi phí đối với trọng số và hệ số chệch là:

$$
\frac{\partial J}{\partial w_j} = \frac{1}{m} \sum_{i=1}^{m} (\hat{y}^{(i)} - y^{(i)}) x_j^{(i)}
$$

$$
\frac{\partial J}{\partial b} = \frac{1}{m} \sum_{i=1}^{m} (\hat{y}^{(i)} - y^{(i)})
$$

Các đạo hàm này chỉ ra hướng tăng mạnh nhất của hàm chi phí. Bằng cách trừ chúng đi (hoặc cộng với giá trị âm của chúng), chúng ta di chuyển về phía điểm cực tiểu. Thành phần $$(\hat{y}^{(i)} - y^{(i)})$$ là sự khác biệt giữa xác suất dự đoán và nhãn thực tế, biểu thị lỗi cho mỗi mẫu.

## Tóm tắt

Hồi quy Logistic, được hỗ trợ bởi hàm sigmoid, hàm chi phí cross-entropy và gradient descent, cung cấp một khuôn khổ đơn giản nhưng mạnh mẽ cho bài toán phân loại nhị phân. Hiểu biết về cơ sở toán học của nó là rất quan trọng để áp dụng và diễn giải mô hình một cách hiệu quả.