---
title: Vector - Ma trận - Hệ phương trình tuyến tính
layout: default
nav_order: 1 # Thường đặt 1 cho trang chủ để ưu tiên
parent: Các chủ đề
description: Vector-Matrix
math: katex
---
Chào bạn, hành trình của chúng ta bắt đầu từ những viên gạch nhỏ nhất trong đại số tuyến tính: **vector**. Hãy tưởng tượng vector như những mũi tên trong không gian, mang theo cả hướng và độ lớn. Chúng ta có thể kết hợp chúng, kéo dài chúng, thậm chí xoay chúng.

## Vector và Tổ hợp Tuyến tính

Vector là trái tim của đại số tuyến tính. Hãy cùng nhìn vào hai vector đơn giản trong không gian 2 chiều, như được giới thiệu trong tài liệu của chúng ta:

$$ \mathbf{v} = \begin{bmatrix} 2 \\ 4 \end{bmatrix}, \quad \mathbf{w} = \begin{bmatrix} 1 \\ 3 \end{bmatrix} $$

* Vector $$\mathbf{v}$$ có hai thành phần, $$v_1 = 2$$ và $$v_2 = 4$$.
* Vector $$\mathbf{w}$$ cũng ở trong không gian 2 chiều, với thành phần $$w_1 = 1$$ và $$w_2 = 3$$.

Những vector này có thể được kết hợp để tạo ra **tổ hợp tuyến tính**. Một tổ hợp tuyến tính của $$\mathbf{v}$$ và $$\mathbf{w}$$ có dạng $$c\mathbf{v} + d\mathbf{w}$$, trong đó $$c$$ và $$d$$ là những số bất kỳ. Hãy thử một vài giá trị cho $$c$$ và $$d$$:

$$ c\mathbf{v} + d\mathbf{w} = c \begin{bmatrix} 2 \\ 4 \end{bmatrix} + d \begin{bmatrix} 1 \\ 3 \end{bmatrix} = \begin{bmatrix} 2c \\ 4c \end{bmatrix} + \begin{bmatrix} d \\ 3d \end{bmatrix} = \begin{bmatrix} 2c + d \\ 4c + 3d \end{bmatrix} $$

* Nếu $$c=1, d=1$$, ta có $$\mathbf{v} + \mathbf{w} = \begin{bmatrix} 2(1) + 1 \\ 4(1) + 3 \end{bmatrix} = \begin{bmatrix} 3 \\ 7 \end{bmatrix}$$. Đây là vector tổng của $$\mathbf{v}$$ và $$\mathbf{w}$$.
* Nếu $$c=5, d=-2$$, ta có $$5\mathbf{v} - 2\mathbf{w} = 5 \begin{bmatrix} 2 \\ 4 \end{bmatrix} - 2 \begin{bmatrix} 1 \\ 3 \end{bmatrix} = \begin{bmatrix} 10 \\ 20 \end{bmatrix} - \begin{bmatrix} 2 \\ 6 \end{bmatrix} = \begin{bmatrix} 8 \\ 14 \end{bmatrix}$$.

Tổ hợp tuyến tính $$c\mathbf{v} + d\mathbf{w}$$ tạo ra tất cả các vector trong một mặt phẳng (nếu $$\mathbf{v}$$ và $$\mathbf{w}$$ không cùng nằm trên một đường thẳng đi qua gốc tọa độ) hoặc một đường thẳng đi qua gốc tọa độ (nếu chúng cùng nằm trên một đường thẳng).

Câu hỏi quan trọng mà tổ hợp tuyến tính đặt ra là:
* Tất cả các tổ hợp tuyến tính $$c\mathbf{v} + d\mathbf{w}$$ tạo ra gì? Một mặt phẳng hay một đường thẳng?
* Tìm các giá trị $$c$$ và $$d$$ để tạo ra một vector cụ thể $$\begin{bmatrix} 2 \\ 0 \end{bmatrix}$$.

Để trả lời câu hỏi thứ hai, chúng ta cần giải một hệ phương trình tuyến tính:

$$ c \begin{bmatrix} 2 \\ 4 \end{bmatrix} + d \begin{bmatrix} 1 \\ 3 \end{bmatrix} = \begin{bmatrix} 2 \\ 0 \end{bmatrix} $$

