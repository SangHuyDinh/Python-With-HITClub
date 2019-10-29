Bài 1: Tài rất thích nghĩ ra các giải thuật mã hóa xâu, hôm nay Tài lại tiếp tục nghĩ ra một giải thuật mới và đố bạn giải mã.
Tài gọi trung vị của một xâu là ký tự nằm chính giữa xâu đó, nếu xâu có độ dài chẵn thì trung vị của xâu là phần tử lệch về bên trái.
Ví dụ: codeforces, codefight, tourist, contest, acm là các xâu có phần tử trung vị đã được im đậm.
Giải thuật mã hóa của Tài được thực hiện như sau:
Tài ghi lại phần tử trung vị của xâu sau đó xóa phần tử trung vị này đi , sau đó lại tiếp tục tìm trung vị rồi ghi lại, ... tới khi chỉ còn xâu rỗng. Xâu mã hóa là sâu đã được Tài ghi lại.
Tài cho bạn xâu s là xâu đã được mã hóa, nhiệm vụ của bạn biến đổi xâu đã được mã hóa này về xâu ban đầu.

Ví dụ:

Cho s = "edwoacr", thì kết quả của nó sẽ là decodeString(s) = "codewar"
Với xâu ban đầu "codewar" thì trung vị của nó sẽ là 'e', ta ghi lại phần tử này và xóa nó đi để xâu trở thành "codwar".
Với xâu "codwar" thì trung vị của nó sẽ là 'd', ta ghi lại phần tử này và xóa nó đi để xâu trở thành "cowar".
Với xâu "cowar" thì trung vị của nó sẽ là 'w', ta ghi lại phần tử này và xóa nó đi để xâu trở thành "coar".
Với xâu "coar" thì trung vị của nó sẽ là 'o', ta ghi lại phần tử này và xóa nó đi để xâu trở thành "car".
Với xâu "car" thì trung vị của nó sẽ là 'a', ta ghi lại phần tử này và xóa nó đi để xâu trở thành "cr".
Với xâu "cr" thì trung vị của nó sẽ là 'c', ta ghi lại phần tử này và xóa nó đi để xâu trở thành 'r'.
Với xâu 'r' thì trung vị của nó sẽ là 'r', ta ghi lại phần tử này và xóa nó đi để xâu trở thành xâu rỗng.
Vậy xâu ban dầu "codewar" sẽ được Tài mã hóa thành "edwoacr".

Đầu vào: một chuỗi s là chuỗi đã được mã hoá Đầu ra: chuỗi s trước khi được mã hoá.

Bài 2: Cho toạ độ trái dưới, phải trên của 2 hình chữ nhật A, B. Hãy tính phần diện tích không trùng nhau của 2 hình chữ nhật. Cho biết các cạnh của hình chữ nhật luôn song song với 2 trục Ox,Oy.
 Ví dụ: Cho A=[1,1,3,3] và B=[2,2,4,4], thì đầu ra của chúng ta sẽ là 6
 Phần không trùng nhau như chúng ta nhìn thấy ở trên hình là 6 ô.
 Đầu vào:
 Dòng đầu tiên là toạ độ của hình chữ nhật A được biểu diễn bởi 4 điểm (x1,y1,x2,y2) tương ứng với các điểm trái dưới và phải trên của hình chữ nhật.
 Dòng thứ hai là toạ độ của hình chữ nhật B được biểu diễn bởi 4 điểm (x1,y1,x2,y2) tương ứng với các điểm trái dưới và phải trên của hình chữ nhật.
 Đầu ra:nhật Diện tích không trùng nhau của hình chữ nhật.
