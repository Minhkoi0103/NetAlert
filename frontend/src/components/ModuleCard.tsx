interface ModuleCardProps {
  title: string
  description: string
}

export default function ModuleCard({ title, description }: ModuleCardProps) {
  return (
    <section>
      <h2>{title}</h2>
      <p>{description}</p>
    </section>
  )
}
