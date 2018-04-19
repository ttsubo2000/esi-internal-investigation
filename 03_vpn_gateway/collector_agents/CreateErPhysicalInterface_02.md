# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Er Physical Interface" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "resource_id": "3118d6be-b1cb-472a-805f-7e1ec46aa5e7",
    "field_name": "interface",
    "type": "snmp_ports_status",
    "properties": {
        "community_name": "***",
        "device_ip": "10.79.5.185",
        "if_name": "ae0"
    },
    "resource_type": "er_physical_interfaces",
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "interface"
            }
        }
    }
}
```

- Response

```
{
    "id": "e848bb97-1643-4167-9865-9a8b3b30b66f",
    "created_at": "2018-04-16T00:05:57Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/e848bb97-1643-4167-9865-9a8b3b30b66f",
    "type": "snmp_ports_status",
    "resource_id": "3118d6be-b1cb-472a-805f-7e1ec46aa5e7",
    "resource_type": "er_physical_interfaces",
    "field_name": "interface",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "community_name": "***",
        "device_ip": "10.79.5.185",
        "if_name": "ae0"
    },
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "interface"
            }
        }
    }
}
```

### This is JSON data for checking "Er Physical Interface" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/e848bb97-1643-4167-9865-9a8b3b30b66f
```

- Response

```
{
    "id": "e848bb97-1643-4167-9865-9a8b3b30b66f",
    "created_at": "2018-04-16T00:05:57Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/e848bb97-1643-4167-9865-9a8b3b30b66f",
    "type": "snmp_ports_status",
    "resource_id": "3118d6be-b1cb-472a-805f-7e1ec46aa5e7",
    "resource_type": "er_physical_interfaces",
    "field_name": "interface",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "community_name": "***",
        "device_ip": "10.79.5.185",
        "if_name": "ae0"
    },
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "interface"
            }
        }
    },
    "values": []
}
```
and then ...
```
{
    "id": "e848bb97-1643-4167-9865-9a8b3b30b66f",
    "created_at": "2018-04-16T00:05:57Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/e848bb97-1643-4167-9865-9a8b3b30b66f",
    "type": "snmp_ports_status",
    "resource_id": "3118d6be-b1cb-472a-805f-7e1ec46aa5e7",
    "resource_type": "er_physical_interfaces",
    "field_name": "interface",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "community_name": "***",
        "device_ip": "10.79.5.185",
        "if_name": "ae0"
    },
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "interface"
            }
        }
    },
    "values": [
        {
            "reporter": "SNMPPortPool",
            "key": "status",
            "value": "UP",
            "last_reported": "2018-04-16T00:06:53Z",
            "last_changed": "2018-04-16T00:06:53Z",
            "fail_counter": 0
        }
    ]
}
```
