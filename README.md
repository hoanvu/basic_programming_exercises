# Tổng hợp các bài tập lập trình cơ bản
Những bạn mới học lập trình thường cảm thấy khó khăn khi muốn tìm bài tập thể rèn kĩ năng của mình. Có thể dùng Google để tìm kiếm, nhưng tài nguyên trên Google thường quá nhiều và có thể bạn không biết độ khó của những bài tập đó có nằm trong khả năng của mình hay không. Để giảm thời gian cho việc này, mình sẽ liệt kê một số bài tập mà những người mới bắt đầu có thể làm ngay nếu như bạn nắm rõ được các cấu trúc cơ bản của Python như vòng lặp, câu điều kiện if/else, các phép toán, các kiểu dữ liệu, ...

Các bài tập liệt kê ở đây có thể được giải quyết bằng bất kì ngôn ngữ nào chứ không chỉ riêng Python nên có thể được dùng để tham khảo khi chúng ta học một ngôn ngữ khác.

Các bạn không nên dùng các standard library của Python (hay một ngôn ngữ nào khác mà bạn đang tìm hiểu) để giải các bài tập này mà chỉ dùng các cấu trúc cơ bản của ngôn ngữ như mình đã nêu ở trên. Điều này giúp bạn hiểu và nắm chắc hơn những lí thuyết đã được học. Đối với mỗi bài tập mình cũng sẽ cố gắng liệt kê ra những lí thuyết bạn cần biết và sẽ nắm chắc hơn sau khi xử lí được bài tập đó. Trong trường hợp phải dùng standard library để giải thì mình sẽ nêu rõ trong yêu cầu.

Các bài giải mình sẽ viết theo chuẩn PEP8 (sử dụng flake8 để kiểm tra code), mình cũng recommend là bạn hãy tập cho mình thói quen viết code theo chuẩn này, rất có lợi khi đi làm thực tế.

### Danh sách bài tập (click vào mỗi bài tập để xem đáp án)
1. <a href="https://github.com/hoanvu/basic_programming_exercises/blob/master/solutions/001.py">Tính độ dài một chuỗi không sử dụng hàm có sẵn</a>
2. <a href="https://github.com/hoanvu/basic_programming_exercises/blob/master/solutions/002.py">Tính độ dài một mảng không sử dụng hàm có sẵn</a>
3. <a href="https://github.com/hoanvu/basic_programming_exercises/blob/master/solutions/003.py">Đảo ngược một chuỗi</a>
4. <a href="https://github.com/hoanvu/basic_programming_exercises/blob/master/solutions/004.py">Đảo ngược một mảng</a>
5. <a href="https://github.com/hoanvu/basic_programming_exercises/blob/master/solutions/005.py">Tìm một hoặc nhiều từ dài nhất trong một chuỗi</a>
6. <a href="https://github.com/hoanvu/basic_programming_exercises/blob/master/solutions/006.py">Tìm số lớn nhất và nhỏ nhất trong một mảng</a>
7. <a href="https://github.com/hoanvu/basic_programming_exercises/blob/master/solutions/007.py">Tính tổng, tích và trung bình của các số trong một mảng</a>
8. <a href="https://github.com/hoanvu/basic_programming_exercises/blob/master/solutions/008.py">In hoa một chuỗi (chuyển toàn bộ chữ cái thường sang in hoa, giữ nguyên những chữ cái in hoa)</a>
9. <a href="https://github.com/hoanvu/basic_programming_exercises/blob/master/solutions/009.py">Kiểm tra xem một chữ cái có phải là nguyên âm hay không</a>
10. <a href="https://github.com/hoanvu/basic_programming_exercises/blob/master/solutions/010.py">Tìm tất cả các từ trong một chuỗi có độ dài lớn hơn n (n là do người dùng chọn)</a>
11. <a href="https://github.com/hoanvu/basic_programming_exercises/blob/master/solutions/011.py">Tìm tất cả các số trong một mảng lớn hơn n (n là do người dùng chọn)</a>
12. <a href="https://github.com/hoanvu/basic_programming_exercises/blob/master/solutions/012.py">Kiểm tra xem một chuỗi có phải là palindrome hay không</a>
13. <a href="https://github.com/hoanvu/basic_programming_exercises/blob/master/solutions/013.py">Tính giai thừa</a>
14. <a href="https://github.com/hoanvu/basic_programming_exercises/blob/master/solutions/014.py">Kiểm tra xem một số được nhập vào có phải là số nguyên tố hay không</a>
15. Tìm số nguyên tố thứ n (n là do người dùng chọn)
16. Tìm tất cả các nhân tử chung của 2 mảng
17. Tìm tất cả ước số chung của một số nguyên bất kì
18. Tìm ước số chung lớn nhất của 2 số nguyên a và b bât kì
19. <a href="https://github.com/hoanvu/basic_programming_exercises/blob/master/solutions/019.py">Chuyển tất cả chữ cái đầu tiên của mỗi từ trong một chuỗi sang in hoa, các chữ cái còn lại trong từ viết thường</a>
20. <a href="https://github.com/hoanvu/basic_programming_exercises/blob/master/solutions/020.py">Cắt bớt một chuỗi nếu chuỗi lớn hơn một độ dài bất kì do người dùng nhập</a>
21. <a href="https://github.com/hoanvu/basic_programming_exercises/blob/master/solutions/021.py">Sinh chuỗi Fibonacci</a>

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
    + Kiến thức cần biết: vòng lặp, chuỗi, dictionary, tuple

