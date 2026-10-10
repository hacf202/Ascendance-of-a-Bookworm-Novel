import codecs

translations = [
# Chunk 1: Lines 46-64
"""
"Roderick, xin hãy cân nhắc điều này cẩn thận..." tôi nói. "Trở thành một người dâng tên là một quyết định quá hệ trọng để thực hiện theo sự bốc đồng."
Việc có thêm ma lực chắc chắn là điều quan trọng đối với các quý tộc, nhưng tôi không nghĩ rằng nó đáng để theo đúng nghĩa đen là giao cho người khác quyền kiểm soát cuộc sống của bạn—đặc biệt là khi "người khác" đó lại là tôi.
"Tiểu thư Ro ze mai nói đúng," Matthias nói. "Đây không phải là điều để quyết định một cách quá bốc đồng như vậy. Roderick, hãy dùng đầu óc của cậu một chút đi."
"Ngài Matthias, tôi—"
"Ngay khoảnh khắc chúng ta dâng tên của mình cho ai đó, chúng ta sẽ cắt đứt mối quan hệ với cha mẹ mình mãi mãi. Chúng ta đã ở trong phe Veronica suốt cuộc đời mình; ngay cả khi cậu dâng tên của mình và kết thúc bằng việc trở thành tùy tùng của Tiểu thư Ro ze mai, mọi người sẽ đối xử với cậu như một kẻ phản bội, và ai mà biết các phe phái sẽ trông như thế nào trong vài năm nữa," Matthias nói, nhíu mày trong một biểu cảm đau khổ. "Từng... có một người đàn ông. Anh ta đã bị mê hoặc bởi một người được định sẵn để trở thành aub tiếp theo, và trái tim anh ta rực cháy khát khao được phục vụ người đó mãi mãi như một giebe trung thành khi người đó lên nắm giữ chiếc ghế aub. Nhưng tình hình đã thay đổi. Người mà trái tim anh ta hướng về đã đánh mất tư cách tranh cử vào chiếc ghế đó chỉ sau một đêm."
Một ai đó trong đám đông nuốt nước bọt cái ực. Đó không phải là một kịch bản bất khả thi; Veronica đã nắm giữ quyền lực trong nhiều thập kỷ, chỉ để đột nhiên mất tất cả. Chỉ mới vài năm trôi qua kể từ đó, và hoàn toàn có khả năng cán cân quyền lực sẽ lật ngược một lần nữa.
"Tiểu thư Ro ze mai đã theo học Học viện Hoàng gia vào năm ngoái, và trong khoảng thời gian của một mùa đông duy nhất, người đã hình thành các mối quan hệ với hoàng tộc và nhiều ứng cử viên lãnh chúa từ các lãnh địa xếp hạng hàng đầu," Matthias tiếp tục. "Xem xét việc ảnh hưởng của người sẽ giúp ích cho lãnh địa của chúng ta theo những cách mà trước đây không thể tưởng tượng được, tôi có thể đồng ý rằng việc trở thành một người dâng tên cho người là một bước đi danh giá và đáng giá, nhưng..." Cậu ấy dừng lại.

"Chúng ta vẫn chưa biết liệu ảnh hưởng đó có đảm bảo được quyền lực hay không. Tôi sẽ không nói điều này nếu cậu đang dâng tên của mình cho Ngài Sylvester hoặc Phu nhân Florencia, cặp đôi lãnh chúa, nhưng Tiểu thư Ro ze mai, Ngài Wilfried, và Tiểu thư Charlotte đều chưa đến tuổi trưởng thành, và chúng ta không biết tương lai có thể nắm giữ điều gì. Đó là lý do tại sao chúng ta không thể đủ khả năng để đưa ra những quyết định thiếu suy nghĩ như vậy, Roderick. Chúng ta sẽ mất đi cha mẹ của mình, và họ là chỗ dựa duy nhất mà chúng ta có ngay lúc này."
Roderick tái mặt. Đôi mắt của cậu ấy không yên và đảo từ Matthias sang tôi, nhưng tôi không nói gì.
"Hãy suy nghĩ thật cẩn thận, được chứ...?" Matthias kết luận, giọng nói của cậu ấy nhuốm một chút đắng cay. Hẳn là cậu ấy đã lặp đi lặp lại những lời đó rất nhiều lần rồi, và chúng mang một sức nặng khiến nó nghe hoàn toàn như thể cậu ấy thực sự đang tự nói với chính mình.

Chuyến Thăm Của Hirschur Và Lễ Thăng Cấp
Sau khi cảnh báo những đứa trẻ của phe Veronica cũ hãy suy nghĩ cẩn thận trước khi đưa ra bất kỳ quyết định cực đoan nào, tôi đã cho họ giải tán.
"Ta đã không biết về việc dâng tên cho đến khi Aub Ehrenfest nói với ta về nó, vì vậy vẫn còn nhiều điều ta muốn tìm hiểu. Liệu nó có phải là một điều mà một người nói chung sẽ muốn làm để đổi lấy việc đảm bảo có thêm ma lực không?" tôi hỏi, đưa mắt nhìn qua các tùy tùng của mình.
Bọn trẻ sẽ có thể tự do chọn phe cho riêng mình một khi chúng đến tuổi trưởng thành, và tôi không biết liệu phương pháp nén ma lực của tôi có đủ quan trọng để biện minh cho việc mạo hiểm cuộc sống của một người hay không.
Brunhilde lắc đầu. "Tôi không có ý định dâng tên của mình cho bất kỳ ai," cô ấy nói với nụ cười cao quý được mong đợi ở một quý tộc. "Tôi muốn tự mình đưa ra các quyết định, và tự quyết định con đường đi qua cuộc sống của chính mình. Chắc chắn người ta có thể đếm số lượng các quý tộc dâng tên trên một bàn tay, và tôi tin rằng lòng trung thành có thể được trao đi ngay cả khi không thực hiện một sự hy sinh như vậy."
Leonore đồng ý với đánh giá này. "Tôi cảm thấy rằng việc dâng tên được thực hiện tốt nhất không phải để thể hiện lòng trung thành của một người, mà là để bày tỏ tình yêu với người khác—để dâng tên của mình cho người thân yêu nhất của mình và đổi lại nhận được tên của họ, qua đó hình thành một lời thề vĩnh cửu về tình yêu trường tồn. Tuy nhiên, điều đó hầu như không thực tế. Tôi không tin rằng nó sẽ bao giờ xảy ra với tôi."
Ồ, tuyệt thật. Vậy là việc dâng tên cũng có thể được sử dụng một cách lãng mạn, nhỉ?
Tôi có thể hiểu điều đó trong bối cảnh tình yêu đôi lứa, nhưng tôi sẽ rất ghét việc ai đó mà tôi không có tình cảm lại cố gắng ép buộc điều đó lên tôi.
"Tôi đã tận mắt chứng kiến niềm vui mà anh trai Eckhart của chúng ta cảm thấy khi anh ấy giành được sự tin tưởng của Ngài Ferdinand thông qua việc dâng tên, và sự tuyệt vọng mà anh ấy cảm thấy khi anh ấy trú ẩn trong đền thờ," Cornelius nói. "Tôi không nghĩ tôi có thể dâng tên của mình cho ai đó sau khi thấy anh ấy đã suy sụp đến mức nào."

Phải rồi... Huynh ấy đã tận mắt nhìn thấy hậu quả của việc ai đó dâng tên của mình.
Hartmut gật đầu, rõ ràng là đồng ý với Cornelius, nhưng rồi anh ấy thản nhiên nói, "Tôi sẽ không bận tâm đến việc dâng tên của mình cho Tiểu thư Ro ze mai, nếu người khao khát điều đó."
Mọi người dường như hoàn toàn sửng sốt, lúc đó anh ấy mỉm cười và nói thêm, "Nhưng dĩ nhiên là người không muốn thế."
Ferdinand có thể đã cần một sự thể hiện lòng tận tụy cực đoan như vậy, nhưng đó là vì ngài ấy đã bị bủa vây bởi kẻ thù và thiếu đi bất kỳ ai ngài ấy có thể tin tưởng. Tôi có cha mẹ nuôi, cha mẹ ruột là thượng quý tộc, và một số người giám hộ đang chăm sóc cho tôi, thêm vào đó là các tùy tùng của tôi, những người mà tôi rất hòa thuận.
"Tiểu thư Ro ze mai không hề yêu cầu một lòng trung thành cuồng tín như vậy một chút nào, người cũng không hiểu được giá trị của việc nhận một cái tên," Hartmut tiếp tục. "Người cũng coi trọng ý chí tự do của người khác đến mức người cho phép ngay cả các xám y linh mục và vu nữ tự đưa ra quyết định của riêng mình. Thật khó để tưởng tượng rằng người sẽ đánh giá cao một sự thể hiện đại diện cho điều hoàn toàn ngược lại."
Hartmut đang giải thích tư duy của tôi cho các tùy tùng khác bằng những từ ngữ đơn giản. Anh ấy chính xác đến mức kỳ lạ, như thể anh ấy đã tìm ra cách nào đó để mổ xẻ những suy nghĩ của tôi, nhưng anh ấy đã đúng—tôi sẽ không muốn bất kỳ ai dâng tên của họ cho tôi.
"Wilfried, Charlotte, hai người có chấp nhận tên của những đứa trẻ đó không?" tôi hỏi, nhận thức được rằng họ cũng ở cùng hoàn cảnh với tôi lần này.
Wilfried gật đầu như thể câu trả lời đúng là quá rõ ràng.
"Tất nhiên rồi," huynh ấy nói. "Đó là nghĩa vụ của huynh với tư cách là chúa tể của họ. Huynh sẽ coi đó là một vinh dự khi có những người đủ trung thành đến mức sẵn lòng dâng tên của họ cho huynh," huynh ấy nói thẳng thừng, lưu ý rằng huynh ấy thậm chí sẽ chấp nhận cả những đứa trẻ của phe Veronica cũ.

"Muội cũng sẽ như vậy," Charlotte nói thêm, cũng gật đầu đồng ý. "Thực tế, muội thấy việc tỷ không làm thế mới là kỳ lạ hơn đấy, tỷ tỷ. Tỷ đã chấp nhận Philine, và tỷ đang gánh vác mạng sống của những đứa trẻ mồ côi trên vai mình với tư cách là giám đốc cô nhi viện. Chẳng phải sẽ dễ dàng hơn khi chấp nhận một lòng trung thành bị trói buộc bởi việc dâng tên so với một lòng trung thành chỉ dựa trên lời nói thôi sao?"
Đúng như những gì muội ấy nói—tôi đang bảo vệ các bình dân ở khu hạ lưu và hỗ trợ cuộc sống của tất cả những người trong cô nhi viện. Cũng đúng là Philine gần như đã ở vị trí của một người dâng tên rồi, xét đến việc tôi đang dành cho em ấy một sự đối xử đặc biệt như vậy. Tuy nhiên, em ấy chưa bao giờ thực sự dâng tên của mình cho tôi. Em ấy đã chọn phục vụ với tư cách là tùy tùng của tôi, nhưng tôi đã tự nguyện chúi mũi vào các vấn đề gia đình của em ấy. Vì vậy, tôi nghĩ đơn giản trách nhiệm của tôi là chăm sóc em ấy cho đến khi em ấy đến tuổi trưởng thành và có thể tự lập—hoặc, nếu cần thiết, cho đến khi em ấy kết hôn.
Tuy nhiên, tôi hầu như không biết bất kỳ đứa trẻ nào từ phe Veronica cũ, vì nền chính trị bè phái đã ngăn cản chúng tôi giao du với nhau. Một phần trong tôi nghi ngờ rằng điều này chỉ tương đương với việc họ bất hòa với cha mẹ mình và muốn bám víu vào tôi để thay thế. Tôi không thể hiểu làm thế nào mà họ lại không gây ra các rắc rối.
Sử dụng một sự tương tự, tôi giống như một giám đốc công ty, trong khi các bình dân và trẻ mồ côi là những nhân viên của tôi. Tôi đang chăm sóc Philine, người tương đương với một nhân viên ăn ở tại chỗ tự xoay sở mọi thứ bằng tiền lương của mình. Tôi cần phải chăm lo cho các nhân viên của mình một cách bình đẳng để mọi người đều có công việc và không ai bị đối xử bất công.
Trong khi đó, những đứa trẻ của phe Veronica cũ lại giống như nhân viên của một công ty hoàn toàn riêng biệt. Bằng cách dâng tên của họ cho tôi, họ đang chen ngang trước những nhân viên ăn ở tại chỗ của tôi và yêu cầu tôi nhận nuôi họ vào gia đình mình và cung cấp sự hỗ trợ cho họ. Tôi chắc chắn rằng việc đưa ra một yêu cầu như vậy đòi hỏi rất nhiều quyết tâm từ phía họ, nhưng tôi sẽ cần phải hy sinh rất nhiều để thực sự tiếp nhận họ.

"Nó không hoàn toàn đơn giản như vậy đối với tỷ..." tôi nói để đáp lại câu hỏi của Charlotte.
"Huynh nghĩ muội sẽ thấy họ đáng tin cậy hơn rất nhiều sau khi dâng tên so với việc họ chỉ đơn giản là yêu cầu được đổi phe," Wilfried lưu ý.
Tôi chỉ có thể đáp lại bằng một cái gật đầu lấp lửng.
Bây giờ khi tất cả các học sinh năm nhất đã chuyển đến và học sinh của mọi năm đã tập trung lại với nhau, bữa tối hôm nay sang trọng hơn một chút so với hôm qua. Ủy ban Nâng cao Điểm số chúng tôi đã chia mọi người thành các đội và công bố phần thưởng cho cuộc thi năm nay: công thức làm bánh tart. Tôi đã chọn ngẫu nhiên một món ăn không có trong sách công thức mà chúng tôi đang bán.
"Chính xác thì Tiểu thư Ro ze mai có bao nhiêu công thức nấu ăn vậy?!" một trong số các học sinh thốt lên.
"Chắc chắn lần này chúng ta sẽ thắng," một người khác nói. "Tôi có thể đảm bảo điều đó."
Khi thấy mọi người trở nên sôi nổi về việc học tập trong sảnh sinh hoạt chung hệt như những gì họ đã làm vào năm ngoái, tôi thở phào nhẹ nhõm. Bầu không khí nặng nề từ một lúc trước đã phai nhạt đi phần nào, và ngay cả những đứa trẻ của phe Veronica cũ cũng đang hòa nhập vào... Mặc dù tôi không thể nói chắc chắn liệu đây có chỉ là một cách để các quý tộc che giấu cảm xúc của họ hay không.
Ngày hôm sau, khi mọi người nhanh chóng tập hợp thành các đội và bắt đầu học tập, Hirschur đột ngột bước vào ký túc xá.
"Tiểu thư Ro ze mai, Ngài Wilfried, lễ thăng cấp và buổi họp mặt giao lưu sẽ diễn ra vào ngày mai, vậy mà ta không nhận được bất kỳ tin tức nào cho biết rằng tất cả các học sinh của Ehrenfest đều đã đến," bà ấy nói một cách gay gắt.
"Có ai được bảo phải báo cho bà ấy biết không...?" tôi hỏi với một cái nghiêng đầu.

Cornelius thở dài. "Đó không phải là một quy tắc rõ ràng, nhưng trong những năm trước, thượng quý tộc năm cuối nhất luôn liên lạc với Giáo sư Hirschur. Người có cấp bậc cao nhất được kỳ vọng sẽ làm điều này, vì vậy chúng tôi đã thống nhất là Ngài Wilfried vào năm nay. Phải không, Ignaz?" huynh ấy hỏi, liếc nhìn một học giả tập sự đang đứng phía sau Wilfried.
Ignaz nở một nụ cười rắc rối. "Thần đã quên báo cho Ngài Wilfried," cậu ấy nói. "Thành thật xin lỗi."
"Ignaz, cậu..." Wilfried định nói, nhưng rồi huynh ấy dừng lại. "Xin hãy tha thứ cho chúng tôi, Giáo sư Hirschur. Có vẻ như lỗi nằm ở chúng tôi ngày hôm nay."
Có điều gì đó về việc Wilfried nói lời xin lỗi khiến tôi cảm thấy kỳ lạ. Chắc chắn điều quan trọng là chúng tôi phải theo dõi đúng quy trình và phải chịu trách nhiệm khi chúng tôi thất bại, nhưng cảm giác không đúng khi Hirschur lại quá chỉ trích trong khi bà ấy thậm chí ngay từ đầu đã không ở trong ký túc xá.
Tôi liếc nhìn bà ấy ngay khi bà ấy nói, "Lần sau hãy cẩn thận hơn."
"Chẳng phải vấn đề lớn nhất là người giám sát ký túc xá của chúng ta đã không có mặt ở ký túc xá sao?" tôi hỏi. "Ta nói rằng những người giám sát khác vẫn ở lại ký túc xá kể từ lúc những học sinh đầu tiên bắt đầu đến chẳng lẽ không đúng sao?"
"Ồ, người không biết sao, Tiểu thư Ro ze mai? Flutrane và Heilschmerz chữa lành theo những cách của riêng họ," Hirschur trả lời với một nụ cười.
Đó là một cách nói uyển ngữ mà về cơ bản có nghĩa là "mỗi người đều có cách làm việc của riêng mình," vì vậy tôi có thể suy luận rằng bà ấy hoàn toàn không có ý định thay đổi cách làm của mình. Không thể làm được gì nhiều hơn, tôi chỉ đơn thuần nhún vai.
"Tiểu thư ấy chắc chắn là giống với Phu nhân Florencia..." Hirschur đột nhiên lẩm bẩm, mắt bà ấy dán chặt vào Charlotte.
Bà ấy sau đó di chuyển đến giữa phòng sinh hoạt chung và bắt đầu giải thích lịch trình ngày mai và bản chất mới của ký túc xá cho những học sinh mới. Tất cả đều giống hệt như năm ngoái.
""",

# Chunk 2: Lines 67-85
"""
"...Hơn nữa, lễ thăng cấp sẽ được tổ chức vào hồi chuông thứ ba ngày mai, và bữa trưa sẽ được phục vụ tại các buổi họp mặt giao lưu," Hirschur lưu ý, lúc này đã đi đến phần cuối bài phát biểu nhanh gọn của bà ấy. "Các bài học bắt đầu vào ngay ngày hôm sau. Ehrenfest hiện xếp hạng thứ mười, vì vậy hãy cẩn thận sử dụng các cánh cửa và căn phòng được đánh dấu phù hợp. Tất cả các bạn đều đã đạt được rất nhiều tiến bộ trong việc học tập của mình, và ta không kỳ vọng bất kỳ ai trong số các bạn sẽ gặp vấn đề trong lớp học, nhưng đừng quên báo cáo kết quả của mình. Có câu hỏi nào không?"
Một học sinh mở miệng, nhưng trước khi họ kịp nói gì, Hirschur tiếp tục.
"Tiểu thư Ro ze mai, ta có một vài câu hỏi dành cho người. Người có phiền đi cùng ta không?" bà ấy hỏi với một nụ cười. Đôi mắt màu tím của bà ấy lấp lánh dữ dội như của một loài động vật ăn thịt đang tập trung vào con mồi của mình.
Chà, tôi biết bà ấy có lẽ muốn hỏi về trang phục của Schwartz và Weiss, và những tài liệu nghiên cứu mà Ferdinand đã đưa cho tôi, nhưng mà... Thật dễ để đoán những gì Hirschur định nói—hay đúng hơn, thật khó để nghĩ ra bất cứ điều gì khác mà bà ấy sẽ muốn biết. Và vì tôi có một số thứ từ Ferdinand mà tôi được yêu cầu đưa cho bà ấy, tôi gật đầu.
"Tôi không phiền, nhưng xin hãy giữ nó ngắn gọn," tôi trả lời. "Không giống như Ferdinand, tôi không thể dành cả đêm để thảo luận những vấn đề này với bà."
"Nghiên cứu của ta chắc chắn sẽ phải chịu đựng nếu ta ốm yếu như người," Hirschur nói với một cái gật đầu.
Tôi ghen tị mới đúng... Tôi ước mình có thể dành cả đêm đắm chìm vào những gì làm tôi hứng thú như bà có thể làm.
Tôi ra hiệu bằng mắt cho Rihyarda đi lấy những tài liệu mà Ferdinand đã bảo tôi đưa cho Hirschur trước, và bà ấy nhanh chóng di chuyển để làm chính xác điều đó.

Ngẫu nhiên, để có một lượng lớn nguồn tài nguyên nhằm vắt kiệt các ân huệ từ Hirschur, tôi đã sắp xếp các tài liệu có độ khẩn cấp thấp hơn thành năm chồng, sẽ được ban phát từng cái một khi chúng tôi cần thêm sự giúp đỡ từ bà ấy. Tất cả những điều này đều nhờ có Justus, người mà sau khi biết về tình hình của ký túc xá, đã nhờ Ferdinand hỗ trợ trong việc nhờ đến sự giúp đỡ của Hirschur khi cần thiết.
"Bây giờ thì—ta muốn biết những vòng tròn ma thuật nào đã được sử dụng trong các bộ trang phục, và chúng đã được cải tiến như thế nào."
Hirschur không lãng phí chút thời gian nào để bắt đầu cuộc thẩm vấn của mình, rõ ràng là quá mất kiên nhẫn để chờ những bộ trang phục được mang đến cho bà ấy, nhưng tôi đã giao lại tất cả công việc kinh doanh nghiên cứu cho Ferdinand. Nói cách khác, có rất ít điều mà tôi thực sự có thể giúp bà ấy. Điều duy nhất tôi có thể nói để đáp lại hàng loạt câu hỏi của bà ấy là bà ấy có thể đi cùng chúng tôi khi chúng tôi đến thay quần áo cho hai con shumil.
"Người không hứng thú với việc nghiên cứu các vòng tròn ma thuật sao, Tiểu thư Ro ze mai?" Hirschur hỏi. "Không phải người được cho là đệ tử được đánh giá cao nhất của Ferdinand sao?"
"Ferdinand là người giám hộ của tôi, và mặc dù đôi khi ngài ấy đóng vai trò là một người hướng dẫn, tôi sẽ không nói rằng chúng tôi có mối quan hệ thầy trò khi nói đến nghiên cứu," tôi trả lời, không muốn bị tính là một trong những nhà khoa học điên rồ của Ehrenfest. Sự quan tâm của tôi là ở việc đọc sách hơn là thực hiện bất kỳ nghiên cứu thực tế nào. Việc biên soạn các tài liệu nghiên cứu và những thứ tương tự chắc chắn được chào đón, nhưng tôi không cảm thấy bất kỳ mong muốn nào để tự mình tạo ra những tài liệu như vậy.
"Tuy nhiên, tôi dự định trở thành một thủ thư, vì vậy tôi sẽ dốc hết sức mình vào việc nghiên cứu các ma cụ và vòng tròn ma thuật có thể đóng một vai trò quan trọng trong việc vận hành một thư viện. Điều đó làm tôi nhớ ra—Giáo sư Hirschur, khi nào chúng ta nên mang quần áo đến thư viện?"
"Tại sao không đơn giản là hỏi bằng ordonnanz?" Hirschur gợi ý.

Và thế là, tôi gửi một ordonnanz cho Solange, thông báo với bà ấy rằng những bộ trang phục mới đã hoàn thành và tôi muốn cung cấp ma lực cho các ma cụ. Bà ấy trả lời rằng thư viện sẽ mở cửa một khi các lớp học bắt đầu, lưu ý rằng tôi có thể đến vào bất kỳ lúc nào sau thời điểm đó.
"Thành thật xin lỗi vì đã để người phải chờ, thưa tiểu thư."
Rihyarda sớm quay trở lại với trang phục của Schwartz và Weiss. Hirschur ngay lập tức cầm chúng lên và bắt đầu kiểm tra kỹ lưỡng các vòng tròn ma thuật của chúng, dùng ngón tay lần theo chúng và tham khảo các tài liệu đi kèm với một biểu cảm giống như biểu cảm mà Ferdinand sẽ làm trong khi tự mình nghiên cứu.
Điều đó có nghĩa là bà ấy cũng đã quên mất sự tồn tại của tôi...
"Rihyarda, ta có thể dọn dẹp tủ sách không?" tôi hỏi.
"Tại sao không, tôi cho là vậy. Tôi hình dung bà ấy sẽ mất khá nhiều thời gian đấy."
Tôi quyết định dọn dẹp tủ sách với Rihyarda trong khi chờ đợi Hirschur gãi ngứa cơn thèm nghiên cứu của bà ấy. Tôi dành các ngăn kệ riêng biệt cho học sinh năm nhất, năm hai, hiệp sĩ tập sự, học giả tập sự, và người hầu tập sự, đảm bảo rằng mỗi kệ chứa sách giáo khoa liên quan đến các môn học tương ứng của họ. Điều này dường như là cách tiếp cận tốt nhất trong mắt tôi, vì những cuốn sách này sẽ được sử dụng nhiều nhất. Sau đó, tôi sắp xếp sách của riêng mình trong khi gán phân loại thập phân cho chúng. Ehrenfest có sự thiên vị rất lớn đối với các số thập phân cụ thể do hầu hết các sách in đều là tiểu thuyết, nhưng mục tiêu của tôi là một ngày nào đó sẽ in các bản sao của mọi cuốn sách trong các phòng sách của Ehrenfest.
Ngay cả tiếng chuông thứ tư cũng không đủ để làm Hirschur nhúc nhích. Ngay cả khi tôi cố gắng nói chuyện với bà ấy, bà ấy sẽ ngay lập tức trả lời rằng bà ấy đang bận, thậm chí không buồn ngước lên khỏi công việc của mình.
Cuối cùng, chúng tôi mặc kệ Hirschur và ăn trưa. Một số học sinh chuẩn bị đi thu thập vào buổi chiều, trong khi những người khác tiếp tục việc học của mình, nhưng tôi đã ở lại trong phòng sinh hoạt chung và đọc sách để ít nhất sẽ có ai đó ở đó khi bà ấy quay lại với thực tại.

"Thưa tiểu thư, thưa tiểu thư!" Rihyarda kêu lên, vỗ nhẹ vào vai tôi và gập cuốn sách của tôi lại.
Tôi giật mình ngước lên và thấy Hirschur đang nhìn xuống tay tôi với đôi mắt tò mò.
"Tiểu thư Ro ze mai, cuốn sách đó là gì vậy?" bà ấy hỏi.
"Một loại mới được làm bằng giấy Ehrenfest," tôi trả lời.
"Ta có thể xem nó được không?"
"Bà có thể đọc nó bao lâu tùy thích, miễn là bà đọc nó ở đây. Nó là tài sản của phòng sinh hoạt chung, và tôi sẽ không cho phòng thí nghiệm của bà mượn nó đâu," tôi nói, giải thích các quy tắc của tủ sách trong khi đưa bản sao cuốn Những câu chuyện ở Học viện Hoàng gia của tôi cho bà ấy.
Bà ấy lật qua nó, một nụ cười thích thú hình thành trên khuôn mặt bà ấy.
"Chà, chà... Ta có thể nói tất cả các câu chuyện trong cuốn sách này đều có cơ sở từ thực tế. Mặc dù số năm có sự khác biệt, nhưng ta có thể đoán ai đã kể câu chuyện nào khá dễ dàng."
"Chúng được viết dựa trên những tin đồn được thảo luận qua các bữa tiệc trà, vì vậy tôi tưởng tượng một giáo sư như bà sẽ biết chúng. Ngẫu nhiên... câu chuyện nào đến từ ai vậy?"
Tên của những người liên quan đã được thay đổi, tên của các lãnh địa cũng vậy, vì vậy trong khi ai đó có mặt ở Học viện Hoàng gia có thể nhận ra các câu chuyện, tôi không có cách nào để biết chuyện nào là của ai. Câu chuyện duy nhất tôi có thể xác định được là về Sylvester và Florencia.
"Ta thà không nói còn hơn, vì họ đã chọn cách giấu tên vì một lý do, và những câu chuyện này không chỉ hoàn toàn nói về Ehrenfest," Hirschur nói, tự cười cạc cạc khi đặt cuốn sách xuống. Sau đó, bà ấy cầm các tài liệu từ Ferdinand lên và rời khỏi phòng, trông đặc biệt hài lòng.
Được rồi, bây giờ tôi đang tò mò đây... Có câu chuyện nào trong số này là về Ferdinand không? Tôi nhớ mình đã nghe nói rằng Eckhart đã kể cho Mẹ rất nhiều về ngài ấy.

Khi Hirschur rời đi, đã đến lúc chuẩn bị cho lễ thăng cấp và các buổi họp mặt giao lưu. Chúng tôi tặng kẹp tóc cho các cô gái, hy vọng sẽ bảo đảm chúng trở thành một xu hướng và lan truyền chúng rộng hơn. Chúng là những chiếc kẹp tóc mà Brunhilde đã chọn và đặt hàng từ Thương hội Gilberta.
"Vì mục đích tiếp thị, ta yêu cầu các bạn đeo những chiếc kẹp tóc này không được thiếu sót trong lễ thăng cấp năm nay," tôi tuyên bố. "Chúng ta cũng sẽ phân phát rinsham, vì vậy hãy chắc chắn làm sạch tóc của các bạn vào ngày hôm trước."
Những đánh giá của Brunhilde rất hợp lý; những chiếc kẹp tóc nhiều màu trong hộp hoàn toàn phù hợp với màu tóc và vẻ ngoài của các cô gái. Tôi rất ấn tượng khi cô ấy có thể nắm vững phong cách của quá nhiều học sinh như vậy. Tôi có thể hiểu được việc biết những thông tin như vậy về những người thân cận với bạn, nhưng bất cứ điều gì hơn thế nghe có vẻ bất khả thi đối với tôi.
"Ôi chao, thật đáng yêu làm sao!"
"Không thể ngờ người có thể chuẩn bị nhiều kẹp tóc cùng lúc đến vậy, Tiểu thư Ro ze mai."
"Tất cả đều do Brunhilde làm. Cô ấy có con mắt khá sắc sảo khi nói đến thời trang," tôi trả lời. "Bây giờ, Wilfried... Chúng ta cũng sẽ phân phát một chút rinsham cho các chàng trai nữa."
"Không cần đâu. Huynh đã giữ một ít cho họ rồi," Wilfried nói.
Sylvester dường như đã chuẩn bị rinsham cho tất cả các nam sinh sau khi tham dự Hội nghị Lãnh chúa.
"Bản thân huynh không phải là người hâm mộ nó, vì nó khiến tóc huynh có mùi ngọt ngào, nhưng... không thể làm gì khác được."
"Ồ, nhưng không phải tất cả các loại rinsham đều có mùi ngọt ngào đâu," tôi giải thích.
Huynh ấy hẳn là chỉ chưa chọn những mùi hương kiềm chế hơn mà chúng tôi dành cho nam giới.
Wilfried nhăn mặt một chút. "Huynh được bảo phải sử dụng loại có mùi hương mạnh hơn để người khác dễ nhận thấy nó hơn. Huynh không muốn có mùi giống như một cô gái

theo sự lựa chọn đâu," huynh ấy trả lời, vẫy chai rinsham từ bên này sang bên kia. Tôi thấy một vài cậu bé khác cũng gật đầu đồng tình.
Đó là ngày diễn ra lễ thăng cấp và các buổi họp mặt giao lưu. Chúng tôi cần phải có mặt tại khán phòng vào hồi chuông thứ ba, vì vậy sau bữa sáng, chúng tôi mặc quần áo và khoác lên mình chiếc áo choàng hiển thị màu sắc của lãnh địa chúng tôi. Chúng tôi cũng đeo trâm cài nhận dạng của mình, điều đó rất quan trọng, bởi vì chúng tôi không thể quay trở lại ký túc xá nếu không có chúng.
"Tiểu thư Ro ze mai," Brunhilde nói. "Cornelius, Leonore, và Judithe sẽ là hiệp sĩ hộ vệ của người trong buổi họp mặt giao lưu. Tôi sẽ tháp tùng người với tư cách là người hầu, và Hartmut là học giả. Điều này có chấp nhận được không?"
Tôi gật đầu. Buổi họp mặt giao lưu sẽ có sự tham dự của hoàng tộc và các ứng cử viên lãnh chúa, vì vậy những tùy tùng có địa vị cao nhất của tôi được ưu tiên. Judithe, là trung quý tộc duy nhất đi cùng tôi, có vẻ hơi lo lắng về điều này. Nụ cười của em ấy cứng nhắc một cách bất thường.
"Tôi sẽ cố gắng hết sức để lấp đầy khoảng trống mà Angelica để lại," Judithe nói, giọng em ấy chỉ hơi run rẩy một chút.
"Không có gì phải lo lắng cả," tôi trả lời, cố gắng an ủi em ấy. "Sẽ không có bất kỳ sự cố nào xảy ra trong suốt buổi họp mặt giao lưu đâu."
Tôi hướng đến sảnh vào để thấy mọi người chủ yếu mặc những bộ trang phục màu đen cùng áo choàng và trâm cài của họ. Các cô gái đang đeo kẹp tóc với những màu sắc khác nhau, và một số người còn đeo hai cái cùng một lúc, giống như tôi.
"Tất cả đều rất hợp," Philine nói, chạm vào chiếc kẹp tóc của chính mình với một nụ cười nhẹ.
Bên cạnh tiền lương tập sự của em ấy, tôi đã trả tiền cho em ấy để sao chép và cho công việc của em ấy khi giúp đỡ Ferdinand cùng với những người khác trong phòng của ngài ấy, nhưng ngay cả như vậy, em ấy vẫn phải vật lộn để nuôi sống bản thân

mà không có bất kỳ cha mẹ nào để dựa dẫm vào. Em ấy chắc chắn không có tiền để mua các phụ kiện cho bản thân mình, nhưng tôi đã mua những chiếc kẹp tóc này bằng tiền của chính mình trong Lễ hội Thu hoạch. Rõ ràng, Philine thậm chí đã có thể chọn được chiếc mà em ấy muốn.
"Mặc dù, thành thực mà nói, tôi chỉ chọn một trong số vài cái mà Brunhilde đã chọn cho tôi. Tôi chưa bao giờ được phép mua đồ phụ kiện, ngay cả ở nhà, vì vậy tôi không biết làm thế nào để đánh giá những gì sẽ trông hợp với mình," Philine thừa nhận, một chút buồn bã bao trùm lấy nụ cười của em ấy.
"Chào buổi sáng, tỷ tỷ," Charlotte nói. Muội ấy tương tự cũng đang mặc áo choàng Ehrenfest và đeo trâm cài lên bộ trang phục màu đen của mình. Muội ấy cũng đang đeo hai chiếc kẹp tóc, và vì tóc của muội ấy sáng hơn tóc tôi, nên những bông hoa tối màu khá nổi bật trên mái tóc đó.
"Những thứ đó trông rất đáng yêu với muội, Charlotte. Muội thật sự đáng yêu quá," tôi nói.
"Ôi chao, nhưng tỷ còn đáng yêu hơn muội nhiều."
Charlotte đang phát triển với tốc độ nhanh hơn tôi, và khoảng cách giữa chúng tôi có lẽ đã giãn rộng kể từ năm ngoái. Chà... chắc chắn là vậy. Tôi chỉ đơn giản là đang phủ nhận điều đó. Bây giờ muội ấy phải nhìn xuống chỉ để giao tiếp bằng mắt với tôi, và nếu chúng tôi đi bộ cạnh nhau, mọi người sẽ nghĩ Charlotte là chị lớn, không nghi ngờ gì về điều đó.
Mình luôn có thể đứng thật thẳng... Có lẽ khi đó mọi người sẽ nghĩ mình là chị gái.
Tôi đã cố gắng đứng thẳng theo một cách có vẻ không quá rõ ràng, nhưng nó khiến đôi chân tôi chao đảo, và tôi sớm phải vật lộn để giữ cho bản thân đứng vững. Nó trở nên tệ đến mức các tùy tùng của tôi bắt đầu lo lắng cho sức khỏe của tôi, vì vậy tôi bỏ cuộc và đặt gót chân của mình trở lại mặt đất.
"Đến lúc phải đi rồi," Wilfried tuyên bố, mở cửa và dẫn các học sinh Ehrenfest ra ngoài.
Con số phía trên cánh cửa của chúng tôi chắc chắn lúc này đang hiển thị là "mười," và chúng tôi đã ở gần khán phòng hơn so với năm ngoái. Hồi đó, chúng tôi đã đối mặt với những chiếc áo choàng màu xanh lá cây sẫm, vì vậy thật kỳ lạ khi họ lại ở
""",

# Chunk 3: Lines 88-105
"""
phía sau chúng tôi vào lúc này. Ngay cả bên trong khán phòng, chúng tôi cũng đang đứng ở một vị trí khác, xa hơn rất nhiều so với trước đây.
"Ehrenfest chắc chắn đã tăng thứ hạng," một giọng nói vang lên khi chúng tôi lê bước vào vị trí.
"Có vẻ như tất cả bọn họ đều đang sử dụng rinsham..."
Tôi thở dài. Một số trong những lời lầm bầm đó được nói ra bằng những giọng điệu khó có thể coi là thân thiện. Đúng như những gì Sylvester đã dự đoán, sự ghen tị và cay đắng vì thứ hạng của chúng tôi tăng lên sẽ còn tồi tệ hơn so với năm ngoái.
Lễ thăng cấp không có gì đặc biệt khác so với năm ngoái—một nhân vật quan trọng đã nói chuyện một lúc, sau đó các giáo sư nói phần của họ. Mọi thứ khá giống như trước đây, vì vậy tôi chỉ đứng lặng lẽ và chờ nó kết thúc. Tôi có lẽ sẽ cần phải chú ý nhiều hơn vào năm sau khi tôi trở thành học sinh năm ba và bước vào các khóa học chuyên ngành của mình, nhưng với tư cách là một học sinh năm hai, tôi sẽ có các bài học thực hành và bài giảng ở cùng những nơi giống như năm ngoái, vì vậy tôi sẽ ổn nếu không lắng nghe.
Lễ thăng cấp nhàm chán đến kinh khủng cuối cùng cũng kết thúc, điều đó có nghĩa là đã đến lúc cho buổi họp mặt giao lưu căng thẳng hơn nhiều, nơi không được phép mắc bất kỳ sai lầm nào. Tôi vẫn không biết sự thay đổi về thứ hạng của chúng tôi sẽ tác động đến mọi thứ một cách đầy đủ như thế nào.
"Bây giờ các bạn sẽ được di chuyển đến các buổi họp mặt tùy theo địa vị của mình, nhưng hãy chú ý đứng gần các thành viên của lãnh địa mình," người diễn thuyết nói. "Các đàn anh đàn chị thuộc mọi địa vị, hãy chăm sóc cho các hậu bối của mình. Các hậu bối, các bạn biết rất ít, vì vậy hãy cẩn thận và tuân theo sự thông thái của các đàn anh đàn chị."
Cornelius là một học sinh năm sáu, năm lớn nhất của các học sinh, vì vậy huynh ấy đã đảm nhận một vị trí chỉ huy ở đây. Các tùy tùng của tôi chia nhau thành những người sẽ đi theo các hạ quý tộc, trung quý tộc, thượng quý tộc, và chúng tôi, những ứng cử viên lãnh chúa.

Chúng tôi rời khỏi khán phòng và di chuyển đến cùng những hội trường mà chúng tôi đã đến lần trước. Tôi bắt đầu đi đến căn phòng được biết đến với tên gọi là Đại Sảnh Nhỏ, và Charlotte vươn vai với một biểu cảm có phần căng thẳng khi chúng tôi bước đi.
"Đừng sợ, Charlotte. Tỷ ở đây cùng muội mà."
Cứ thoải mái dựa dẫm vào ta nhiều bao nhiêu tùy thích. Dù sao thì ta cũng là tỷ tỷ của muội mà. Tôi nắm lấy tay Charlotte và mỉm cười. Muội ấy chớp mắt ngạc nhiên vài lần, sau đó mỉm cười trong một giây.
"Đúng vậy. Tỷ cũng sẽ tham dự buổi này mà," muội ấy nói. "Muội cần phải luôn tỉnh táo..."
Sau khi đưa ra nhận xét này, Charlotte bước lên phía trước, một tia sáng kiên định trong đôi mắt màu chàm của muội ấy. Tôi rất vui khi thấy rằng bình luận của mình đã làm giảm bớt sự căng thẳng của muội ấy.
"Ngài Wilfried, Tiểu thư Ro ze mai, và Tiểu thư Charlotte từ Ehrenfest hạng Mười đã đến," một học giả đang đứng bên cửa thông báo.
Và với điều đó, chúng tôi được dẫn vào Đại Sảnh Nhỏ.
Tôi chú ý đến một dáng người nhỏ bé đang ngồi tại chiếc bàn lớn ở cuối phòng, nơi Anastasius đã ngồi vào năm ngoái.
Đó có thể là em trai của Vương tử Anastasius chăng?

Buổi Họp Mặt Giao Lưu Của Học Sinh Năm Hai
Nếu người đang ngồi ở vị trí của hoàng tộc ở cuối căn phòng là một thượng quý tộc của Vương hạt, ông ta đáng lẽ phải lớn tuổi hơn rất nhiều. Có vẻ an toàn để kết luận rằng cậu ấy thực sự là một vương tử.
Tuy nhiên, không ai nói với tôi rằng một vương tử sẽ đến tham dự cả. Tôi nghiêng đầu. Nếu những người giám hộ của tôi biết về điều này, tôi chắc chắn họ đã cảnh báo tôi hoặc ít nhất là bảo tôi phải cảnh giác.
Thay vì mặc màu đen như Học viện đã bắt buộc, dáng người nhỏ bé đó—từ "nhỏ bé" luôn tự động xuất hiện trong tâm trí tôi mỗi khi tôi nhìn thấy cậu ấy—được mặc màu đỏ và trắng, những màu sắc thần thánh của mùa đông. Cậu ấy ít nhất cũng đang khoác một chiếc áo choàng màu đen, để đánh dấu rằng cậu ấy đến từ Vương hạt, nhưng cậu ấy vẫn rất nổi bật. Ngay cả Anastasius cũng chủ yếu mặc màu đen, vì vậy tôi chưa bao giờ nghĩ đến việc hoàng tộc được phép phá vỡ quy định về trang phục.
"Đây là chỗ ngồi của mọi người," một người hầu nói.
Giống hệt như năm ngoái, Đại Sảnh Nhỏ có các bàn bốn người được xếp cách đều nhau một khoảng bằng nhau. Chúng tôi được đưa đến ba chiếc bàn dành cho Ehrenfest, lúc đó Wilfried ngồi vào vị trí của mình ở chiếc bàn bên trái tôi và Charlotte ngồi ở chiếc bàn bên phải tôi. Brunhilde kéo ghế ra cho tôi trước khi quay lại vị trí của mình, đứng phía sau tôi cùng với các hiệp sĩ hộ vệ của tôi. Trong khi đó, Hartmut ngồi bên cạnh tôi với tư cách là học giả của tôi.
"Hartmut, anh có biết rằng một thành viên của hoàng tộc sẽ tham dự vào năm nay không?" tôi hỏi bằng một giọng khe khẽ.
Anh ấy kín đáo lắc đầu. "Thần không biết, và có vẻ như chúng ta không phải là những người duy nhất. Nhiều lãnh địa khác có vẻ cũng ngạc nhiên không kém, vì vậy chúng ta có thể giả định rằng không có ai được thông báo."

Thật vui khi biết tôi không đơn độc trong sự thiếu hiểu biết của mình. Tôi luôn có cảm giác rằng mình đang bỏ lỡ những thông tin quan trọng, vì tôi không dành nhiều thời gian ở lâu đài, nhưng đó không phải là trường hợp ở đây.
"Tuy nhiên," Hartmut tiếp tục, "thần nhớ có những tin đồn trong Học viện Hoàng gia vào năm ngoái rằng một thành viên hoàng gia sắp được rửa tội. Mọi người nói đó là con trai của người vợ thứ ba của nhà vua, người em trai cùng cha khác mẹ của Vương tử Sigiswald và Anastasius. Nếu những tin đồn đó là sự thật, cậu ấy có lẽ chỉ mới được rửa tội vào mùa thu này."
"Cậu ấy đã được rửa tội trong năm nay sao?" tôi hỏi. "Vậy thì hẳn là phải có ai đó biết về cậu ấy chứ."
"Các quý tộc ở Ehrenfest ra mắt trong hội giao lưu mùa đông, nhưng hoàng tộc được chính thức ra mắt trong Hội nghị Lãnh chúa mùa xuân. Thần mong đợi rằng ngài ấy vẫn chưa có một buổi ra mắt chính thức nào."
Điều đó giải thích tại sao cậu ấy lại bé xíu như vậy. Tôi đã nghĩ rằng có thể trông cậu ấy nhỏ xíu vì cậu ấy ngồi ở quá xa, nhưng điều này thì hợp lý hơn nhiều. Nói là như vậy, nhưng tại sao ngay từ đầu lại có một vương tử mới được rửa tội ở đây cơ chứ? Hartmut chỉ khiến tôi thêm bối rối.
Rất may, một khi các ứng cử viên lãnh chúa từ tất cả các lãnh địa đã yên vị, một học giả của Vương hạt đã giới thiệu vị vương tử nhỏ bé và giải thích hoàn cảnh.
"Đây là Tam Vương tử Hildebrand," học giả nói. "Ngài ấy đã được rửa tội vào mùa thu này và được chào đón vào gia đình hoàng gia. Trong những hoàn cảnh bình thường, ngài ấy sẽ theo học Học viện muộn hơn nhiều, nhưng nhà vua đã hướng dẫn ngài ấy theo học vào năm nay như một phần trong các nghĩa vụ hoàng gia của ngài ấy."
Tóm lại, có một quy tắc là phải luôn có ít nhất một thành viên của gia đình hoàng gia đang theo học tại Học viện Hoàng gia. Nếu không có ai ở độ tuổi phù hợp, một người trưởng thành đã tốt nghiệp sẽ được cử đi thay thế. Sẽ là phù hợp hơn nếu Anastasius quay trở lại,

nhưng có vẻ như ngài ấy đang cực kỳ bận rộn với các nghĩa vụ của mình với tư cách là nhị vương tử. Ngài ấy cần phải lấp đầy ma lực cho vùng đất mà ngài ấy đã được ban cho nhờ cuộc hôn nhân của mình và các ma cụ của hoàng gia đã rơi vào tình trạng không được sử dụng.
Nói cách khác, Vương tử Anastasius đang quá háo hức muốn kết hôn với Tiểu thư Eglantine đến mức ngài ấy đang dồn hết sức mình vào việc chuẩn bị sẵn sàng cho vùng đất của mình và từ chối quay lại Học viện Hoàng gia.
Phải là vậy, đúng không? Ý tôi là, việc hồi sinh những ma cụ cũ đó phải là một công việc khó khăn hơn nhiều so với việc đóng quân tại Học viện. Bây giờ khi ngài ấy đã là một người trưởng thành, Anastasius đã chọn làm việc chăm chỉ suốt mùa đông thay vì ở lại Học viện Hoàng gia.
Kết quả là Hildebrand đã bị ném vào tình cảnh khó khăn nhất, phải theo học Học viện quá sớm sau lễ rửa tội của cậu ấy. Tuy nhiên, cậu ấy ở đây đơn thuần chỉ vì các lý do chính trị; không phải là cậu ấy sẽ thực sự đến các lớp học. Cậu ấy có lẽ sẽ dành phần lớn thời gian của mình trong chính phòng của mình.
Tôi tự hỏi tại sao quy tắc này lại được thiết lập... Có phải là dành cho các trường hợp khẩn cấp hay thứ gì đó không? Có thể để đảm bảo luôn có người ở đó để giải quyết các tranh chấp chăng? Năm ngoái, khi Dunkelfelger làm ầm ĩ lên vì việc tôi đưa Schwartz và Weiss ra khỏi thư viện, Anastasius đã được liên lạc và đến gần như ngay lập tức để làm trọng tài phân xử cho vụ tranh chấp. Ngài ấy sau đó cũng đã nói chuyện với Solange và tôi để tìm hiểu thêm về tình hình.
Chắc chắn là có rất nhiều người ở đây; ai biết được những loại vấn đề nào có thể phát sinh? Hoàng tộc hẳn phải bận rộn với những thứ này. Và để gia đình hoàng gia gửi một đứa trẻ bảy tuổi theo đúng nghĩa đen đến Học viện Hoàng gia, họ hẳn phải đang ở trong tình thế vô cùng khó khăn.
Khi thông báo của học giả đã kết thúc, mọi người chuẩn bị gửi lời chào của mình, giống như họ đã làm vào năm trước.
Một lần nữa, Klassenberg là người đầu tiên. Có vẻ như họ không có bất kỳ ứng cử viên lãnh chúa nào

bây giờ khi Eglantine đã tốt nghiệp, vì vậy một cậu bé trông có vẻ lớn tuổi hơn đã đứng dậy và thay vào đó đi đến chào vương tử. Sự kiện tiếp tục như dự kiến: những người đại diện của mỗi lãnh địa sẽ đứng lên chào hoàng tộc và sau đó đi xuống dọc bên cạnh để chào hỏi từng lãnh địa có thứ hạng cao hơn họ.
Dunkelfelger là người tiếp theo đi lên, sau đó là Drewanchel... Chỉ sau khi lãnh địa xếp thứ chín chào vương tử thì mới đến lượt chúng tôi.
Wilfried và Charlotte đứng dậy trong khi tôi được giúp bước xuống khỏi ghế của mình. Wilfried sau đó nhìn Charlotte và tôi.
"Ro ze mai. Charlotte. Đi thôi."
Wilfried hộ tống chúng tôi đến bàn của vương tử ở cuối hội trường, di chuyển đủ chậm để tôi có thể theo kịp. Khi chúng tôi đến chỗ Hildebrand, chúng tôi quỳ xuống, bắt chéo tay, và cúi đầu.
"Vương tử Hildebrand, liệu chúng tôi có thể cầu nguyện cho một lời chúc phúc để tri ân cuộc gặp gỡ tình cờ này, được định đoạt bởi sự phán xét khắc nghiệt của Thần Sự sống Ewigeliebe không?"
"Các người có thể," một giọng nói trẻ con đặc trưng vang lên.
Khi đến gần, tôi có thể thấy Hildebrand có đôi mắt màu tím sáng và một chút sắc xanh nhạt trên mái tóc màu bạc của mình. Cậu ấy cũng có một khuôn mặt dễ thương. Có lẽ một cậu bé sẽ không đánh giá cao việc được gọi là dễ thương, nhưng cậu ấy trông đặc biệt trẻ—đúng như dự đoán, xét đến việc cậu ấy đã bị gửi đến Học viện Hoàng gia quá sớm.
Chưa kể, không giống như biểu cảm ngạo mạn về uy nghiêm của hoàng gia mà Anastasius vẫn thường trưng ra, Hildebrand đang nở một nụ cười tươi sáng thực sự khiến tôi cảm thấy nhẹ nhõm. Cậu ấy khác xa so với nguyên mẫu của một người đàn ông đặc biệt nam tính.
""",

# Chunk 4: Lines 109-125
"""
Với sự cho phép của vương tử, chúng tôi rót ma lực vào nhẫn của mình và ban một lời chúc phúc. Tôi đảm bảo chỉ thêm vào một chút ma lực, đồng thời quan sát Wilfried và Charlotte để chắc chắn rằng mình không làm quá đà. Ferdinand đã khăng khăng yêu cầu tôi không được nhượng bộ trước cảm xúc của mình và ban ra một lời chúc phúc quá mức như tôi đã làm trong lễ tốt nghiệp.
Được rồi. Hoàn hảo.
Tôi tự gật đầu với chính mình, đã thành công trong việc đưa ra một lời chúc phúc nhỏ như của các anh chị em mình.
Hildebrand sau đó bảo chúng tôi ngẩng đầu lên, lúc này Wilfried tiếp tục lời chào hỏi.
"Thật vinh dự khi được gặp ngài, Vương tử Hildebrand. Chúng tôi là Wilfried, Ro ze mai, và Charlotte của Ehrenfest, đến đây để học hỏi nhằm trở thành những quý tộc đúng mực phù hợp để phục vụ Yurgenschmidt. Mong cho tương lai sẽ luôn tươi sáng."
Hildebrand nhìn từng người chúng tôi theo thứ tự, mặc dù cậu ấy có vẻ quan sát Charlotte với sự chú ý đặc biệt.
"Ta được kể rằng các ứng cử viên lãnh chúa của Ehrenfest rất xuất sắc—rằng một người đứng đầu lớp và một người khác đạt danh hiệu học sinh danh dự, tất cả trong khi giúp đỡ các bạn cùng lớp của họ trong việc nâng cao điểm số tổng thể của lãnh địa," cậu ấy nói một cách dứt khoát bằng giọng the thé của mình. "Quốc vương Trauerqual đặt nhiều hy vọng vào tất cả các bạn. Hãy tiếp tục những nỗ lực của mình."
Tôi có thể cảm nhận được rằng cậu ấy đang hoàn toàn tập trung vào việc lặp lại chính xác những lời mà những người lớn đã hướng dẫn cậu ấy nói, và với tư cách là một người đã từng ghi nhớ đủ loại cụm từ cho các buổi lễ, tôi biết cậu ấy hẳn đã phải làm việc chăm chỉ như thế nào để đạt được điểm này. Tôi muốn nói với cậu ấy rằng cậu ấy đang làm rất tốt và hãy tiếp tục phát huy, nhưng nói điều đó với một vương tử thì có vẻ thô lỗ. Thay vào đó, tôi quyết định dùng một biểu hiện của lòng biết ơn.
"Chúng tôi cảm ơn ngài."

Và thế là, cuộc gặp đầu tiên của chúng tôi với Hildebrand đã kết thúc mà không có sự cố nào. Thú thực thì điều đó khiến tôi hơi mất cảnh giác, vì Anastasius đã lớn tiếng trước mặt tôi về việc tôi là một "vị thánh giả" vào năm trước, nhưng dù sao thì chúng tôi cũng tiến đến chiếc bàn tiếp theo—chiếc bàn thuộc về Klassenberg.
"Một lần nữa, Nữ thần Thời gian Dregarnuhr đã đan các sợi chỉ của chúng ta lại với nhau và ban phước cho chúng ta bằng một cuộc gặp gỡ. Đây là Charlotte, em gái út của tôi. Em ấy đang theo học tại Học viện Hoàng gia với tư cách là học sinh năm nhất," Wilfried nói. "Mong cho tương lai của chúng ta sẽ luôn tươi sáng."
Charlotte tiếp tục đưa ra những lời chào hỏi đầu tiên của muội ấy. Wilfried đã không tự giới thiệu bản thân, và tôi cũng đã được bảo là không nên tự giới thiệu, vì vậy tôi chỉ có thể cho rằng chúng tôi đã tự giới thiệu bản thân với người này vào năm ngoái. Có lẽ họ là một ứng cử viên lãnh chúa chứ không phải là một thượng quý tộc.
Tôi không thể hỏi chính xác họ là ai, vì vậy tôi sẽ chỉ kiểm tra lại với Hartmut sau. Theo Hartmut, họ không phải là thượng quý tộc, mà đúng hơn là con trai của người vợ thứ hai của Aub Klassenberg. Anh ấy giải thích rằng tôi đã chào hỏi cậu bé đó vào năm ngoái, nhưng tôi hoàn toàn không thể nhớ ra cậu ấy, vì vậy tôi chỉ đáp lại bằng một nụ cười đơn giản.
Ý tôi là, làm sao tôi có thể nhớ được một người mà tôi mới chỉ chào hỏi đúng một lần chứ? Đặc biệt là khi tôi chưa bao giờ thực sự mong đợi sẽ gặp lại họ.
"Việc Tiểu thư Eglantine không giới thiệu lại cậu ấy với người mặc dù hai người có mối quan hệ thân thiết, có thể là trường hợp chính cô ấy cũng không tương tác với cậu ấy. Không có gì lạ khi con của một người vợ thứ hai lại hiếm khi giao du."
Ồ, đúng rồi. Điều đó làm tôi nhớ lại... Tôi gần như chưa bao giờ nói chuyện với Nikolaus.

Các gia đình thượng quý tộc và gia đình lãnh chúa nói chung thường lấy những người vợ thứ hai để ổn định chính trị bè phái, đền bù cho một người vợ cả không có khả năng sinh con, hoặc chỉ đơn giản là tăng số lượng con cái của họ. Việc những anh chị em cùng cha khác mẹ hiếm khi tương tác với nhau không phải là chuyện hiếm.
Lãnh địa tiếp theo mà chúng tôi sẽ chào hỏi là Dunkelfelger. Chúng tôi tiến đến bàn của Lestilaut và Hannelore, nơi Wilfried nói chuyện với họ với tư cách là người đại diện của chúng tôi và Charlotte thực hiện lời chúc phúc được đưa ra trong các cuộc gặp mặt đầu tiên.
"Tiểu thư Hannelore," tôi nói, "vô cùng cảm ơn người vì cuốn sách tuyệt vời của Dunkelfelger mà người đã cho tôi mượn. Ngay cả aub cũng nhờ tôi bày tỏ lời cảm ơn của ngài ấy đến người."
Tôi kể cho cô ấy nghe tôi đã sửng sốt như thế nào khi biết rằng chính Aub Dunkelfelger đã giao cuốn sách tại Hội nghị Lãnh chúa, nhưng đồng thời, tôi đã biết ơn như thế nào vì việc nó được gửi đến sớm như vậy có nghĩa là tôi có rất nhiều thời gian để đọc nó.
Hannelore chớp mắt vài lần. "Chắc hẳn người đã phải đứng tim khi nhận được một cuốn sách từ chính aub. Phụ thân thích làm mọi người ngạc nhiên, và, ừm... tôi thường thấy mình toát mồ hôi lạnh sau một trong những trò đùa của người. Tôi thấy nhẹ nhõm vì người đã không làm phiền người," cô ấy nói với một nụ cười đầy rắc rối, hai bím tóc màu hồng nhạt của cô ấy đung đưa khi cô ấy chuyển động.
Aub Dunkelfelger dường như đã tuyên bố rằng ngài ấy sẽ đích thân giao cuốn sách để làm tôi ngạc nhiên. Ngài ấy nghe có vẻ giống như một người thích sự tinh nghịch, nhưng để ngài ấy cho chúng tôi mượn một cuốn sách cũng có thể được coi là một báu vật của lãnh địa họ, ngài ấy có lẽ cũng là một người thực sự tốt.
"Việc được tặng một cuốn sách không bao giờ có thể làm phiền tôi," tôi trả lời. "Tôi đã có khoảng thời gian tuyệt vời với nó, và để cảm ơn, Tiểu thư Hannelore, tôi dự định cho người mượn một cuốn sách từ Ehrenfest. Tôi nghĩ sẽ rất tuyệt nếu chúng ta có thể trao đổi những cuốn sách mới khi trả lại những cuốn chúng ta đã đọc."

"Tôi vô cùng cảm ơn người, Tiểu thư Ro ze mai. Tôi đang rất mong chờ điều đó."
Hannelore và tôi trao đổi một nụ cười, tận hưởng cuộc trò chuyện thú vị của chúng tôi, lúc này Lestilaut nhìn tôi với vẻ mặt đầy nghi ngờ.
"Một ai đó ở Ehrenfest đã xoay sở đọc được cuốn sách đó sao?" cậu ấy hỏi.
"Đúng vậy. Tôi đã kinh ngạc trước chiều sâu quá khứ của lãnh địa các ngài," tôi trả lời. Thực tế là rất nhiều câu chuyện của họ liên quan đến những kẻ cuồng chiến, những người tiếp tục chiến đấu cho đến khi họ giành chiến thắng ít nhiều đã giải thích tại sao Giáo sư Rauffen lại khăng khăng thách thức chúng tôi tham gia vào các trận tái đấu ditter như vậy—thầy ấy có quá nhiều lịch sử ở phía sau mình.
"Hmph. Nên là như vậy," Lestilaut khịt mũi. "Chúng ta hoàn toàn không giống Ehrenfest, một lãnh địa thảm hại chỉ với vỏn vẹn hai trăm năm lịch sử."
"Ca ca!" Hannelore kêu lên và đưa cho cậu ấy một cú giật mang tính khiển trách vào tay áo của cậu ấy. Sau đó, cô ấy nhìn tôi; đôi mắt màu đỏ dễ thương của cô ấy tràn ngập sự lo lắng. Cô ấy chắc chắn đang lo lắng rằng Lestilaut đã xúc phạm tôi, nhưng tôi chỉ mỉm cười với cậu ấy và gật đầu.
"Sự thật là lịch sử của lãnh địa chúng tôi nhạt nhòa khi so sánh với lãnh địa của các người và những cuốn sách lịch sử của chúng tôi thì mỏng manh hơn nhiều khi đem ra so sánh," tôi nói. "Đó là lý do tại sao tôi rất cảm kích cuốn sách mà tôi đã tử tế được cho mượn, và tôi chắc chắn sẽ rất thích đọc thêm những cuốn sách tuyệt vời của Dunkelfelger."
Dự định của tôi là dẫn đến một cuộc thảo luận dài hơi, trong thời gian đó tôi có thể đánh giá về cuốn sách của Dunkelfelger và có được nhiều sách hơn từ họ, nhưng Wilfried đã ngắt lời tôi và Charlotte khéo léo kéo nhẹ tay áo của tôi.
"Có lẽ điều này có thể được thảo luận khi chúng ta đến cho Dunkelfelger mượn cuốn sách của mình," Wilfried nói. "Chúng ta không nên chần chừ quá lâu khi có những người khác đang chờ đợi."
Ồ, đúng rồi... Chúng tôi đang ở giữa cuộc chào hỏi các lãnh địa.

Tôi đã quá hào hứng khi được đoàn tụ với Hannelore và quá háo hức muốn nói chuyện với cô ấy đến mức tôi đã quên mất mình đang ở đâu. Tôi hứa sẽ mời cô ấy đến một bữa tiệc trà sớm và sau đó tiến đến bàn của Drewanchel.
"Ngài Wilfried, Tiểu thư Ro ze mai, tôi chúc mừng hai người về việc đính hôn," Adolphine nói. "Tôi đã nghi ngờ đôi tai của mình khi Phụ thân trở về từ Hội nghị Lãnh chúa cùng với tin tức này."
Adolphine đang phát biểu với tư cách là người đại diện của lãnh địa, nhưng cũng đi cùng với cô ấy là Ortwin, người bạn cùng lớp của tôi và hai ứng cử viên lãnh chúa khác. Mái tóc màu đỏ rượu vang chảy xuống ngực cô ấy thành những gợn sóng uy nghi có độ bóng mượt dễ chịu, gần như thể cô ấy đã sử dụng rinsham. Sự quan sát cẩn thận đối với các học sinh khác của lãnh địa cho thấy tất cả bọn họ cũng đều có mái tóc bóng mượt.
Khi thấy mắt tôi di chuyển, Adolphine vuốt ve mái tóc của mình và mỉm cười.
Không, không thể nào... Mình chỉ cho họ một chai thôi mà. Họ hẳn đã phân tích loại rinsham mà tôi đã đưa cho họ tại bữa tiệc trà. Quy trình thực tế để làm ra nó rất đơn giản, vì vậy tôi đã đoán ra rằng phương pháp sản xuất cuối cùng cũng sẽ bị lộ, nhưng chuyện này diễn ra sớm hơn nhiều so với những gì tôi dự kiến. Việc Drewanchel là một lãnh địa của các nhà khoa học điên rồ có thể chỉ khiến nó trở nên đáng sợ hơn một chút so với những gì tôi dự kiến.
Tôi ngước lên nhìn Adolphine và nuốt nước bọt cái ực. Trong khi đó, Wilfried và Ortwin dường như đang có một cuộc trò chuyện tích cực hơn nhiều, nói về các trò chơi mà họ đã chơi để giao lưu.
"Nâng ly cho một năm tốt lành nữa nhé, Wilfried?"
"Cậu có thể cá về điều đó. Tôi sẽ cho cậu thấy tôi đã chơi gewinnen giỏi hơn bao nhiêu."
Vì một lý do nào đó, Adolphine đang nở một nụ cười đầy ẩn ý với tôi.
"Tiểu thư Ro ze mai, những học giả mà chúng tôi gửi đến Hội nghị Lãnh chúa

đã trở về trong một trạng thái phấn khích khá điên cuồng," cô ấy nói. "Có vẻ như Ehrenfest có những ma cụ mà ngay cả bình dân cũng có thể sử dụng—những mảnh giấy vụn tự di chuyển, uốn éo tìm đường đến với bất kỳ mảnh nào lớn hơn. Khá thú vị. Ngay cả các học giả của chúng tôi cũng bị sửng sốt bởi khái niệm này."
"Ồ, đó không phải là thứ gì đáng để được chú ý nhiều như vậy đâu," tôi trả lời với một tiếng cười khúc khích lảng tránh. Tôi bắt đầu cảm thấy họ sẽ mổ xẻ bất cứ thứ gì họ tìm cách chạm tay vào được.
"Tôi không quan sát thấy bất kỳ loại giấy nào như vậy trong Học viện Hoàng gia, và nó cũng không được trình bày tại Giải đấu Liên Lãnh địa, phải không?" Adolphine hỏi. "Có thể có một lý do nào đó cho chuyện này chăng?"
"Có lẽ là do aub của chúng tôi coi nó không xứng đáng để được công khai," tôi trả lời.
Nó không có mặt tại Giải đấu Liên Lãnh địa vì nó do các bình dân tạo ra, và không ai ở Ehrenfest thực sự coi nó là một ma cụ. Tuy nhiên, tôi không thể nói điều đó!
"Thật khó một cách đáng ngạc nhiên để nắm bắt được điều gì là bình thường và không bình thường ở lãnh địa của một người," Adolphine nói. "Đây là điều mà tôi đã học được rất rõ kể từ khi đến Học viện Hoàng gia. Tiểu thư Ro ze mai, tôi cầu nguyện rằng chúng ta có thể dành nhiều thời gian bên nhau trong năm nay."
Hay nói cách khác, người muốn vắt kiệt thông tin từ tôi chứ gì? Được thôi. Đã đến lúc liên lạc với những người giám hộ của mình. Chuyện đó chẳng mất bao lâu.
"Tôi xin chia sẻ những lời cầu nguyện của người," tôi nói với một nụ cười, nhưng tôi có thể cảm nhận được khuôn mặt mình đang cứng lại.
Mắt của Adolphine chuyển sang dừng lại ở Charlotte một khoảnh khắc trước khi nhìn sang Ortwin theo kiểu so sánh.
"Cô là học sinh năm nhất, phải không, Tiểu thư Charlotte?" Adolphine hỏi. "Tôi có thể thấy trước chúng ta cũng sẽ trở thành những người bạn thân thiết."
"Tôi sẽ rất vinh dự."
""",

# Chunk 5: Lines 127-145
"""
Có cảm giác như một ai đó cực kỳ nguy hiểm vừa nhắm vào Charlotte vì một điều gì đó!
Á á! Ferdinand! CỨU VỚI!
Tôi di chuyển đến bàn tiếp theo, hy vọng bảo vệ Charlotte khỏi ánh nhìn của Adolphine.
Một khi chúng tôi đã hoàn thành việc chào hỏi lãnh địa thứ tư và thứ năm, đã đến lúc chúng tôi nói chuyện với Ahrensbach thứ Sáu. Chỉ có Detlinde ở đó với tư cách là ứng cử viên lãnh chúa. Cô bé nhỏ nhắn mà chúng tôi đã thấy trong đám cưới của Lamprecht không có mặt ở đó; cô bé ấy nhỏ xíu chừng tôi, vì vậy đúng như dự đoán, cô bé ấy chưa đủ tuổi để theo học Học viện vào năm nay.
"Đã quá lâu rồi kể từ cuộc đoàn tụ cuối cùng của chúng ta," Detlinde nói. "Tất cả các người có vẻ đều đang làm tốt. Aurelia vẫn đang sống tốt ở Ehrenfest chứ? Chúng tôi đã rất lo lắng rằng chị ấy có thể không hòa nhập được, đúng không nào, Martina?"
Cô ấy chuyển sự chú ý sang một cô gái trông hơi giống Tuuli—tùy tùng của cô ấy, dựa trên vị trí mà cô gái đó đang đứng.
"Tiểu thư Bettina dường như vẫn giữ liên lạc, nhưng chúng tôi không nghe thấy tin tức gì từ tỷ tỷ Aurelia của mình cả. Tôi đã rất lo lắng cho chị ấy," Martina nói, buồn bã cụp mắt xuống.
Cô ấy đủ giống Tuuli đến mức chỉ cần nhìn thấy cô ấy buồn bã cũng khiến trái tim tôi đau nhói.
"Aurelia đang tận hưởng cuộc sống của cô ấy ở Ehrenfest," tôi nói. "Cô ấy đã chuẩn bị một chiếc mạng che mặt mới, và chúng tôi đã cùng nhau uống trà. Có đúng vậy không, Charlotte?"
"Quả thực vậy," Charlotte đồng ý với một nụ cười, muội ấy đã gặp Aurelia tại cuộc thi nhuộm. "Chị ấy là một người ngọt ngào và vô cùng đáng yêu."
Martina đặt một tay lên ngực mình trong sự nhẹ nhõm, trong khi Detlinde chớp mắt vài lần, đôi mắt màu xanh lá cây sẫm phản bội lại sự kinh ngạc của cô ấy.
"Aurelia á? Ngọt ngào sao?" cô ấy tự lẩm bẩm.
Tại sao điều đó lại gây ra sự ngạc nhiên đến vậy? Ở thế giới nào mà Aurelia lại không ngọt ngào chứ? Tôi cũng chớp mắt trong bối rối, cảm nhận được rằng Aurelia mà chúng tôi biết bằng một cách nào đó khác với người mà Detlinde quen thuộc.

"Về điều đó," Detlinde nói, nhanh chóng chuyển chủ đề, "Tôi nhận ra mình đã không chúc mừng một cách đúng mực lễ đính hôn của các người tại Lễ Kết Tinh. Xin hãy cho phép tôi sửa chữa điều đó. Xin chúc mừng."
Cô ấy nói với một nụ cười nhẹ nhàng, điều này nói giảm nói tránh thì đúng là kỳ lạ. Cảm giác như thể cô ấy đang thực sự chúc phúc cho việc đính hôn của chúng tôi, và cô ấy trông thân thiện đến mức tôi muốn hỏi tất cả những điều vô nghĩa vào năm ngoái là về cái gì. Việc cô ấy thậm chí còn thừa nhận tôi bên cạnh Wilfried dường như không thể hiểu nổi, và nói thật, nó thực sự khiến tôi cảm thấy hơi khó chịu.
"Tất cả các người đều là anh em họ của tôi ở Ehrenfest," cô ấy tiếp tục. "Tôi hy vọng rằng chúng ta có thể hòa thuận với nhau."
Lãnh địa thứ bảy, thứ tám, và thứ chín theo sau Ahrensbach rõ ràng đã đề phòng chúng tôi, xét đến việc thứ hạng của chúng tôi đã tăng quá đột ngột. Họ hầu như không để ý đến chúng tôi vào năm ngoái, nhưng bây giờ họ đang bắn cho chúng tôi những lời cảnh báo và xúc phạm chúng tôi thông qua những từ ngữ uyển ngữ.
Rất tiếc phải nói với các người, nhưng Wilfried sẽ không hề nhận ra những kiểu coi thường đó đâu. Và chúng cũng sẽ không khiến tôi chùn bước đâu!
Chúng tôi hoàn thành việc chào hỏi các lãnh địa có thứ hạng cao hơn, điều đó có nghĩa là đã đến lúc các lãnh địa có thứ hạng thấp hơn bắt đầu chào hỏi chúng tôi. Điều này cũng gây phiền nhiễu theo cách riêng của nó. Lãnh địa thứ mười một, mười hai, và mười ba đặc biệt thù địch với chúng tôi và nói chuyện với những nụ cười sáo rỗng, vì chúng tôi đã đẩy tất cả họ xuống trong quá trình thăng tiến của mình.
Để dịch một vài lời lăng mạ của họ:
"May mắn và cơ hội không kéo dài mãi mãi."
"Thời kỳ tốt đẹp chỉ là những ảo ảnh mong manh—sớm muộn gì chúng cũng sẽ tan vỡ."
"Các người lại định tăng tốc qua các lớp học của mình một lần nữa sao? Tôi chỉ hy vọng rằng điểm số của các người không phải chịu đựng như trước đây."

Thật dễ chịu làm sao. Tất nhiên, chúng tôi cần phải bảo vệ nhân phẩm và danh tiếng của mình, vì vậy chúng tôi đã đưa ra những câu trả lời có ý nghĩa đại loại như, "Thành công của chúng tôi không phải là một ảo ảnh; chúng tôi sẽ đảm bảo những thời kỳ tốt đẹp sẽ tiếp tục."
"Chúng tôi cảm ơn sự khích lệ của các người," tôi nói với một trong những học sinh đang chào hỏi chúng tôi. "Xin hãy mong đợi được nhìn thấy điểm số của chúng tôi được công bố; tôi tin rằng các người sẽ thấy chúng có tác động khá lớn đấy."
Sau khi trao đổi nhiều lời lăng mạ khác với nụ cười trên môi, đã đến lúc chúng tôi nói chuyện với Frenbeltag.
Đây là lần đầu tiên Charlotte gặp Rudiger. Đôi mắt muội ấy mở to kinh ngạc, và muội ấy liếc nhìn nhiều lần giữa anh ấy và Wilfried, có lẽ là đang lưu ý xem họ trông giống nhau như thế nào. Tuy nhiên, vì Charlotte cũng có đôi mắt màu chàm giống như Rudiger, muội ấy dường như còn giống anh ấy hơn cả việc anh ấy giống với Wilfried—ít nhất là xét từ góc độ màu sắc. Tôi chắc chắn rằng muội ấy có thể dễ dàng cho mình là em gái của anh ấy.
Dù vậy tôi thì không. Tôi không có chung huyết thống với họ.
Rudiger hẳn đã nhận ra cách Charlotte đang nhìn mình vì anh ấy nở một nụ cười. Anh ấy quỳ xuống, bắt chéo tay, và sau đó cúi đầu.
"Ngài Wilfried, Tiểu thư Ro ze mai. Một lần nữa, Nữ thần Thời gian Dregarnuhr đã đan các sợi chỉ của chúng ta lại với nhau và ban phước cho chúng ta bằng một cuộc gặp gỡ. Và cũng như vậy đối với người, Tiểu thư Charlotte. Liệu tôi có thể cầu nguyện cho một lời chúc phúc để tri ân cuộc gặp gỡ tình cờ này, được định đoạt bởi sự phán xét khắc nghiệt của Thần Sự sống Ewigeliebe không?"
"Ngài có thể."
Rudiger ban cho Charlotte một lời chúc phúc và trao đổi những lời chào hỏi với muội ấy. Sau đó, một khi chuyện đó đã xong, anh ấy nhìn Wilfried.
"Huynh nghe nói về việc các ứng cử viên lãnh chúa của lãnh địa muội đang dẫn đầu trong Lễ Cầu Nguyện Mùa Xuân vì lợi ích của

người dân và đã đề nghị chúng ta làm điều tương tự ở Frenbeltag. Kết quả là, chúng ta đã có thể bảo đảm một vụ thu hoạch lớn hơn bình thường," anh ấy nói.
Rõ ràng là Rudiger đã phải lấy hết can đảm mới dám nói với gia đình rằng anh ấy muốn đến đền thờ, nhưng sau khi nghe nói rằng Wilfried đã làm điều tương tự ở Ehrenfest và đạt được kết quả tuyệt vời, cặp đôi lãnh chúa đã quyết định thử xem sao—nếu không vì điều gì khác thì có lẽ là vì quá tuyệt vọng.
Dù sao thì mẹ của Rudiger cũng là chị gái của Sylvester... Ít nhất thì mình cũng có thể nhìn thấy những điểm tương đồng giữa họ, một chút.
Nhờ những nỗ lực mới này, Frenbeltag rõ ràng đã có một vụ mùa bội thu hơn, và doanh thu thuế tăng lên đã giúp mọi thứ trở nên dễ dàng hơn cho lãnh địa.
"Hy vọng đã trở lại trong đôi mắt từng u ám của các quý tộc chúng ta," Rudiger nói với một nụ cười nhẹ, đầy hài lòng. "Điều đó mang lại cho huynh nhiều niềm vui hơn bất cứ điều gì khác. Rất trân trọng lời khuyên của các đệ muội. Mẫu thân cũng đã vô cùng vui mừng."
Là một lãnh địa thuộc phe thua trận trong cuộc nội chiến, tôi biết rằng aub của họ đã bị hành quyết, nhưng lãnh địa của họ chắc chắn cũng phải gánh chịu những bề chìm khác nữa. Lấy một ví dụ, tôi nhận thức được việc Aurelia bị đối xử khắc nghiệt một cách vô lý ở Ahrensbach do mẹ của cô ấy đến từ Frenbeltag. Điều này không nghi ngờ gì đã khiến việc đưa những người vợ và những người chồng vào lãnh địa trở nên khó khăn hơn rất nhiều.
Thực tế, thật ấn tượng khi họ đã xoay sở để từ bỏ cái tôi của mình và tham gia vào các buổi lễ tôn giáo. Tôi đã háo hức lao vào đền thờ để nhúng tay vào sách, nhưng họ đã coi thường nó suốt cả cuộc đời mình. Chắc chắn rồi, quyết định làm việc với đền thờ của họ bất chấp sự khinh miệt có lẽ là vì họ quá tuyệt vọng—đang chết đuối thì vớ được cọng rơm, như người ta thường nói—nhưng dù sao thì vẫn vậy.
"Huynh hy vọng rằng tình bạn của chúng ta với Ehrenfest có thể tiếp tục bền vững như thế," Rudiger nói, cẩn thận nhìn tôi để chờ phản ứng của tôi. Anh ấy trông rất giống

Wilfried lúc tôi bảo huynh ấy kiểm tra Frenbeltag tại bữa tiệc trà, trước khi dạy cho họ các phương pháp của chúng tôi.
"Chúng ta là anh em họ và là những người hàng xóm; một tình bạn chỉ là điều đương nhiên thôi," tôi trả lời, khiến cả Rudiger và Wilfried đều thở hắt ra trong nhẹ nhõm.
Một khi cuộc chào hỏi đã kết thúc, bữa trưa bắt đầu. Món súp năm nay thực sự có vị rất ngon, có lẽ là do các đầu bếp đã áp dụng các công thức nấu ăn của chúng tôi, nhưng đồ ngọt thì... Chà, một lần nữa, chúng chẳng ngon hơn những cục đường là bao.

Phần Kết
Hildebrand đứng trước cánh cửa dịch chuyển. Hôm nay, cậu ấy sẽ đến Học viện Hoàng gia!
Cậu ấy ngước lên, run rẩy vì phấn khích, chỉ để Arthur, người hầu trưởng của cậu ấy, gạt sang một bên phần tóc mái rủ xuống trán vị vương tử trẻ tuổi.
"Hãy nhớ rằng ngài đang theo học Học viện với tư cách là hoàng tộc," Arthur nhấn mạnh.
"Ta biết. Đây là nghĩa vụ đầu tiên của ta với tư cách là vương tử, được Phụ thân ra lệnh," Hildebrand trả lời. Cậu ấy cố gắng tạo ra một biểu cảm nghiêm túc khi gật đầu hiểu chuyện, nhưng cậu ấy không thể kìm nén được sự tò mò đối với nơi mới mẻ, chưa biết mà cậu ấy đang đi tới này.
Chính xác thì điều gì đang chờ đợi cậu ấy phía sau cánh cửa đó?
"Bây giờ chúng ta có thể đi," Arthur nói.
Cánh cửa mở ra trước đôi mắt màu tím sáng của vị vương tử. Các tùy tùng khuyến khích cậu ấy bước tới, và khi cậu ấy thực hiện bước đi đầu tiên của mình, cậu ấy nhận ra bản thân đang bị bao trùm trong sự im lặng.
Một hành lang trải dài vào khoảng không phía xa, các bức tường của nó xếp thành những hàng cánh cửa cách đều nhau với các chữ cái và con số được viết phía trên. Nó hoàn toàn không giống bất cứ thứ gì cậu ấy từng thấy trong biệt thự nơi cậu ấy và mẹ mình đã ở trước khi rửa tội hay biệt thự mà cậu ấy đang sống bây giờ.
Nhưng đã có rất nhiều người khi ta đến cung điện hoàng gia lần đầu tiên...
Là một đứa con của người vợ thứ ba của nhà vua, Hildebrand đã lớn lên trong biệt thự của mẹ cậu ấy, và cậu ấy đã không mạo hiểm ra bên ngoài những bức tường của nó trước lễ rửa tội của mình. Thỉnh thoảng gia đình mẹ cậu ấy có đến thăm, nhưng cậu ấy đã quen với việc nhận được ít sự chú ý hơn thế. Do đó, cậu ấy có thể nhớ lại những đám đông ngập tràn mà cậu ấy đã nhìn thấy trong chuyến viếng thăm cung điện hoàng gia như thể chuyện đó chỉ mới xảy ra vào ngày hôm qua.

Hildebrand biết rằng Học viện Hoàng gia là nơi để con cái của hoàng tộc và các quý tộc học tập từ năm thứ mười cho đến khi trưởng thành, và cậu ấy đã mặc nhiên cho rằng mọi người sẽ chào đón mình một cách nhiệt tình. Một hành lang trống rỗng là điều hoàn toàn nằm ngoài dự đoán.
"Không có ai ở đây cả..." cậu ấy lẩm bẩm.
"Lễ thăng cấp đang được diễn ra, vì vậy các học sinh và giáo sư đều ở trong khán phòng," hiệp sĩ hộ vệ dẫn đầu trả lời, khiến vị vương tử nhận ra mình đã nói to. "Đây là một sự xả hơi đáng hoan nghênh đối với những hiệp sĩ hộ vệ chúng thần, vì có ít nguy hiểm đáng sợ hơn."
Có vẻ như mọi người đã tập trung ở một nơi khác.
Thật hợp lý khi Hildebrand không tham dự lễ thăng cấp, xét đến việc cậu ấy không phải là học sinh mới, nhưng giống như thể cậu ấy đang bị bỏ rơi vậy. Cảm thấy hơi thất vọng, Hildebrand đi dọc theo hành lang tối tăm với những cánh cửa cách đều nhau cho đến khi cậu ấy đến một hành lang khác, hành lang này có các cửa sổ.
Bên ngoài có rất nhiều tuyết, nhiều hơn so với những gì cậu ấy vẫn thường thấy bên ngoài biệt thự của chính mình. Cậu ấy mím môi lại với nhau; lớp tuyết chất đống gần giống như một phép ẩn dụ, biểu thị rằng cậu ấy sẽ có nhiều nhiệm vụ hơn ở đây tại Học viện Hoàng gia.
"Ngài có lo lắng không?" Arthur hỏi, có vẻ lo lắng cho cậu ấy. "Ngài tỏ ra khá cứng nhắc đấy."
"Ta chỉ đơn giản cảm thấy sức nặng từ những trách nhiệm của mình thôi," Hildebrand trả lời với một cái gật đầu. "Ta ở đây với tư cách là hoàng tộc mặc dù ta chỉ mới được rửa tội gần đây."
Cậu ấy nghĩ lại lúc nhà vua—phụ thân của cậu ấy—đã hướng dẫn cậu ấy theo học tại Học viện Hoàng gia. Đó là vào khoảng giữa mùa thu.
"Sẽ là một gánh nặng to lớn, nhưng ta yêu cầu con giám sát Học viện Hoàng gia với tư cách là hoàng tộc."
""",

# Chunk 6: Lines 148-150
"""
Hildebrand đã nhận được yêu cầu này từ cha mẹ mình, những người đang đến thăm biệt thự mà họ đã ban cho cậu ấy.
Cậu ấy không biết phải trả lời như thế nào, vì vậy Arthur, người hầu trưởng của cậu ấy, đã lên tiếng thay cho cậu ấy, mặc dù với một giọng điệu đầy rắc rối.
"Vương tử Hildebrand chỉ vừa mới được rửa tội. Ngài ấy thậm chí còn chưa có buổi ra mắt của mình."
Sau khi một đứa trẻ được rửa tội trong cung điện hoàng gia, quy trình chuẩn mực là chúng sẽ được ra mắt với tư cách là một hoàng tộc mới trong Hội nghị Lãnh chúa tiếp theo. Chưa từng có tiền lệ về việc một hoàng tộc thực hiện các nghĩa vụ công khai trước buổi ra mắt của họ.
"Sự thật thì... Ta đã dành nhiều thời gian để tranh luận xem nên gửi con hay Anastasius," nhà vua nói với con trai mình. "Tuy nhiên, Anastasius có công việc quan trọng hơn nhiều phải làm thay vì đứng vào vị trí tại Học viện Hoàng gia. Ta muốn con làm công việc này cho ta, Hildebrand."
Nếu đây là kết luận mà nhà vua đã đưa ra sau một cuộc tranh luận nội bộ kéo dài, không có cách nào để những người tùy tùng đơn thuần có thể phản đối. Họ chỉ có thể im lặng chấp nhận mệnh lệnh và hỗ trợ người mà họ phụ trách một cách tốt nhất có thể.
Mặc dù vậy, cuối cùng thì, mình cũng sẽ chủ yếu bị hạn chế trong biệt thự của mình thôi.
Hildebrand được bảo phải tránh tiếp xúc với các học sinh càng nhiều càng tốt; cậu ấy còn quá trẻ để tự mình xác định tốt hay xấu, vì vậy có khả năng các học sinh sẽ cố gắng lợi dụng cậu ấy cho mục đích này hay mục đích khác. Hoàng tộc chỉ đơn giản là có ngần ấy quyền uy đối với tên của họ—chứ không phải là Hildebrand hoàn toàn hiểu được điều này. Cậu ấy đã dành trọn cuộc đời mình trong biệt thự của mẹ và hiếm khi tương tác với thế giới bên ngoài, vì vậy cậu ấy không hoàn toàn nắm bắt được thứ quyền lực mà cậu ấy đang nắm giữ.
Có vẻ như với mình thì Mẫu thân và các tùy tùng của mình có nhiều quyền lực hơn mình rất nhiều, nhưng họ nói ngược lại, vì vậy...
"""
]

# Read original
lines = codecs.open('d:/novel/p4vol5/translated_251_300.txt', 'r', 'utf-8-sig').read().split('\n')
# We know the valid lines were up to line 106.
base_text = '\n'.join(lines[:106])

# Join the recovered chunks
recovered_text = '\n\n'.join([c.strip() for c in translations])

# Final file
final_text = base_text + '\n\n' + recovered_text

codecs.open('d:/novel/p4vol5/translated_251_300.txt', 'w', 'utf-8-sig').write(final_text)

print("Done completely recovering the file without duplicates.")
