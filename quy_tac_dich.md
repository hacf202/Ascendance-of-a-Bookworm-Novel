# Quy Tắc Dịch Thuật Novel (Ascendance of a Bookworm)

Tài liệu này chứa các quy tắc dịch thuật, từ vựng và quy trình thực hiện để các phiên làm việc (agents) luôn tạo ra kết quả đồng nhất và chất lượng cao. Đảm bảo tuân thủ mọi nguyên tắc dưới đây.

## 1. Đồng Nhất Giọng Văn & Xưng Hô

- **Bối cảnh:** Giữ vững văn phong và từ vựng phù hợp với bối cảnh quý tộc, cung đình phong kiến phương Tây. Lời thoại cần phản ánh đúng địa vị, giai cấp và thái độ của nhân vật.
- **Xưng hô cơ bản:**
  - Rozemyne xưng "tôi", gọi các nhân vật bề trên là "ngài", "phu nhân", "tiểu thư", "lãnh chúa",...
  - Với Wilfried/Cornelius anh trai của rozemyne.
  - Với retainers (hầu cận): xưng "ta - ngươi" hoặc "tôi - cậu/bạn/anh/chị" tùy vào thái độ của Rozemyne với từng người, nhưng thường Rozemyne khá lịch sự với hầu cận của mình (ví dụ: dùng "tôi", gọi tên). Hầu cận xưng "thần - người/tiểu thư".
  - Quý tộc nói chuyện với nhau: dùng các từ ngữ trang trọng, lịch sự, có phần vòng vo đặc trưng của quý tộc.
- **Mạch truyện:** Đảm bảo câu cú mượt mà, giữ nguyên cảm xúc và những đoạn độc thoại nội tâm đặc trưng của nhân vật chính mà không làm đứt đoạn cảm xúc của người đọc.
- **Cách xưng hô tham khảo:**
  - Lord: Lãnh chúa (hoặc Ngài tuỳ ngữ cảnh).
  - Lady: Phu nhân / Tiểu thư (tuỳ độ tuổi và tình trạng hôn nhân).
  - **Ferdinand:** Khi Rozemyne xưng hô hoặc nhắc đến Ferdinand (kể cả trong suy nghĩ nội tâm), luôn sử dụng "Ngài Ferdinand" để thể hiện đúng vai vế và sự tôn trọng.

## 2. Phiên Âm Tên Nhân Vật (Hỗ Trợ Text-to-Speech)

Để các công cụ đọc màn hình (như Google Dịch / Trợ lý ảo) có thể đọc tên nhân vật một cách trôi chảy và dễ nghe, tên của nhân vật chính được phiên âm sang cách đọc tiếng Việt trong văn bản dịch:

- **Rozemyne** -> Ro se mai

Các tên riêng khác **giữ nguyên gốc**, không dịch hay phiên âm trừ khi có yêu cầu đặc biệt:

- Ferdinand, Wilfried, Hannelore, Lieseleta, Philine, Hartmut, Eglantine, Lestilaut, Ortwin, Detlinde, Rudiger, Adolphine, Justus, Brunhilde, Gudrun, Rihyarda, Eckhart, Angelica, Sylvester, Cornelius, Hirschur, Bonifatius, Roderick, Leonore, Judithe, Traugott, Matthias,...

## 3. Thuật Ngữ Đặc Thù (Glossary)

Giữ nguyên gốc hoặc dịch theo quy ước sau để đảm bảo tính nhất quán của hệ thống phép thuật trong tác phẩm:

- **Mana:** ma lực
- **Feybeast:** feybeast / quái thú / dã thú (tuỳ ngữ cảnh)
- **Highbeast:** highbeast
- **Schtappe:** schtappe
- **Trombe:** trombe / cây trombe
- **Ternisbefallen:** ternisbefallen / con ternisbefallen
- **Ordonnanz:** ordonnanz / con ordonnanz
- **Feystone:** feystone / viên feystone
- **Blessing:** lời ban phước
- **Apprentice knight:** học sinh hiệp sĩ tập sự / hiệp sĩ tập sự
- **Guard knight:** hiệp sĩ bảo vệ
- **Retainer:** hầu cận
- **Gathering spot:** địa điểm thu thập / khu vực thu thập
- **Archduke Conference:** Hội nghị Lãnh chúa
- **Dedication Ritual:** Lễ dâng hiến

## 4. Xử Lý Format, Đánh Dấu Số Trang & Chuyển Phần

- **Loại bỏ số trang:** Loại bỏ hoàn toàn các cụm từ đánh dấu số trang (như "Page | 179", "231 | P a g e", "Trang | 180"...) có trong bản gốc. Không giữ lại các khoảng trắng thừa, các dòng trống dư thừa sinh ra từ việc xóa số trang.
- **Mạch truyện liền mạch:** Việc này giúp văn bản dịch trở thành một câu chuyện liền mạch hoàn toàn, không bị ngắt quãng gây khó chịu khi sử dụng công cụ đọc văn bản (TTS).
- **Đánh dấu chuyển phần/góc nhìn:** Khi kết thúc một phần (hoặc góc nhìn POV) và bắt đầu một tựa đề phần mới, bắt buộc phải thêm một câu thông báo để công cụ đọc văn bản có thể đọc tựa đề mạch lạc. Cú pháp bắt buộc là: `[Thông báo: Hết phần. Tiếp theo là phần: <Tên Tựa Đề>]`.

## 5. Quy Trình Dịch Thuật Bằng Python Scripts (Chống Token Limit)

Khi xử lý các tệp văn bản lớn (như rawtext dài hàng trăm dòng), việc in trực tiếp ra console hoặc dùng tool thay thế toàn bộ văn bản rất dễ gặp lỗi vượt giới hạn token (token limit) hoặc thao tác chậm chạp. Quy trình tiêu chuẩn là:

1. **Chia nhỏ (Chunking):** Xem tệp nguồn (`rawtext...txt`) và dịch theo từng đoạn nhỏ (khoảng 30-40 dòng).
2. **Sử dụng Script Python (`append_chunk.py`):** Dùng Python để mở tệp đích ở chế độ nối đuôi (`'a'` - append) và ghi bản dịch vào.
   - Mã hóa (encoding) phải luôn luôn là `utf-8`.
   - Ví dụ:
     ```python
     with open('translated_XXX.txt', 'a', encoding='utf-8') as f:
         f.write('Văn bản dịch đoạn 1...\n')
     ```
3. **Thực thi bằng `run_command`:** Chạy script Python để nối nội dung vào tệp đích. Nếu script dài hoặc thao tác nhiều, đảm bảo xử lý lỗi và chạy từng script một nếu cần thiết.
4. **Lặp lại:** Lặp lại các bước trên cho đến khi toàn bộ tệp nguồn được dịch xong.
