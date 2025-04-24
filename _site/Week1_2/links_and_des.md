### 1. Sequential image segmentation based on minimum spanning tree representation

*   **Tên bài báo:** Sequential image segmentation based on minimum spanning tree representation
*   **Link:** [DOI: 10.1016/j.patrec.2016.06.001](https://doi.org/10.1016/j.patrec.2016.06.001) []
*   **Phương pháp:** **Phân vùng ảnh tuần tự** sử dụng **biểu diễn cây bao trùm tối thiểu (MST)**.
*   **Hiệu suất:** Nguồn chỉ cung cấp thông tin và tóm tắt mô tả, không đề cập đến hiệu suất cụ thể.

### 2. [IEEE 2001 International Conference on Image Processing - Thessaloniki, Greece (7-10 Oct. 2001)] Proceedings 2001 International Conference on Image Processing (Cat. No.01CH37205) - Scale space segmentation of color images using watersheds and fuzzy region merging

*   **Tên bài báo:** [IEEE 2001 International Conference on Image Processing - Thessaloniki, Greece (7-10 Oct. 2001)] Proceedings 2001 International Conference on Image Processing (Cat. No.01CH37205) - Scale space segmentation of color images using watersheds and fuzzy region merging
*   **Link:** [DOI: 10.1109/icip.2001.959150](https://doi.org/10.1109/icip.2001.959150) []
*   **Phương pháp:** **Phân vùng ảnh màu theo không gian tỷ lệ** kết hợp **thuật toán Watersheds** và **hợp nhất vùng mờ**.
*   **Hiệu suất:** Nguồn chỉ cung cấp thông tin và tóm tắt mô tả, không đề cập đến hiệu suất cụ thể. Tuy nhiên, nguồn có nhắc đến một phương pháp **multi-scale watershed approach (MSHLK)** được biết đến với chất lượng tốt nhưng chi phí tính toán cao (1 giây/kPixel), đây có thể là một phương pháp liên quan.

### 3. An Efficient Parallel Algorithm for Graph-Based Image Segmentation

*   **Tên bài báo:** An Efficient Parallel Algorithm for Graph-Based Image Segmentation
*   **Link:** [https://2024.sci-hub.ru/6177/a33216d66196b4234bce28cc0bd870c6/wassenberg2009.pdf#cite.vanhamel](https://2024.sci-hub.ru/6177/a33216d66196b4234bce28cc0bd870c6/wassenberg2009.pdf#cite.vanhamel) []
*   **Phương pháp:** Thuật toán **song song hiệu quả** dựa trên **cây bao trùm tối thiểu (MST)** với một **phương pháp cắt đồ thị (graph-cutting heuristic)** mới (**PHMSF - Parallel Heuristic for Minimum Spanning Forests**), được thiết kế để cho phép song song hóa mà không làm gián đoạn các đối tượng ở ranh giới các khối ảnh.
*   **Hiệu suất:** Thuật toán **PHMSF** được chứng minh là **vượt trội hơn đáng kể so với các kỹ thuật phân vùng hiện có**. So sánh với các thuật toán khác trên ảnh USC SIPI:
    *   **MSHLK** cho chất lượng cao nhưng hợp nhất mái nhà vào vùng trời và bị oversegmentation ở ảnh thứ hai. Chi phí tính toán là **1 giây/kPixel**.
    *   **MS** thành công hơn trong việc hợp nhất các đối tượng nhưng cũng chia nhỏ một số đối tượng và có các phân đoạn giả gần ranh giới. Tốc độ xử lý là **0.1 MPixel/s**. **PHMSF nhanh hơn MS 138 lần**.
    *   **MSER** tạo ra nhãn ảnh khá tốt nhưng không coi bức tường là một vùng ổn định. Tốc độ là **2 MPixel/s**. **PHMSF nhanh hơn MSER 5 lần**.
    *   **GBS** chấp nhận được nhưng undersegmentation gần đường mái và oversegmentation vùng trời và tường, cũng như hợp nhất các đối tượng khác màu. Tốc độ là **0.45 MPixel/s**. **PHMSF nhanh hơn GBS 28 lần**.
    *   **PHMSF** cung cấp kết quả tương đương với MSHLK và MS nhưng với thời gian tính toán chỉ bằng **1/4000 và 1/50** tương ứng. Tốc độ đạt được là **12.80 MPixel/s** trên một tập hợp 8.19 MPixel của ảnh Quickbird. Trên các ảnh lớn hơn (tới 527 MPixel), hiệu suất còn cải thiện, đạt tới **24.4 MPixel/s**.

### 4. Efficient Graph-Based Image Segmentation

*   **Tên bài báo:** Efficient Graph-Based Image Segmentation
*   **Link:** [http://people.cs.uchicago.edu/~pff/segment/](http://people.cs.uchicago.edu/~pff/segment/) [] (dựa trên trích dẫn trong nguồn)
*   **Phương pháp:** Thuật toán **phân vùng ảnh hiệu quả dựa trên đồ thị**, định nghĩa một **vị ngữ để đo lường bằng chứng về ranh giới giữa hai vùng** và phát triển một thuật toán dựa trên vị ngữ này. Thuật toán này dựa trên việc **chọn các cạnh từ đồ thị** và **điều chỉnh thích ứng tiêu chí phân vùng dựa trên mức độ biến thiên ở các vùng lân cận của ảnh**.
*   **Hiệu suất:** Thuật toán chạy trong thời gian **gần như tuyến tính theo số lượng cạnh của đồ thị**. Thời gian chạy là **O(n log n)** cho $n$ pixel ảnh và có thể chạy ở **tốc độ video**. Thuật toán có khả năng **bảo toàn chi tiết ở các vùng ảnh có độ biến thiên thấp đồng thời bỏ qua chi tiết ở các vùng có độ biến thiên cao**. Phương pháp này **điều chỉnh thích ứng tiêu chí phân vùng dựa trên mức độ biến thiên ở các vùng lân cận của ảnh**. Thuật toán này đã được sử dụng trong các ứng dụng cơ sở dữ liệu ảnh quy mô lớn. Trong các thử nghiệm, thuật toán cho thấy khả năng nắm bắt các nhóm hoặc vùng quan trọng về mặt nhận thức và xử lý các trường hợp mà sự khác biệt về cường độ lớn không nhất thiết chỉ ra nhiều vùng.
