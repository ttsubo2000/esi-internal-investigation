# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Gw Interface" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "resource_id": "257d0a9f-d5ae-4a93-9af4-81ad611e1b0d",
    "field_name": "logical_port",
    "type": "snmp_ports",
    "properties": {
        "community_name": "***",
        "device_ip": "10.161.0.34",
        "if_name": "xe-0/0/4.1025"
    },
    "resource_type": "ese_logical_ports",
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes",
                "tags": [
                    {
                        "direction": "in",
                        "port_id": "53eeb091-3297-4b9b-a200-b6568567e387",
                        "resource_id": "257d0a9f-d5ae-4a93-9af4-81ad611e1b0d"
                    }
                ]
            },
            "traffic.out": {
                "metric": "traffic.bytes",
                "tags": [
                    {
                        "direction": "out",
                        "port_id": "53eeb091-3297-4b9b-a200-b6568567e387",
                        "resource_id": "257d0a9f-d5ae-4a93-9af4-81ad611e1b0d"
                    }
                ]
            }
        },
        "etcd": {
            "status": {
                "key": "logical_port"
            }
        }
    }
}
```

- Response

```
{
    "id": "5e4c28ad-c5f2-43fc-97e8-1b5e99642b87",
    "created_at": "2018-04-16T00:12:56Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/5e4c28ad-c5f2-43fc-97e8-1b5e99642b87",
    "type": "snmp_ports",
    "resource_id": "257d0a9f-d5ae-4a93-9af4-81ad611e1b0d",
    "resource_type": "ese_logical_ports",
    "field_name": "logical_port",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "community_name": "***",
        "device_ip": "10.161.0.34",
        "if_name": "xe-0/0/4.1025"
    },
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "logical_port"
            }
        },
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes",
                "tags": [
                    {
                        "direction": "in",
                        "port_id": "53eeb091-3297-4b9b-a200-b6568567e387",
                        "resource_id": "257d0a9f-d5ae-4a93-9af4-81ad611e1b0d"
                    }
                ]
            },
            "traffic.out": {
                "metric": "traffic.bytes",
                "tags": [
                    {
                        "direction": "out",
                        "port_id": "53eeb091-3297-4b9b-a200-b6568567e387",
                        "resource_id": "257d0a9f-d5ae-4a93-9af4-81ad611e1b0d"
                    }
                ]
            }
        }
    }
}
```

### This is JSON data for checking "Gw Interface" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/5e4c28ad-c5f2-43fc-97e8-1b5e99642b87
```

- Response

```
{
    "id": "5e4c28ad-c5f2-43fc-97e8-1b5e99642b87",
    "created_at": "2018-04-16T00:12:56Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/5e4c28ad-c5f2-43fc-97e8-1b5e99642b87",
    "type": "snmp_ports",
    "resource_id": "257d0a9f-d5ae-4a93-9af4-81ad611e1b0d",
    "resource_type": "ese_logical_ports",
    "field_name": "logical_port",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "community_name": "***",
        "device_ip": "10.161.0.34",
        "if_name": "xe-0/0/4.1025"
    },
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "logical_port"
            }
        },
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes",
                "tags": [
                    {
                        "direction": "in",
                        "port_id": "53eeb091-3297-4b9b-a200-b6568567e387",
                        "resource_id": "257d0a9f-d5ae-4a93-9af4-81ad611e1b0d"
                    }
                ]
            },
            "traffic.out": {
                "metric": "traffic.bytes",
                "tags": [
                    {
                        "direction": "out",
                        "port_id": "53eeb091-3297-4b9b-a200-b6568567e387",
                        "resource_id": "257d0a9f-d5ae-4a93-9af4-81ad611e1b0d"
                    }
                ]
            }
        }
    },
    "values": []
}
```
and then ...
```
{
    "id": "5e4c28ad-c5f2-43fc-97e8-1b5e99642b87",
    "created_at": "2018-04-16T00:12:56Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/5e4c28ad-c5f2-43fc-97e8-1b5e99642b87",
    "type": "snmp_ports",
    "resource_id": "257d0a9f-d5ae-4a93-9af4-81ad611e1b0d",
    "resource_type": "ese_logical_ports",
    "field_name": "logical_port",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "community_name": "***",
        "device_ip": "10.161.0.34",
        "if_name": "xe-0/0/4.1025"
    },
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "logical_port"
            }
        },
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes",
                "tags": [
                    {
                        "direction": "in",
                        "port_id": "53eeb091-3297-4b9b-a200-b6568567e387",
                        "resource_id": "257d0a9f-d5ae-4a93-9af4-81ad611e1b0d"
                    }
                ]
            },
            "traffic.out": {
                "metric": "traffic.bytes",
                "tags": [
                    {
                        "direction": "out",
                        "port_id": "53eeb091-3297-4b9b-a200-b6568567e387",
                        "resource_id": "257d0a9f-d5ae-4a93-9af4-81ad611e1b0d"
                    }
                ]
            }
        }
    },
    "values": [
        {
            "reporter": "SNMPPortPool",
            "key": "traffic.in",
            "value": 1523837636,
            "last_reported": "2018-04-16T00:13:56Z",
            "last_changed": "2018-04-16T00:13:56Z",
            "fail_counter": 0
        },
        {
            "reporter": "SNMPPortPool",
            "key": "traffic.out",
            "value": 1523837636,
            "last_reported": "2018-04-16T00:13:56Z",
            "last_changed": "2018-04-16T00:13:56Z",
            "fail_counter": 0
        },
        {
            "reporter": "SNMPPortPool",
            "key": "status",
            "value": "UP",
            "last_reported": "2018-04-16T00:13:56Z",
            "last_changed": "2018-04-16T00:13:56Z",
            "fail_counter": 0
        }
    ]
}
```
