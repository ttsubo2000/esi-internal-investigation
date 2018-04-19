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
    "field_name": "secondary_router",
    "type": "snmp_ports_metric",
    "properties": {
        "community_name": "***",
        "device_ip": "10.79.5.184",
        "if_name": "ge-0/0/1.122"
    },
    "resource_type": "vpn_interfaces",
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes",
                "tags": {
                    "direction": "in",
                    "device_index": "secondary",
                    "resource_id": "07d4f1fc-5142-4fae-b115-627fc009e222"
                }
            },
            "traffic.out": {
                "metric": "traffic.bytes",
                "tags": {
                    "direction": "out",
                    "device_index": "secondary",
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
    "id": "3bdb3c86-ac6d-4ff2-aa55-4b2989971614",
    "created_at": "2018-04-16T00:10:08Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/3bdb3c86-ac6d-4ff2-aa55-4b2989971614",
    "type": "snmp_ports_metric",
    "resource_id": "07d4f1fc-5142-4fae-b115-627fc009e222",
    "resource_type": "vpn_interfaces",
    "field_name": "secondary_router",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "community_name": "***",
        "device_ip": "10.79.5.184",
        "if_name": "ge-0/0/1.122"
    },
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes",
                "tags": {
                    "device_index": "secondary",
                    "direction": "in",
                    "resource_id": "07d4f1fc-5142-4fae-b115-627fc009e222"
                }
            },
            "traffic.out": {
                "metric": "traffic.bytes",
                "tags": {
                    "device_index": "secondary",
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
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/3bdb3c86-ac6d-4ff2-aa55-4b2989971614
```

- Response

```
{
    "id": "3bdb3c86-ac6d-4ff2-aa55-4b2989971614",
    "created_at": "2018-04-16T00:10:08Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/3bdb3c86-ac6d-4ff2-aa55-4b2989971614",
    "type": "snmp_ports_metric",
    "resource_id": "07d4f1fc-5142-4fae-b115-627fc009e222",
    "resource_type": "vpn_interfaces",
    "field_name": "secondary_router",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "community_name": "***",
        "device_ip": "10.79.5.184",
        "if_name": "ge-0/0/1.122"
    },
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes",
                "tags": {
                    "device_index": "secondary",
                    "direction": "in",
                    "resource_id": "07d4f1fc-5142-4fae-b115-627fc009e222"
                }
            },
            "traffic.out": {
                "metric": "traffic.bytes",
                "tags": {
                    "device_index": "secondary",
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
    "id": "3bdb3c86-ac6d-4ff2-aa55-4b2989971614",
    "created_at": "2018-04-16T00:10:08Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/3bdb3c86-ac6d-4ff2-aa55-4b2989971614",
    "type": "snmp_ports_metric",
    "resource_id": "07d4f1fc-5142-4fae-b115-627fc009e222",
    "resource_type": "vpn_interfaces",
    "field_name": "secondary_router",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "community_name": "***",
        "device_ip": "10.79.5.184",
        "if_name": "ge-0/0/1.122"
    },
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes",
                "tags": {
                    "device_index": "secondary",
                    "direction": "in",
                    "resource_id": "07d4f1fc-5142-4fae-b115-627fc009e222"
                }
            },
            "traffic.out": {
                "metric": "traffic.bytes",
                "tags": {
                    "device_index": "secondary",
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
            "last_reported": "2018-04-16T00:11:09Z",
            "last_changed": "2018-04-16T00:11:09Z",
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
