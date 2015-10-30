# Các bài tập lập trình cơ bản - Phần II

<a href="https://github.com/hoanvu/basic_programming_exercises/blob/master/Ph%E1%BA%A7n%20I.md">Đọc các bài tập thuộc phần I tại đây</a>

Đây là phần II giới thiệu về các bài tập lập trình cơ bản cho các bạn mới bắt đầu. Ở phần I, các bạn đã được làm quen với các thành phần cơ bản của Python như chuỗi, mảng, các kiểu dữ liệu, list, dict, set, hàm, ... Hi vọng lúc này các bạn đã có thể sử dụng các thành phần này một cách nhuần nhuyễn. Chính vì thế, trong phần mô tả chi tiết mình sẽ không đề cập các thành phần cơ bản trên vào mục Kiến thức cần biết nữa.

Trong phần II này, các bài tập sẽ tập trung chủ yếu vào việc xử lí file (đọc, ghi, ...), xử lí các exception, regular expression, ...

### Danh sách các bài tập - Phần II
1. <a href="https://github.com/hoanvu/basic_programming_exercises/blob/master/solutions/part_2/part02_001.py">Đọc file và in nội dung ra màn hình</a>
2. <a href="https://github.com/hoanvu/basic_programming_exercises/blob/master/solutions/part_2/part02_002.py">Đọc một file và dùng exception handling để in lỗi tương ứng nếu file đó không tồn tại</a>
3. <a href="https://github.com/hoanvu/basic_programming_exercises/blob/master/solutions/part_2/part02_003.py">Tính số dòng, số từ và chữ cái trong một file (không tính dấu cách và dòng trống)</a>
4. <a href="https://github.com/hoanvu/basic_programming_exercises/blob/master/solutions/part_2/part02_004.py"></a>Tính số dòng, số từ và chữ cái trong một file (không tính dấu cách và dòng trống) sử dụng exception handling</a>
5. Tính tổng 2 số được nhập vào và dùng exception handling để kiểm tra input người dùng có phải là số hay không
6. Ghi dòng chữ "Hello World!" vào file với tên bất kì

### Mô tả chi tiết bài tập
1. <strong>Đọc file và in nội dung ra màn hình</strong>
    + Input: đường dẫn tới file cần đọc
    + Output: nội dung của file đó
    + Kiến thức cần biết: Files I/O

2. <strong>Đọc một file và dùng exception handling để in lỗi tương ứng nếu file đó không tồn tại</strong>
    + Input: đường dẫn tới file cần đọc
    + Output: 
        + Nếu file đó tồn tại, in nội dung ra console
        + Nếu file không tồn tại, xử lí và in ra tin nhắn file không tồn tại
    + Kiến thức cần biết: Files I/O, Exception Handling

3. <strong>Tính số dòng, số từ và chữ cái trong một file (không tính dấu cách)</strong>
    + Input: đường dẫn tới file cần đọc
    + Output: số dòng, số từ và chữ cái của file vừa nhập
    + Kiến thức cần biết: Files I/O

4. <strong>Tính số dòng, từ và chữ cái trong một file (không tính dấu cách) sử dụng exception handling</strong>
    + Input: đường dẫn tới file cần đọc 
    + Output: số dòng, số từ và chữ cái của file vừa nhập
    + Kiến thức cần biết: Files I/O, exception handling

5. <strong>Tính tổng 2 số được nhập vào và dùng exception handling để kiểm tra input người dùng có phải là số hay không</strong>
    + Input: 2 số bất kì
    + Output: 
        + Nếu người dùng nhập vào 2 số, in ra tổng 2 số đó
        + Nếu người dùng nhập vào không phải số, dùng exception handling để xử lí và in ra tin nhắn phù hợp
    + Kiến thức cần biết: exception handling

6. <strong>Ghi dòng chữ "Hello World!" vào file với tên bất kì</strong>
    + Input: chuỗi "Hello World!" hoặc bất kì chuỗi nào mà bạn thích
    + Output: một file mới với nội dung là chuỗi vừa được nhập
    + Kiến thức cần biết: files I/O