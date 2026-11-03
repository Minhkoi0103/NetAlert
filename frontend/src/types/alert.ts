export type DeviceType = 'router' | 'switch' | 'firewall'

export interface NormalizedEvent {
  raw_event_id: number | null
  device_id: string
  device_type: DeviceType
  event_time: string
  severity: string
  event_type: string
  message: string
}

export interface AlertGroup {
  group_key: string
  first_seen: string
  last_seen: string
  count: number
  severity: string
  rule_id: string
}