Điều này dẫn đến hệ phương trình:
$$ \begin{cases} 2c + d = 2 \\ 4c + 3d = 0 \end{cases} $$

Giải hệ này, ta được $$c = 3$$ và $$d = -4$$.

![Linear Combination](image.png)

## Độ dài và Góc từ Tích vô hướng

Độ dài của một vector và góc giữa hai vector được xác định thông qua **tích vô hướng**. Tích vô hướng của hai vector $$\mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \end{bmatrix}$$ và $$\mathbf{w} = \begin{bmatrix} w_1 \\ w_2 \end{bmatrix}$$ là:

$$ \mathbf{v} \cdot \mathbf{w} = v_1 w_1 + v_2 w_2 $$

Nếu các vector ở trong không gian $$n$$ chiều, tích vô hướng là tổng của tích các thành phần tương ứng:

$$ \mathbf{v} \cdot \mathbf{w} = v_1 w_1 + v_2 w_2 + \dots + v_n w_n $$

Tích vô hướng của một vector với chính nó cho ta bình phương độ dài của vector đó:

$$ \mathbf{v} \cdot \mathbf{v} = v_1^2 + v_2^2 + \dots + v_n^2 = ||\mathbf{v}||^2 $$

Độ dài của vector $$\mathbf{v}$$ là căn bậc hai của tích vô hướng của nó với chính nó:

$$ ||\mathbf{v}|| = \sqrt{\mathbf{v} \cdot \mathbf{v}} $$

Đối với vector $$\mathbf{w} = \begin{bmatrix} 1 \\ 3 \end{bmatrix}$$, bình phương độ dài là $$1^2 + 3^2 = 1 + 9 = 10$$. Độ dài của $$\mathbf{w}$$ là $$||\mathbf{w}|| = \sqrt{10}$$.

Tích vô hướng còn liên quan đến góc giữa hai vector thông qua công thức cosine:

$$ \mathbf{v} \cdot \mathbf{w} = ||\mathbf{v}|| \cdot ||\mathbf{w}|| \cos \theta $$

Trong đó $$\theta$$ là góc giữa $$\mathbf{v}$$ và $$\mathbf{w}$$. Từ đó, ta có:

$$ \cos \theta = \frac{\mathbf{v} \cdot \mathbf{w}}{||\mathbf{v}|| \cdot ||\mathbf{w}||} $$

* Nếu $$\mathbf{v} \cdot \mathbf{w} = 0$$, hai vector $$\mathbf{v}$$ và $$\mathbf{w}$$ vuông góc với nhau ($$\theta = 90^\circ$$ vì $$\cos 90^\circ = 0$$).

Công thức cosine này dẫn đến **Bất đẳng thức Schwarz**:

$$ |\mathbf{v} \cdot \mathbf{w}| \le ||\mathbf{v}|| \cdot ||\mathbf{w}|| $$

Và **Bất đẳng thức Tam giác**:

$$ ||\mathbf{v} + \mathbf{w}|| \le ||\mathbf{v}|| + ||\mathbf{w}|| $$

![Cosine](image-1.png)

## Ma trận và Không gian Cột của chúng

Một **ma trận** là một bảng hình chữ nhật chứa các số. Ma trận có thể được xem như một tập hợp các vector cột hoặc vector hàng. Ví dụ, ma trận $$A$$ chứa hai vector cột $$\mathbf{v}$$ và $$\mathbf{w}$$:

$$ A = \begin{bmatrix} \mathbf{v} & \mathbf{w} \end{bmatrix} = \begin{bmatrix} 2 & 1 \\ 4 & 3 \end{bmatrix} $$

Khi một ma trận nhân với một vector $$\mathbf{x} = \begin{bmatrix} c \\ d \end{bmatrix}$$, kết quả là một tổ hợp tuyến tính của các cột của ma trận đó:

$$ A \mathbf{x} = \begin{bmatrix} 2 & 1 \\ 4 & 3 \end{bmatrix} \begin{bmatrix} c \\ d \end{bmatrix} = c \begin{bmatrix} 2 \\ 4 \end{bmatrix} + d \begin{bmatrix} 1 \\ 3 \end{bmatrix} = c\mathbf{v} + d\mathbf{w} $$

