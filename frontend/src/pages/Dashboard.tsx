import ModuleCard from '../components/ModuleCard'

export default function Dashboard() {
  return (
    <main>
      <h1>NetAlert</h1>
      <p>Khung giao diện dự án N4.2. Dữ liệu cảnh báo sẽ được kết nối sau.</p>
      <ModuleCard title="Dashboard" description="Thống kê và biểu đồ sẽ hiển thị tại đây." />
      <ModuleCard title="Cảnh báo" description="Danh sách và bộ lọc cảnh báo sẽ hiển thị tại đây." />
    </main>
  )
}