9. <strong>Kiểm tra xem một chữ cái có phải là nguyên âm hay không</strong>
    + Input: nhập vào một chữ cái bất kì. VD: 'a', 'f', 'g', 'd', 'e', ...
    + Output: True nếu chữ cái vừa nhập là một nguyên âm, False nếu không phải
    + Kiến thức cần biết: câu điều kiện, hàm

10. <strong>Tìm tất cả các từ trong một chuỗi có độ dài lớn hơn 'n'</strong>
    + Input: nhập vào một chuỗi bất kì và số nguyên 'n'
    + Output: tất cả các từ trong chuỗi vừa nhập có độ dài lớn hơn 'n'
    + Kiến thức cần biết: chuỗi, vòng lặp, câu điều kiện, list comprehension

11. <strong>Tìm tất cả các số trong một mảng lớn hơn 'n'</strong>
    + Input: nhập vào một mảng bất kì và số nguyên 'n'
    + Output: tất cả các số trong chuỗi vừa nhập lớn hơn 'n'
    + Kiến thức cần biết: mảng, vòng lặp, câu điều kiện, hàm

12. <strong>Kiểm tra xem một chuỗi có phải là palindrome hay không</strong>
    + Input: nhập vào một chuỗi bất kì
    + Output: True nếu chuỗi là palindrome, False nếu không phải
    + Kiến thức cần biết: chuỗi, hàm

13. <strong>Tính giai thừa</strong>
    + Input: một số bất kì. VD: 5, 10, 8, ...
    + Output: giai thừa của số vừa nhập
    + Kiến thức cần biết: đệ quy, hàm

14. <strong>Kiểm tra xem một số được nhập vào có phải là số nguyên tố hay không</strong>
    + Input: một số bất kì. VD: 5, 10, 8, ...
    + Output: True nếu số vừa nhập là một số nguyên tố, False nếu không phải
    + Kiến thức cần biết: thư viện 'math' của Python (để tính căn bậc 2), câu điều kiện

15. <strong>Tìm số nguyên tố thứ n (n là do người dùng chọn)</strong>
    + Input: một số nguyên n bất kì. VD: 4, 12, 300, ...
    + Output: số nguyên tố thứ n. VD: số nguyên tố thứ 4 là số 7.
    + Kiến thức cần biết: Python generator

16. <strong>Tìm tất cả các nhân tử chung của 2 mảng</strong>
    + Input: hai mảng bất kì. VD: [1, 2, 3, 4, '5', 'test'] và [4, 5, 6, 'test', 7]
    + Output: các nhân tử chung của 2 mảng vừa nhập. VD: với 2 mảng nhập phía trên, kết quả là: [4, 'test']
    + Kiến thức cần biết: mảng

17. <strong>Tìm tất cả ước số của một số nguyên bất kì</strong>
    + Input: một số nguyên bất kì. VD: 6, 12, 40, ...
    + Output: tất cả các ước số của số vừa nhập. VD: nếu số được nhập là 6, kết quả sẽ trả về là: [1, 2, 3]
    + Kiến thức cần biết: 

18. <strong>Tìm ước số chung lớn nhất của 2 số nguyên a và b bât kì</strong>
    + Input: 2 số nguyên bất kì. VD: 9 và 12, 10 và 15, ...
    + Output: ước số chung lớn nhất của 2 số vừa nhập. VD: nếu 2 số là 9 và 12 thì kết quả sẽ là 3
    + Kiến thức cần biết: 

19. <strong>Chuyển tất cả chữ cái đầu tiên của mỗi từ trong một chuỗi sang in hoa, các chữ cái còn lại trong từ viết thường</strong>
    + Input: một chuỗi bất kì. VD: "Co con gIo baY ngAng qua!"
    + Output: chuỗi vừa nhập với tất cả các chữ cái đầu tiên của mỗi từ được viết hoa, còn lại viết thường
    + Kiến thức cần biết: chuỗi, mảng

20. <strong>Cắt bớt một chuỗi nếu chuỗi lớn hơn một độ dài bất kì do người dùng nhập</strong>
    + Input: một chuỗi và một số nguyên n bất kì
    + Output: 
        + Nếu n lớn hơn độ dài của chuỗi được nhập, trả về chuỗi ban đầu
        + Nếu n nhỏ hơn, trả về một chuỗi con của chuỗi vừa nhập, với độ dài n (từ 0 tới n - 1)
    + Kiến thức cần biết: chuỗi, câu điều kiện