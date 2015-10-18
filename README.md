# Tổng hợp các bài tập lập trình cơ bản
Những bạn mới học lập trình thường cảm thấy khó khăn khi muốn tìm bài tập thể rèn kĩ năng của mình. Có thể dùng Google để tìm kiếm, nhưng tài nguyên trên Google thường quá nhiều và có thể bạn không biết độ khó của những bài tập đó có nằm trong khả năng của mình hay không. Để giảm thời gian cho việc này, mình sẽ liệt kê một số bài tập mà những người mới bắt đầu có thể làm ngay nếu như bạn nắm rõ được các cấu trúc cơ bản của Python như vòng lặp, câu điều kiện if/else, các phép toán, các kiểu dữ liệu, ...

Các bài tập liệt kê ở đây có thể được giải quyết bằng bất kì ngôn ngữ nào chứ không chỉ riêng Python nên có thể được dùng để tham khảo khi chúng ta học một ngôn ngữ khác.

Các bạn không nên dùng các standard library của Python (hay một ngôn ngữ nào khác mà bạn đang tìm hiểu) để giải các bài tập này mà chỉ dùng các cấu trúc cơ bản của ngôn ngữ như mình đã nêu ở trên. Điều này giúp bạn hiểu và nắm chắc hơn những lí thuyết đã được học. Đối với mỗi bài tập mình cũng sẽ cố gắng liệt kê ra những lí thuyết bạn cần biết và sẽ nắm chắc hơn sau khi xử lí được bài tập đó. Trong trường hợp phải dùng standard library để giải thì mình sẽ nêu rõ trong yêu cầu.

Các bài giải mình sẽ viết theo chuẩn PEP8 (sử dụng flake8 để kiểm tra code), mình cũng recommend là bạn hãy tập cho mình thói quen viết code theo chuẩn này, rất có lợi khi đi làm thực tế.

### Danh sách bài tập (click vào mỗi bài tập để xem đáp án)
1. Tính độ dài một chuỗi không sử dụng hàm có sẵn
2. Tính độ dài một mảng không sử dụng hàm có sẵn
3. Đảo ngược một chuỗi
4. Đảo ngược một mảng
5. Tìm một hoặc nhiều từ dài nhất trong một chuỗi
6. Tìm số lớn nhất và nhỏ nhất trong một mảng
7. Tính tổng và trung bình của các số trong một mảng
8. 

### Mô tả chi tiết bài tập
1. Tính độ dài một chuỗi không sử dụng hàm có sẵn
    + Input: nhập vào một chuỗi bất kì. VD: "Unbelievable", "This is a sample string!", ...
    + Output: số chữ cái của chuỗi vừa nhập, bao gồm cả dấu cách
    + Kiến thức cần biết: vòng lặp, phép toán (không sử dụng hàm len() có sẵn của Python)

2. Tính độ dài một mảng không sử dụng hàm có sẵn
    + Input: nhập vào một chuỗi bất kì. VD: [1, 2, 3, 4, 5, 6, 7, 8, 9], [5, 5, 5, 5, 5, 5], ...
    + Output: số chữ cái của chuỗi vừa nhập, bao gồm cả dấu cách
    + Kiến thức cần biết: vòng lặp, phép toán (không sử dụng hàm len() có sẵn của Python)

3. <strong>Đảo ngược một chuỗi</strong>
    + Input: nhập vào 1 chuỗi bất kì. VD: "Unbelievable", "This is a sample string!", ...
    + Ouput: chuỗi mới là đảo ngược của chuỗi vừa nhập
    + Kiến thức cần biết: vòng lặp, chuỗi

4. <strong>Đảo ngược một mảng</strong>
    + Input: nhập vào một mảng bất kì. VD: [1, 2, 3, 4, 5], [321, -2, .5, 22], ...
    + Output: một mảng mới là đảo ngược của mảng vừa nhập
    + Kiến thức cần biết: vòng lặp, mảng

5. <strong>Tìm từ (một hoặc nhiều) dài nhất trong một chuỗi</strong>
    + Input: nhập vào một chuỗi bất kì. VD: "Day don gian la mot chuoi nhap vao de test"
    + Output: một mảng bao gồm một hoặc nhiều từ có độ dài lớn nhất trong chuỗi vừa nhập. Ví dụ có 3 từ dài nhất cùng có 5 chữ cái thì sẽ trả về mảng có cả 3 từ đó.
    + Kiến thức cần biết: vòng lặp, câu điều kiện, mảng, chuỗi