Tập hợp tất cả các tổ hợp tuyến tính của các cột của ma trận $$A$$ được gọi là **không gian cột** của $$A$$, ký hiệu là $$C(A)$$. Không gian cột chứa tất cả các vector $$\mathbf{b}$$ mà phương trình $$A\mathbf{x} = \mathbf{b}$$ có nghiệm.

* Nếu các cột của $$A$$ độc lập tuyến tính, không gian cột của $$A$$ lấp đầy toàn bộ không gian vector mà các cột thuộc về.
* Nếu các cột của $$A$$ phụ thuộc tuyến tính, không gian cột của $$A$$ là một không gian con nhỏ hơn.

Ví dụ:
$$ A_1 = \begin{bmatrix} 1 & 0 & 0 \\ 2 & 4 & 0 \\ 3 & 5 & 6 \end{bmatrix} $$
Các cột của $$A_1$$ độc lập tuyến tính. Không gian cột của $$A_1$$ là toàn bộ không gian $$\mathbb{R}^3$$.

$$ A_2 = \begin{bmatrix} 1 & 2 & 3 \\ 1 & 4 & 5 \\ 6 & 0 & 6 \end{bmatrix} $$
Cột thứ ba của $$A_2$$ là tổng của cột thứ nhất và cột thứ hai ($$ \begin{bmatrix} 3 \\ 5 \\ 6 \end{bmatrix} = \begin{bmatrix} 1 \\ 1 \\ 6 \end{bmatrix} + \begin{bmatrix} 2 \\ 4 \\ 0 \end{bmatrix} $$). Các cột phụ thuộc tuyến tính. Không gian cột của $$A_2$$ là mặt phẳng được tạo bởi hai cột đầu tiên.

$$ A_3 = \begin{bmatrix} 1 & 3 & 4 \\ 2 & 6 & 8 \\ 5 & 15 & 20 \end{bmatrix} $$
Tất cả các cột của $$A_3$$ đều là bội số của cột thứ nhất ($$ \begin{bmatrix} 3 \\ 6 \\ 15 \end{bmatrix} = 3 \begin{bmatrix} 1 \\ 2 \\ 5 \end{bmatrix} $$, $$ \begin{bmatrix} 4 \\ 8 \\ 20 \end{bmatrix} = 4 \begin{bmatrix} 1 \\ 2 \\ 5 \end{bmatrix} $$). Không gian cột của $$A_3$$ là một đường thẳng đi qua gốc tọa độ, chứa tất cả các bội số của vector $$ \begin{bmatrix} 1 \\ 2 \\ 5 \end{bmatrix} $$.

**Hạng (Rank)** của ma trận là số lượng cột độc lập tuyến tính tối đa. Nó cho biết "kích thước thực" của không gian cột. Ma trận $$A_1$$ có hạng 3, $$A_2$$ có hạng 2, và $$A_3$$ có hạng 1.



## Phép nhân Ma trận $$AB$$ và $$CR$$

Phép nhân ma trận $$AB$$ là một trong những phép toán cốt lõi. Để nhân ma trận $$A$$ kích thước $$m \times n$$ với ma trận $$B$$ kích thước $$n \times p$$, số cột của $$A$$ phải bằng số hàng của $$B$$. Kết quả là ma trận $$AB$$ có kích thước $$m \times p$$.

Có nhiều cách để hiểu phép nhân ma trận:
* **Theo hàng và cột:** Phần tử ở hàng $$i$$, cột $$j$$ của $$AB$$ là tích vô hướng của hàng $$i$$ của $$A$$ và cột $$j$$ của $$B$$.
* **Theo cột:** Mỗi cột của $$AB$$ là một tổ hợp tuyến tính của các cột của $$A$$. Cột thứ $$j$$ của $$AB$$ là $$A$$ nhân với cột thứ $$j$$ của $$B$$.
* **Theo hàng:** Mỗi hàng của $$AB$$ là một tổ hợp tuyến tính của các hàng của $$B$$. Hàng thứ $$i$$ của $$AB$$ là hàng thứ $$i$$ của $$A$$ nhân với $$B$$.
* **Theo cột nhân hàng (Outer Product):** Ma trận $$AB$$ có thể được biểu diễn bằng tổng các tích ngoài của các cột của $$A$$ và các hàng của $$B$$.

