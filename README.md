# Tổng hợp các bài tập lập trình cơ bản
Những bạn mới học lập trình thường cảm thấy khó khăn khi muốn tìm bài tập thể rèn kĩ năng của mình. Có thể dùng Google để tìm kiếm, nhưng tài nguyên trên Google thường quá nhiều và có thể bạn không biết độ khó của những bài tập đó có nằm trong khả năng của mình hay không. Để giảm thời gian cho việc này, mình sẽ liệt kê một số bài tập mà những người mới bắt đầu có thể làm ngay nếu như bạn nắm rõ được các cấu trúc cơ bản của Python như vòng lặp, câu điều kiện if/else, các phép toán, các kiểu dữ liệu, ...

Các bài tập liệt kê ở đây có thể được giải quyết bằng bất kì ngôn ngữ nào chứ không chỉ riêng Python nên có thể được dùng để tham khảo khi chúng ta học một ngôn ngữ khác.

Các bạn không nên dùng các standard library của Python (hay một ngôn ngữ nào khác mà bạn đang tìm hiểu) để giải các bài tập này mà chỉ dùng các cấu trúc cơ bản của ngôn ngữ như mình đã nêu ở trên. Điều này giúp bạn hiểu và nắm chắc hơn những lí thuyết đã được học. Đối với mỗi bài tập mình cũng sẽ cố gắng liệt kê ra những lí thuyết bạn cần biết và sẽ nắm chắc hơn sau khi xử lí được bài tập đó. Trong trường hợp phải dùng standard library để giải thì mình sẽ nêu rõ trong yêu cầu.

Các bài giải mình sẽ viết theo chuẩn PEP8 (sử dụng flake8 để kiểm tra code), mình cũng recommend là bạn hãy tập cho mình thói quen viết code theo chuẩn này, rất có lợi khi đi làm thực tế.

### Danh sách bài tập (click vào mỗi bài tập để xem đáp án)
1. <a href="https://github.com/hoanvu/basic_programming_exercises/blob/master/solutions/1.py">Tính độ dài một chuỗi không sử dụng hàm có sẵn</a>
2. <a href="https://github.com/hoanvu/basic_programming_exercises/blob/master/solutions/2.py">Tính độ dài một mảng không sử dụng hàm có sẵn</a>
3. <a href="https://github.com/hoanvu/basic_programming_exercises/blob/master/solutions/3.py">Đảo ngược một chuỗi</a>
4. <a href="https://github.com/hoanvu/basic_programming_exercises/blob/master/solutions/4.py">Đảo ngược một mảng</a>
5. <a href="https://github.com/hoanvu/basic_programming_exercises/blob/master/solutions/5.py">Tìm một hoặc nhiều từ dài nhất trong một chuỗi</a>
6. <a href="https://github.com/hoanvu/basic_programming_exercises/blob/master/solutions/6.py">Tìm số lớn nhất và nhỏ nhất trong một mảng</a>
7. <a href="https://github.com/hoanvu/basic_programming_exercises/blob/master/solutions/7.py">Tính tổng, tích và trung bình của các số trong một mảng</a>
8. <a href="https://github.com/hoanvu/basic_programming_exercises/blob/master/solutions/8.py">In hoa một chuỗi (chuyển toàn bộ chữ cái thường sang in hoa, giữ nguyên những chữ cái in hoa)</a>
9. <a href="https://github.com/hoanvu/basic_programming_exercises/blob/master/solutions/9.py">Kiểm tra xem một chữ cái có phải là nguyên âm hay không</a>
10. <a href="https://github.com/hoanvu/basic_programming_exercises/blob/master/solutions/10.py">Tìm tất cả các từ trong một chuỗi có độ dài lớn hơn 'n' ('n' là do người dùng chọn)</a>
11. Tìm tất cả các số trong một mảng lớn hơn 'n' ('n' là do người dùng chọn)
12. Kiểm tra xem một chuỗi có phải là palindrome hay không
13. Tính giai thừa
14. Kiểm tra xem một số được nhập vào có phải là số nguyên tố hay không
15. Tìm số nguyên tố thứ 'n' ('n' là do người dùng chọn)

