# NetAlert — N4.2

Hệ thống thu thập và phân tích cảnh báo từ router, switch và firewall giả lập. Môi trường phát triển chạy trên máy cá nhân bằng Docker Compose; backend dùng Python/FastAPI và PostgreSQL, giao diện dùng React/TypeScript.

Đây là **bộ khung dự án**, chưa phải hệ thống thu thập cảnh báo hoàn chỉnh. API hiện chỉ có endpoint `/api/v1/health`; giao diện là trang giữ chỗ. Các hàm collector, parser, rules, storage và simulator được khai báo để phân công triển khai nhưng chưa có logic nghiệp vụ.

## Cấu trúc dự án

```text
NetAlert/
├── backend/
│   ├── app/
│   │   ├── api/             # HTTP API; router tách theo ingest/events/alerts/stats
│   │   ├── collector/       # Hợp đồng nhận syslog, file hoặc JSON API
│   │   ├── normalization/   # Hợp đồng parser và mapping
│   │   ├── rules/           # Hợp đồng gom nhóm và ngưỡng
│   │   └── storage/         # Interface PostgreSQL, chỗ đặt migration
│   └── tests/               # Kiểm thử backend và pipeline
├── frontend/
│   └── src/
│       ├── api/             # Gọi FastAPI
│       ├── components/      # Thành phần giao diện dùng lại
│       └── pages/           # Dashboard, danh sách, chi tiết cảnh báo
├── simulator/
│   ├── devices/             # Khung giả lập router, switch, firewall
│   ├── scenarios/           # Kịch bản sự kiện giả lập
│   └── samples/             # Bản tin mẫu đã khử thông tin nhạy cảm
├── docs/                    # Kiến trúc, kế hoạch, nghiệm thu, triển khai
├── compose.yaml             # PostgreSQL, API và giao diện phát triển
└── .env.example             # Cấu hình mẫu cho lab cục bộ
```

`backend/app` là một codebase Python. Compose hiện chỉ khởi chạy PostgreSQL, API và giao diện; collector và simulator sẽ được thêm thành service sau khi có logic nhận/gửi log. `docs/` chứa tài liệu dự án, còn mã nguồn và cấu hình chạy đặt ở các thư mục tương ứng.

Đầu vào, đầu ra và hợp đồng dữ liệu của từng module: [docs/ModuleInterfaces.md](docs/ModuleInterfaces.md).

## Chạy bộ khung

Trên máy có Docker Compose:

```bash
docker compose up --build
```

- Giao diện: `http://localhost:5173`
- API health: `http://localhost:8000/api/v1/health`
- Tài liệu API: `http://localhost:8000/docs`

`POSTGRES_DB`, `POSTGRES_USER` và `POSTGRES_PASSWORD` có thể đặt trong file `.env` theo `.env.example`. Mật khẩu mẫu chỉ dùng cho máy cá nhân. Chưa có migration, bảng dữ liệu, endpoint cảnh báo, listener syslog hoặc bộ phát log chạy trong Compose.

## Quy ước làm việc

- Mỗi thay đổi gắn với một Jira task và có người chịu trách nhiệm chính.
- Mã nguồn, tài liệu và dữ liệu mẫu được commit; khóa, mật khẩu, `.env` thật và log chạy cục bộ không được commit.
- Chỉ thêm endpoint hoặc service vào luồng chạy khi phần triển khai tương ứng đã sẵn sàng; không xem các hàm `NotImplementedError` là tính năng hoàn thành.