$$ AB = \mathbf{a}_1 \mathbf{b}_1^T + \mathbf{a}_2 \mathbf{b}_2^T + \dots + \mathbf{a}_n \mathbf{b}_n^T $$
Trong đó $$\mathbf{a}_k$$ là cột thứ $$k$$ của $$A$$ và $$\mathbf{b}_k^T$$ là hàng thứ $$k$$ của $$B$$. Mỗi tích ngoài $$\mathbf{a}_k \mathbf{b}_k^T$$ là một ma trận hạng một.

Ví dụ phép nhân theo hàng và cột:
$$ A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}, \quad B = \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix} $$
$$ AB = \begin{bmatrix} (1)(5)+(2)(7) & (1)(6)+(2)(8) \\ (3)(5)+(4)(7) & (3)(6)+(4)(8) \end{bmatrix} = \begin{bmatrix} 5+14 & 6+16 \\ 15+28 & 18+32 \end{bmatrix} = \begin{bmatrix} 19 & 22 \\ 43 & 50 \end{bmatrix} $$

Ví dụ phép nhân theo cột:
$$ AB = \begin{bmatrix} \begin{bmatrix} 1 \\ 3 \end{bmatrix} & \begin{bmatrix} 2 \\ 4 \end{bmatrix} \end{bmatrix} \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix} = \begin{bmatrix} 5 \begin{bmatrix} 1 \\ 3 \end{bmatrix} + 7 \begin{bmatrix} 2 \\ 4 \end{bmatrix} & 6 \begin{bmatrix} 1 \\ 3 \end{bmatrix} + 8 \begin{bmatrix} 2 \\ 4 \end{bmatrix} \end{bmatrix} = \begin{bmatrix} \begin{bmatrix} 5 \\ 15 \end{bmatrix} + \begin{bmatrix} 14 \\ 28 \end{bmatrix} & \begin{bmatrix} 6 \\ 18 \end{bmatrix} + \begin{bmatrix} 16 \\ 32 \end{bmatrix} \end{bmatrix} = \begin{bmatrix} 19 & 22 \\ 43 & 50 \end{bmatrix} $$

**Phân tích nhân tử $$A = CR$$**: Một ma trận $$A$$ kích thước $$m \times n$$ với hạng $$r$$ có thể được phân tích thành tích của ma trận $$C$$ kích thước $$m \times r$$ và ma trận $$R$$ kích thước $$r \times n$$. Ma trận $$C$$ chứa $$r$$ cột độc lập tuyến tính của $$A$$. Ma trận $$R$$ cho biết cách tổ hợp các cột của $$C$$ để tạo ra tất cả các cột của $$A$$.

$$ A = \begin{bmatrix} \mathbf{c}_1 & \dots & \mathbf{c}_r \end{bmatrix} \begin{bmatrix} r_{11} & \dots & r_{1n} \\ \vdots & \ddots & \vdots \\ r_{r1} & \dots & r_{rn} \end{bmatrix} = CR $$

Ví dụ $$A_3 = \begin{bmatrix} 1 & 3 & 4 \\ 2 & 6 & 8 \\ 5 & 15 & 20 \end{bmatrix}$$. Hạng của $$A_3$$ là 1.
$$ C = \begin{bmatrix} 1 \\ 2 \\ 5 \end{bmatrix}, \quad R = \begin{bmatrix} 1 & 3 & 4 \end{bmatrix} $$
$$ CR = \begin{bmatrix} 1 \\ 2 \\ 5 \end{bmatrix} \begin{bmatrix} 1 & 3 & 4 \end{bmatrix} = \begin{bmatrix} 1 \cdot 1 & 1 \cdot 3 & 1 \cdot 4 \\ 2 \cdot 1 & 2 \cdot 3 & 2 \cdot 4 \\ 5 \cdot 1 & 5 \cdot 3 & 5 \cdot 4 \end{bmatrix} = \begin{bmatrix} 1 & 3 & 4 \\ 2 & 6 & 8 \\ 5 & 15 & 20 \end{bmatrix} = A_3 $$

![matmul](image-4.png)

## Giải Hệ Phương trình Tuyến tính $$A\mathbf{x} = \mathbf{b}$$

Mục tiêu chính của đại số tuyến tính là giải hệ phương trình tuyến tính $$A\mathbf{x} = \mathbf{b}$$. Trong đó $$A$$ là ma trận hệ số, $$\mathbf{x}$$ là vector ẩn, và $$\mathbf{b}$$ là vector vế phải.

