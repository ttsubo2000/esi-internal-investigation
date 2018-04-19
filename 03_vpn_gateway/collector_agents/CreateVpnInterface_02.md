# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Vpn Interface" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "resource_id": "07d4f1fc-5142-4fae-b115-627fc009e222",
    "field_name": "primary_router",
    "type": "snmp_ports_metric",
    "properties": {
        "community_name": "***",
        "device_ip": "10.79.5.185",
        "if_name": "ge-0/0/1.122"
    },
    "resource_type": "vpn_interfaces",
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes",
                "tags": {
                    "direction": "in",
                    "device_index": "primary",
                    "resource_id": "07d4f1fc-5142-4fae-b115-627fc009e222"
                }
            },
            "traffic.out": {
                "metric": "traffic.bytes",
                "tags": {
                    "direction": "out",
                    "device_index": "primary",
                    "resource_id": "07d4f1fc-5142-4fae-b115-627fc009e222"
                }
            }
        }
    }
}
```

- Response

```
{
    "id": "d7885526-613f-4565-a3df-de89ed911e3b",
    "created_at": "2018-04-16T00:10:08Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/d7885526-613f-4565-a3df-de89ed911e3b",
    "type": "snmp_ports_metric",
    "resource_id": "07d4f1fc-5142-4fae-b115-627fc009e222",
    "resource_type": "vpn_interfaces",
    "field_name": "primary_router",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "community_name": "***",
        "device_ip": "10.79.5.185",
        "if_name": "ge-0/0/1.122"
    },
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes",
                "tags": {
                    "device_index": "primary",
                    "direction": "in",
                    "resource_id": "07d4f1fc-5142-4fae-b115-627fc009e222"
                }
            },
            "traffic.out": {
                "metric": "traffic.bytes",
                "tags": {
                    "device_index": "primary",
                    "direction": "out",
                    "resource_id": "07d4f1fc-5142-4fae-b115-627fc009e222"
                }
            }
        }
    }
}
```

### This is JSON data for checking "Vpn Interface" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/d7885526-613f-4565-a3df-de89ed911e3b
```

- Response

```
{
    "id": "d7885526-613f-4565-a3df-de89ed911e3b",
    "created_at": "2018-04-16T00:10:08Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/d7885526-613f-4565-a3df-de89ed911e3b",
    "type": "snmp_ports_metric",
    "resource_id": "07d4f1fc-5142-4fae-b115-627fc009e222",
    "resource_type": "vpn_interfaces",
    "field_name": "primary_router",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "community_name": "***",
        "device_ip": "10.79.5.185",
        "if_name": "ge-0/0/1.122"
    },
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes",
                "tags": {
                    "device_index": "primary",
                    "direction": "in",
                    "resource_id": "07d4f1fc-5142-4fae-b115-627fc009e222"
                }
            },
            "traffic.out": {
                "metric": "traffic.bytes",
                "tags": {
                    "device_index": "primary",
                    "direction": "out",
                    "resource_id": "07d4f1fc-5142-4fae-b115-627fc009e222"
                }
            }
        }
    },
    "values": []
}
```
and then ...
```
{
    "id": "d7885526-613f-4565-a3df-de89ed911e3b",
    "created_at": "2018-04-16T00:10:08Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/d7885526-613f-4565-a3df-de89ed911e3b",
    "type": "snmp_ports_metric",
    "resource_id": "07d4f1fc-5142-4fae-b115-627fc009e222",
    "resource_type": "vpn_interfaces",
    "field_name": "primary_router",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "community_name": "***",
        "device_ip": "10.79.5.185",
        "if_name": "ge-0/0/1.122"
    },
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes",
                "tags": {
                    "device_index": "primary",
                    "direction": "in",
                    "resource_id": "07d4f1fc-5142-4fae-b115-627fc009e222"
                }
            },
            "traffic.out": {
                "metric": "traffic.bytes",
                "tags": {
                    "device_index": "primary",
                    "direction": "out",
                    "resource_id": "07d4f1fc-5142-4fae-b115-627fc009e222"
                }
            }
        }
    },
    "values": [
        {
            "reporter": "SNMPPortPool",
            "key": "traffic.out",
            "value": 1523837468,
            "last_reported": "2018-04-16T00:11:09Z",
            "last_changed": "2018-04-16T00:11:09Z",
            "fail_counter": 0
        },
        {
            "reporter": "SNMPPortPool",
            "key": "status",
            "value": "UP",
            "last_reported": "2018-04-16T00:11:08Z",
            "last_changed": "2018-04-16T00:11:08Z",
            "fail_counter": 0
        },
        {
            "reporter": "SNMPPortPool",
            "key": "traffic.in",
            "value": 1523837468,
            "last_reported": "2018-04-16T00:11:08Z",
            "last_changed": "2018-04-16T00:11:08Z",
            "fail_counter": 0
        }
    ]
}
```
