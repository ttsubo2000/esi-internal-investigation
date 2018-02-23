# HTTP Methods for creating heat-stack: Load Balancer Configuration

Checking heat-stack of "load_balancer" via heatclient.
```
... (snip)
```
Checking heat-template of "load_balancer" via heatclient.
```
$ heat template-show load_balancer_b311c470-d878-4fea-8466-a4393938f2d4
description: Load Balancer
heat_template_version: '2013-05-23'
outputs:
  monitoring_link:
    description: Monitoring Process Link
    value:
      get_attr: [lb_device_monitor, link]
  monitoring_target_id:
    description: Monitoring Target ID
    value: {get_resource: lb_device_monitor}
parameters:
  gohan_id: {description: UUID of the VNF Instance, label: Gohan resource ID, type: string}
  management_ip: {type: string}
  tenant_id: {label: Tenant ID, type: string}
  version: {label: Config version, type: number}
resources:
  lb_device_monitor:
    properties:
      field_name: load_balancer
      properties:
        community_name: LOAD_BALANCER_COMMUNITY
        device_ip: {get_param: management_ip}
      resource_id: {get_param: gohan_id}
      resource_type: load_balancers
      syncer_properties:
        etcd:
          status: {key: load_balancer}
        tsdb:
          cpu.usage:
            metric: cpu.percents
            tags:
              resource_id: {get_param: gohan_id}
              type: usage
          http.request:
            metric: http.request.connections
            tags:
              resource_id: {get_param: gohan_id}
          memory.usage:
            metric: memory.percents
            tags:
              resource_id: {get_param: gohan_id}
              type: usage
          tcp.client:
            metric: tcp.connections
            tags:
              owner: client
              resource_id: {get_param: gohan_id}
          tcp.server:
            metric: tcp.connections
            tags:
              owner: server
              resource_id: {get_param: gohan_id}
      tenant_id: {get_param: tenant_id}
      type: snmp_device_lb
      version: {get_param: version}
    type: ESI::Monitoring::MonitoringTarget
```