Chúng ta sẽ sử dụng phương pháp **khử Gauss** để biến ma trận $$A$$ thành ma trận tam giác trên $$U$$. Đồng thời áp dụng các bước khử này cho vector $$\mathbf{b}$$ để thu được vector $$\mathbf{c}$$. Hệ phương trình ban đầu $$A\mathbf{x} = \mathbf{b}$$ trở thành hệ tam giác trên $$U\mathbf{x} = \mathbf{c}$$.

$$ \begin{bmatrix} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2} & \dots & a_{nn} \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix} = \begin{bmatrix} b_1 \\ b_2 \\ \vdots \\ b_n \end{bmatrix} \implies \begin{bmatrix} u_{11} & u_{12} & \dots & u_{1n} \\ 0 & u_{22} & \dots & u_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & u_{nn} \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix} = \begin{bmatrix} c_1 \\ c_2 \\ \vdots \\ c_n \end{bmatrix} $$

* Quá trình biến đổi $$A$$ thành $$U$$ tốn khoảng $$\frac{1}{3} n^3$$ phép nhân và trừ.
* Quá trình biến đổi $$\mathbf{b}$$ thành $$\mathbf{c}$$ tốn khoảng $$n^2$$ phép toán.

Sau khi có hệ tam giác trên $$U\mathbf{x} = \mathbf{c}$$, ta có thể giải nó bằng **phép thế ngược**. Bắt đầu từ phương trình cuối cùng (chỉ có một ẩn) và giải dần lên trên.

* Nếu tất cả các phần tử trên đường chéo chính của $$U$$ (gọi là **chốt - pivot**) khác không, ma trận $$A$$ khả nghịch và hệ có nghiệm duy nhất.
* Nếu có chốt bằng không, ma trận $$A$$ không khả nghịch. Hệ có thể không có nghiệm hoặc có vô số nghiệm.

![Linear System](image-2.png)


## Ma trận Khử và Ma trận Nghịch đảo

Các bước khử Gauss có thể được biểu diễn bằng phép nhân với các **ma trận khử**. Ví dụ, ma trận $$E_{ij}$$ trừ $$l_{ij}$$ lần hàng $$j$$ vào hàng $$i$$.

$$ E_{ij} = I - l_{ij} \mathbf{e}_i \mathbf{e}_j^T $$
Trong đó $$I$$ là ma trận đơn vị, $$\mathbf{e}_i$$ là vector cột với 1 ở vị trí $$i$$ và 0 ở các vị trí khác.

Ví dụ, ma trận trừ 2 lần hàng 1 vào hàng 2:
$$ E_{21} = \begin{bmatrix} 1 & 0 & 0 \\ -2 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} $$

Phép khử Gauss biến $$A$$ thành $$U$$ thông qua một chuỗi các phép nhân ma trận khử:

$$ E_{nn} \dots E_{31} E_{21} A = U $$

Tích của các ma trận khử này là ma trận $$E$$.

$$ E = E_{nn} \dots E_{31} E_{21} $$

**Ma trận nghịch đảo** $$A^{-1}$$ của ma trận vuông $$A$$ (nếu tồn tại) là ma trận thỏa mãn $$A^{-1}A = I$$ và $$AA^{-1} = I$$. Ma trận nghịch đảo "hoàn tác" những gì ma trận $$A$$ đã làm.

$$ A^{-1}A = I, \quad AA^{-1} = I $$

* Ma trận $$A$$ khả nghịch khi và chỉ khi nó có $$n$$ chốt khác không sau khi khử Gauss (có thể cần hoán vị hàng).
* Nếu $$A$$ khả nghịch, nghiệm duy nhất của $$A\mathbf{x} = \mathbf{b}$$ là $$\mathbf{x} = A^{-1}\mathbf{b}$$.

![LU Decomposition](image-3.png)

**Phân tích nhân tử $$A = LU$$**: Khi không cần hoán vị hàng, ma trận $$A$$ có thể được phân tích thành tích của ma trận tam giác dưới $$L$$ và ma trận tam giác trên $$U$$.

$$ A = LU $$

Ma trận $$U$$ là ma trận tam giác trên thu được từ quá trình khử Gauss. Ma trận $$L$$ là ma trận tam giác dưới chứa các **hệ số nhân** $$l_{ij}$$ được sử dụng trong quá trình khử, với các phần tử trên đường chéo chính bằng 1.