### Mô tả chi tiết bài tập
1. <strong>Tính độ dài một chuỗi không sử dụng hàm có sẵn</strong>
    + Input: nhập vào một chuỗi bất kì. VD: "Unbelievable", "This is a sample string!", ...
    + Output: số chữ cái của chuỗi vừa nhập, bao gồm cả dấu cách
    + Kiến thức cần biết: vòng lặp, phép toán (không sử dụng hàm len() có sẵn của Python)

2. <strong>Tính độ dài một mảng không sử dụng hàm có sẵn</strong>
    + Input: nhập vào một chuỗi bất kì. VD: [1, 2, 3, 4, 5, 6, 7, 8, 9], [5, 5, 5, 5, 5, 5], ...
    + Output: số chữ cái của chuỗi vừa nhập, bao gồm cả dấu cách
    + Kiến thức cần biết: vòng lặp, phép toán (không sử dụng hàm len() có sẵn của Python)

3. <strong>Đảo ngược một chuỗi</strong>
    + Input: nhập vào 1 chuỗi bất kì. VD: "Unbelievable", "This is a sample string!", ...
    + Ouput: chuỗi mới là đảo ngược của chuỗi vừa nhập
    + Kiến thức cần biết: vòng lặp, chuỗi, string slicing

4. <strong>Đảo ngược một mảng</strong>
    + Input: nhập vào một mảng bất kì. VD: [1, 2, 3, 4, 5], [321, -2, .5, 22], ...
    + Output: một mảng mới là đảo ngược của mảng vừa nhập
    + Kiến thức cần biết: vòng lặp, mảng, array slicing

5. <strong>Tìm từ (một hoặc nhiều) dài nhất trong một chuỗi</strong>
    + Input: nhập vào một chuỗi bất kì. VD: "Day don gian la mot chuoi nhap vao de test"
    + Output: một mảng bao gồm một hoặc nhiều từ có độ dài lớn nhất trong chuỗi vừa nhập. Ví dụ có 3 từ dài nhất cùng có 5 chữ cái thì sẽ trả về mảng có cả 3 từ đó.
    + Kiến thức cần biết: vòng lặp, câu điều kiện, mảng, chuỗi

6. <strong>Tìm số lớn nhất và nhỏ nhất trong một mảng, sử dụng hàm</strong>
    + Input: nhập vào một mảng bất kì
    + Output: số lớn nhất và nhỏ nhất trong mảng. Viết 2 hàm tương ứng với số lớn nhất và nhỏ nhất
    + Kiến thức cần biết: vòng lặp, mảng, câu điều kiện, hàm

7. <strong>Tính tổng, tích và trung bình của các số trong một mảng</strong>
    + Input: nhập vào một mảng bất kì
    + Output: tổng, tích và trung bình cộng của các số trong mảng vừa nhập
    + Kiến thức cần biết: mảng, vòng lặp, các phép toán

8. <strong>In hoa một chuỗi không sử dụng hàm upper()</strong>
    + Input: nhập vào một chuỗi bất kì. VD: "I love U", "Python's awesome!"
    + Output: chuỗi vừa nhập dưới dạng in hoa. VD: "I LOVE U", "PYTHON'S AWESOME!"
    + Kiến thức cần biết: vòng lặp, chuỗi

9. <strong>Kiểm tra xem một chữ cái có phải là nguyên âm hay không</strong>
    + Input: nhập vào một chữ cái bất kì. VD: 'a', 'f', 'g', 'd', 'e', ...
    + Output: True nếu chữ cái vừa nhập là một nguyên âm, False nếu không phải
    + Kiến thức cần biết: câu điều kiện, hàm

10. <strong>Tìm tất cả các từ trong một chuỗi có độ dài lớn hơn 'n'</strong>
    + Input: nhập vào một chuỗi bất kì và số nguyên 'n'
    + Output: tất cả các từ trong chuỗi vừa nhập có độ dài lớn hơn 'n'
    + Kiến thức cần biết: chuỗi, vòng lặp, câu điều kiện