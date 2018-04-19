# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Ese Device" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "id": "aeaad149-357c-41b9-b408-6304c5d3396c",
    "created_at": "2018-04-15T23:59:29Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/aeaad149-357c-41b9-b408-6304c5d3396c",
    "type": "snmp_device",
    "resource_id": "4d8371c0-1b91-4818-a6e7-26425178e5d4",
    "resource_type": "ese_devices",
    "field_name": "switch",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "community_name": "***",
        "device_ip": "10.161.0.34"
    },
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "switch"
            }
        }
    }
}
```

- Response

```
{
    "id": "aeaad149-357c-41b9-b408-6304c5d3396c",
    "created_at": "2018-04-15T23:59:29Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/aeaad149-357c-41b9-b408-6304c5d3396c",
    "type": "snmp_device",
    "resource_id": "4d8371c0-1b91-4818-a6e7-26425178e5d4",
    "resource_type": "ese_devices",
    "field_name": "switch",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "community_name": "***",
        "device_ip": "10.161.0.34"
    },
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "switch"
            }
        }
    }
}
```

### This is JSON data for checking "Ese Device" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/aeaad149-357c-41b9-b408-6304c5d3396c
```

- Response

```
{
    "id": "aeaad149-357c-41b9-b408-6304c5d3396c",
    "created_at": "2018-04-15T23:59:29Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/aeaad149-357c-41b9-b408-6304c5d3396c",
    "type": "snmp_device",
    "resource_id": "4d8371c0-1b91-4818-a6e7-26425178e5d4",
    "resource_type": "ese_devices",
    "field_name": "switch",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "community_name": "***",
        "device_ip": "10.161.0.34"
    },
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "switch"
            }
        }
    },
    "values": []
}
```
and then ...
```
{
    "id": "aeaad149-357c-41b9-b408-6304c5d3396c",
    "created_at": "2018-04-15T23:59:29Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/aeaad149-357c-41b9-b408-6304c5d3396c",
    "type": "snmp_device",
    "resource_id": "4d8371c0-1b91-4818-a6e7-26425178e5d4",
    "resource_type": "ese_devices",
    "field_name": "switch",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "community_name": "***",
        "device_ip": "10.161.0.34"
    },
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "switch"
            }
        }
    },
    "values": [
        {
            "reporter": "SnmpDeviceAgent",
            "key": "status",
            "value": "UP",
            "last_reported": "2018-04-16T00:00:29Z",
            "last_changed": "2018-04-16T00:00:29Z",
            "fail_counter": 0
        }
    ]
}
```