$$ L = E^{-1} = (E_{nn} \dots E_{21})^{-1} = E_{21}^{-1} \dots E_{nn}^{-1} $$

* Nghịch đảo của ma trận $$E_{ij}$$ trừ $$l_{ij}$$ lần hàng $$j$$ vào hàng $$i$$ là ma trận cộng $$l_{ij}$$ lần hàng $$j$$ vào hàng $$i$$.
$$ E_{ij}^{-1} = I + l_{ij} \mathbf{e}_i \mathbf{e}_j^T $$

Ví dụ, nghịch đảo của ma trận $$E_{21}$$ trừ 2 lần hàng 1 vào hàng 2 là ma trận cộng 2 lần hàng 1 vào hàng 2:
$$ E_{21}^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} $$

Ma trận $$L$$ có dạng đặc biệt:
$$ L = \begin{bmatrix} 1 & 0 & \dots & 0 \\ l_{21} & 1 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ l_{n1} & l_{n2} & \dots & 1 \end{bmatrix} $$
Các hệ số nhân $$l_{ij}$$ trong quá trình khử chính là các phần tử dưới đường chéo chính của $$L$$.

Giải hệ $$A\mathbf{x} = \mathbf{b}$$ bằng phân tích $$LU$$:
$$ LU\mathbf{x} = \mathbf{b} $$
Đặt $$U\mathbf{x} = \mathbf{c}$$. Đầu tiên giải hệ $$L\mathbf{c} = \mathbf{b}$$ bằng phép thế xuôi, sau đó giải hệ $$U\mathbf{x} = \mathbf{c}$$ bằng phép thế ngược.

**Ma trận đơn vị** $$I$$ là ma trận vuông có các phần tử trên đường chéo chính bằng 1 và các phần tử còn lại bằng 0. Nó giống như số 1 trong phép nhân vô hướng: $$I\mathbf{v} = \mathbf{v}$$.

## Hoán vị và Chuyển vị

**Ma trận hoán vị** $$P$$ là ma trận thu được bằng cách hoán đổi các hàng của ma trận đơn vị $$I$$. Phép nhân $$P\mathbf{x}$$ hoán vị các thành phần của vector $$\mathbf{x}$$.

$$ P = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} $$
$$ P \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} x_2 \\ x_1 \end{bmatrix} $$

Đặc tính quan trọng của ma trận hoán vị là nghịch đảo của nó bằng chuyển vị của nó:

$$ P^{-1} = P^T $$

**Ma trận chuyển vị** $$A^T$$ của ma trận $$A$$ thu được bằng cách đổi hàng thành cột và cột thành hàng. Nếu $$A$$ có kích thước $$m \times n$$, $$A^T$$ có kích thước $$n \times m$$.

$$ A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}, \quad A^T = \begin{bmatrix} a & c \\ b & d \end{bmatrix} $$

$$ (A^T)_{ij} = A_{ji} $$

* Chuyển vị của tích: $$(AB)^T = B^T A^T$$. Thứ tự bị đảo ngược, giống như nghịch đảo của tích.
* Chuyển vị của chuyển vị: $$(A^T)^T = A$$.
* Chuyển vị của tổng: $$(A+B)^T = A^T + B^T$$.

**Ma trận đối xứng** $$S$$ là ma trận vuông bằng chuyển vị của nó:

$$ S^T = S $$

Điều này có nghĩa là các phần tử đối xứng qua đường chéo chính bằng nhau: $$S_{ij} = S_{ji}$$.

* Tích $$A^T A$$ luôn là ma trận đối xứng, bất kể $$A$$ là ma trận gì.
* Tích $$AA^T$$ cũng luôn là ma trận đối xứng.

**Phân tích nhân tử $$PA = LU$$**: Khi cần hoán vị hàng trong quá trình khử Gauss, chúng ta sử dụng ma trận hoán vị $$P$$ để sắp xếp lại các hàng của $$A$$ trước khi khử.

$$ PA = LU $$

## Đạo hàm và Ma trận Sai phân Hữu hạn

Đại số tuyến tính và giải tích liên quan chặt chẽ với nhau. Ma trận sai phân hữu hạn xấp xỉ các toán tử vi phân như đạo hàm.

