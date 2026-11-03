# Đầu vào và đầu ra của các module NetAlert

Tài liệu này là hợp đồng dữ liệu đề xuất cho bản lab. Các tên trường có thể được điều chỉnh ở tuần thiết kế, nhưng mọi thay đổi phải được cập nhật đồng thời ở backend, API, frontend và bộ dữ liệu mẫu.

## Luồng chính

```text
simulator → collector → normalization → storage → API → frontend
                                ↘ rules ↗
```

`rules` nhận sự kiện đã chuẩn hóa và đọc lịch sử từ `storage` để gom cảnh báo hoặc đánh giá ngưỡng; kết quả của nó được ghi lại vào `storage`. Trong backend, collector, normalization và rules gọi nhau qua hàm Python. API HTTP dành cho nguồn gửi JSON và giao diện truy vấn dữ liệu.

| Module/thư mục | Đầu vào | Đầu ra | Ranh giới trách nhiệm |
|---|---|---|---|
| `simulator/devices` | Kịch bản trong `simulator/scenarios`, cấu hình loại thiết bị, tốc độ và thời điểm phát | Bản tin syslog qua UDP đến collector; dữ liệu mẫu lưu trong `simulator/samples` | Chỉ mô phỏng log router, switch, firewall; không thực hiện chức năng mạng của thiết bị thật. |
| `backend/app/collector` | Syslog UDP; bản ghi file; JSON từ endpoint nhận dữ liệu của API | `RawEvent` gồm bản tin gốc, nguồn, thời điểm nhận, định danh thiết bị nếu có; hoặc lỗi tiếp nhận có lý do | Nhận và kiểm tra kích thước/định dạng cơ bản, không tự suy luận severity. |
| `backend/app/normalization` | `RawEvent` và quy tắc parser/mapping tương ứng nguồn | `NormalizedEvent` có thiết bị, thời gian sự kiện, severity chuẩn, loại sự kiện, nội dung và tham chiếu bản gốc; hoặc lỗi parse có lý do | Xử lý khác biệt định dạng và thời gian; giữ bản gốc để đối chiếu. |
| `backend/app/rules` | `NormalizedEvent`, cấu hình luật, các sự kiện/nhóm gần đây đọc từ storage | `AlertGroup` mới hoặc được cập nhật; kết quả vượt ngưỡng nếu có | Gom sự kiện lặp theo khóa và cửa sổ thời gian đã chốt; không xóa sự kiện gốc. |
| `backend/app/storage` | `RawEvent`, `NormalizedEvent`, `AlertGroup`; yêu cầu truy vấn từ API/rules | Bản ghi PostgreSQL, ID, kết quả truy vấn/phân trang/thống kê | Là lớp truy cập dữ liệu; quản lý schema và migration. |
| `backend/app/api` | HTTP request từ frontend; JSON đầu vào giả lập nếu bật endpoint ingest | JSON danh sách/chi tiết cảnh báo, thống kê, kết quả nhập dữ liệu và mã lỗi HTTP | Xác thực tham số, phân trang, gọi collector hoặc storage/rules; không chứa logic parse riêng. |
| `frontend/src/api` | Thao tác người dùng và tham số lọc | HTTP request đến FastAPI; dữ liệu/ lỗi đã chuyển thành kiểu TypeScript | Là nơi tập trung lời gọi API. |
| `frontend/src/pages`, `components` | Dữ liệu từ `frontend/src/api` | Dashboard, danh sách, chi tiết cảnh báo, bộ lọc và trạng thái lỗi/rỗng/đang tải | Hiển thị dữ liệu; không tự tính lại severity hay luật gom nhóm. |
| `backend/tests` | Bộ log mẫu, dữ liệu kỳ vọng, cấu hình kiểm thử | Kết quả kiểm tra parser, rules, API và luồng tích hợp | Đây là module kiểm chứng, không tham gia luồng chạy thực tế. |
| `docs` | Quyết định thiết kế, kết quả triển khai và kiểm thử | Tài liệu kiến trúc, triển khai, nghiệm thu, báo cáo | Tài liệu theo sát hành vi thực tế của hệ thống. |

## Hợp đồng dữ liệu tối thiểu

### RawEvent

| Trường | Ý nghĩa |
|---|---|
| `source_type` | `syslog_udp`, `file` hoặc `api` |
| `received_at` | Thời điểm collector nhận dữ liệu, lưu theo UTC |
| `raw_message` | Nội dung gốc, có giới hạn kích thước |
| `sender` | Địa chỉ nguồn hoặc tên nguồn file/API; không dùng một mình để xác định thiết bị |
| `device_hint` | Định danh thiết bị nếu nguồn cung cấp |

### NormalizedEvent

| Trường | Ý nghĩa |
|---|---|
| `raw_event_id` | Tham chiếu bản ghi gốc |
| `device_id`, `device_type` | Thiết bị và loại `router`, `switch`, `firewall` |
| `event_time` | Thời gian xảy ra sự kiện; phân biệt với `received_at` |
| `severity` | Mức độ sau mapping chung; tập giá trị sẽ chốt ở thiết kế |
| `event_type` | Loại như `interface_down`, `auth_failed`, `traffic_blocked` |
| `message` | Nội dung đã chuẩn hóa để hiển thị |

### AlertGroup

| Trường | Ý nghĩa |
|---|---|
| `group_key` | Khóa gom nhóm từ thiết bị, loại sự kiện và thuộc tính liên quan |
| `first_seen`, `last_seen` | Thời gian đầu/cuối của nhóm |
| `count` | Số sự kiện thuộc nhóm |
| `severity`, `rule_id` | Mức độ và luật tạo/cập nhật nhóm |

Các bảng và tên trường thực tế do nhóm backend thống nhất. Khi parser gặp bản tin không hợp lệ, hệ thống cần giữ thông tin lỗi có giới hạn để kiểm tra, thay vì biến nó thành `NormalizedEvent`.

## Ví dụ một sự kiện

1. Simulator switch gửi syslog về collector: `SW-01 port Gi0/1 down`.
2. Collector tạo `RawEvent` với `source_type=syslog_udp`, `received_at` và `raw_message`.
3. Normalization tạo `NormalizedEvent` với `device_id=SW-01`, `device_type=switch`, `event_type=interface_down` và severity theo bảng mapping đã chốt.
4. Storage lưu sự kiện gốc và chuẩn hóa. Rules tìm nhóm tương ứng trong cửa sổ thời gian; nếu có, tăng `count`, nếu chưa thì tạo nhóm.
5. API trả danh sách sự kiện/nhóm và thống kê; frontend hiển thị ở dashboard.

## Quyết định cần chốt trước khi lập trình song song

- Tập giá trị `severity` chung và mapping từ từng nguồn.
- Mẫu syslog được hỗ trợ, cấu trúc JSON cho endpoint ingest và quy tắc xử lý dòng file lỗi.
- Khóa/cửa sổ gom nhóm và cách tính ngưỡng.
- Tên trường, kiểu dữ liệu, múi giờ, phân trang và mã lỗi của API.
