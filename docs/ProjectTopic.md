N4.2 – Xây dựng hệ thống thu thập và phân tích cảnh báo từ router, switch và firewall
N4 – Mạng, IoT và hạ tầng số
Định hướng phù hợp: Quản trị sự kiện mạng và chuẩn hóa cảnh báo; tạo lab quan sát tập trung trước khi tích hợp hệ thống thật.
Bài toán thực tiễn: Cảnh báo từ thiết bị mạng có định dạng và mức độ khác nhau. Đề tài xây dựng bộ thu thập, chuẩn hóa, tìm kiếm và thống kê cảnh báo từ các nguồn giả lập hoặc lab, giúp người vận hành nhìn được xu hướng và ưu tiên xử lý.
Mục tiêu cụ thể
Tiếp nhận cảnh báo qua syslog/file/API giả lập.
Chuẩn hóa trường thiết bị, thời gian, mức độ và nội dung.
Tạo luật tương quan cơ bản, bộ lọc và thống kê theo thiết bị/loại cảnh báo.
Phạm vi thực hiện trong 18 tuần
Sinh dữ liệu syslog mẫu hoặc dùng thiết bị lab được cấp phép; không quét hay thay đổi thiết bị sản xuất.
Xây dựng parser và mapping mức độ cảnh báo.
Tìm kiếm theo thời gian, thiết bị, severity; gom nhóm cảnh báo lặp.
Dashboard tổng quan, quy tắc ngưỡng và xuất báo cáo.
Công nghệ gợi ý: Syslog-ng/rsyslog hoặc Fluent Bit; Python; OpenSearch/ELK hoặc Loki/Grafana; Docker.
Dữ liệu/môi trường thử nghiệm: Log/cảnh báo được tạo trong lab, dữ liệu đã khử nhạy cảm hoặc kịch bản giả lập theo loại thiết bị.
Sản phẩm bàn giao
Sơ đồ kiến trúc thu thập cảnh báo.
Parser/chuẩn hóa và bộ dữ liệu test.
Dashboard, bộ lọc và luật gom nhóm.
Hướng dẫn triển khai lab và báo cáo kiểm thử tải cơ bản.
Tiêu chí nghiệm thu đề xuất
Có thể nhận dữ liệu từ ít nhất hai nguồn/định dạng mẫu hoặc hai loại thiết bị giả lập.
Cảnh báo được lưu, tìm kiếm, lọc và thống kê đúng theo bộ test.
Không chứa thông tin xác thực; không thực hiện thay đổi cấu hình thiết bị.
Rủi ro và cách giới hạn phạm vi: Tách biệt lab và mạng sản xuất; thông tin IP, hostname, cấu hình và credential phải được giả lập hoặc xử lý theo quy định.
Nguồn dữ liệu public đề xuất
Loghub — Log hệ thống dùng để xây dựng parser và kịch bản cảnh báo. https://github.com/logpai/loghub
NIST RAN Anomalous State Detection — Dữ liệu RAN để bổ trợ metric bất thường. https://catalog.data.gov/dataset/radio-access-network-anomalous-state-detection-dataset
Syslog giả lập — Sinh cảnh báo router/switch/firewall giả lập bằng mẫu syslog, severity và loại sự kiện. Tự tạo trong lab
Dữ liệu VNPT nếu được cung cấp
Nếu được phê duyệt: mẫu syslog/alert đã làm sạch từ thiết bị lab hoặc môi trường staging; ẩn IP quản trị, hostname, community string, credential, topology và thông tin khách hàng. Không cấp quyền đăng nhập thiết bị mạng thật.
Tài nguyên và môi trường triển khai
Docker/Linux VM; syslog-ng/rsyslog hoặc file ingestion; Python; Grafana/Loki hoặc OpenSearch; 8–16 GB RAM. Thiết bị thật là tùy chọn, không phải điều kiện bắt buộc.
Kết quả dự kiến khi nghiệm thu
Một prototype/PoC chạy được trong môi trường thử nghiệm; bộ dữ liệu hoặc pipeline có hướng dẫn tái lập; báo cáo đánh giá theo KPI phù hợp với đề tài; mã nguồn và hướng dẫn cài đặt; slide/demo; danh mục hạn chế và đề xuất bước tiếp theo. Chỉ tiêu định lượng cụ thể cần được UTH và mentor VNPT thống nhất sau khi chốt dữ liệu, không đặt ngưỡng tùy ý trước khi đo baseline.