* Đạo hàm bậc nhất của hàm $$y(x)$$: $$y'(x) = \frac{dy}{dx}$$. Nó cho biết tốc độ thay đổi của $$y$$ theo $$x$$.
* Đạo hàm bậc hai của hàm $$y(x)$$: $$y''(x) = \frac{d^2y}{dx^2}$$. Nó cho biết tốc độ thay đổi của đạo hàm bậc nhất, liên quan đến độ cong của đồ thị.

**Xấp xỉ sai phân hữu hạn** sử dụng các giá trị của hàm tại các điểm rời rạc để xấp xỉ đạo hàm.

* Xấp xỉ đạo hàm bậc nhất (sai phân tiến):
$$ \frac{y(x+h) - y(x)}{h} \approx y'(x) $$
* Xấp xỉ đạo hàm bậc nhất (sai phân lùi):
$$ \frac{y(x) - y(x-h)}{h} \approx y'(x) $$
* Xấp xỉ đạo hàm bậc nhất (sai phân trung tâm, chính xác hơn):
$$ \frac{y(x+h) - y(x-h)}{2h} \approx y'(x) $$
* Xấp xỉ đạo hàm bậc hai:
$$ \frac{y(x+h) - 2y(x) + y(x-h)}{h^2} \approx y''(x) $$

Phương trình vi phân có thể được xấp xỉ bằng hệ phương trình tuyến tính sử dụng ma trận sai phân hữu hạn. Ví dụ, phương trình $$-\frac{d^2u}{dx^2} = f(x)$$ với điều kiện biên $$u(0)=0$$ và $$u(1)=0$$. Chia đoạn $$[0,1]$$ thành $$N+1$$ khoảng bằng nhau, các điểm lưới là $$x_i = ih$$. Chúng ta xấp xỉ $$u(x_i)$$ bằng $$u_i$$.

Phương trình tại điểm lưới $$x_i$$ có thể được xấp xỉ bằng:

$$ -\frac{u_{i-1} - 2u_i + u_{i+1}}{h^2} = f(x_i) $$

Với điều kiện biên $$u_0 = 0$$ và $$u_{N+1} = 0$$, ta có một hệ $$N$$ phương trình tuyến tính cho các ẩn $$u_1, \dots, u_N$$. Hệ này có thể viết dưới dạng ma trận $$K_N \mathbf{u} = h^2 \mathbf{f}$$, trong đó $$K_N$$ là **ma trận sai phân bậc hai cố định-cố định**:

$$ K_N = \begin{bmatrix} 2 & -1 & 0 & \dots & 0 \\ -1 & 2 & -1 & \dots & 0 \\ 0 & -1 & 2 & \dots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \dots & 2 \end{bmatrix} $$

* Ma trận $$K_N$$ là ma trận đối xứng.
* Ma trận $$K_N$$ là ma trận dải (banded), chỉ có các phần tử trên đường chéo chính và hai đường chéo lân cận khác không (tridiagonal).
* Ma trận $$K_N$$ có các đường chéo hằng số (trừ các phần tử ở biên với điều kiện biên).
* Ma trận $$K_N$$ khả nghịch.

Ngoài ra còn có các ma trận sai phân khác như ma trận **cố định-tự do** $$T_N$$ (đường chéo chính bắt đầu bằng 1 thay vì 2) và ma trận **tự do-tự do** $$B_N$$ (đường chéo chính bắt đầu và kết thúc bằng 1), tùy thuộc vào điều kiện biên. Ma trận $$B_N$$ là ma trận suy biến (singular).

$$ T_N = \begin{bmatrix} 1 & -1 & 0 & \dots & 0 \\ -1 & 2 & -1 & \dots & 0 \\ 0 & -1 & 2 & \dots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \dots & 2 \end{bmatrix} $$

$$ B_N = \begin{bmatrix} 1 & -1 & 0 & \dots & 0 \\ -1 & 2 & -1 & \dots & 0 \\ 0 & -1 & 2 & \dots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \dots & 1 \end{bmatrix} $$

Hành trình khám phá của chúng ta mới chỉ bắt đầu. Còn rất nhiều điều thú vị phía trước về các không gian con, tính trực giao, trị riêng, vector riêng, và ứng dụng của đại số tuyến tính trong nhiều lĩnh vực khác nhau.