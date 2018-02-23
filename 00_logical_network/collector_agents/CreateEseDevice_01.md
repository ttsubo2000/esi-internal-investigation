# HTTP Methods for RESTful between heat-engine and CollectorAgents

### This is JSON data for "Create Ese Device" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "718148aa-4483-47d5-bbd1-a0e0738dc018", 
    "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
    "version": 1, 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "switch"
            }
        }
    }, 
    "field_name": "switch", 
    "type": "snmp_device", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.161.0.33"
    }, 
    "resource_type": "ese_devices"
}
```

- Response

```
{
    "resource_id": "718148aa-4483-47d5-bbd1-a0e0738dc018", 
    "field_name": "switch", 
    "created_at": "2018-02-15T06:52:49Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.161.0.33"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 1, 
    "link": "http://collector-agents-se:7070/targets/edd4b769-1665-429f-aef4-f428aca34a0b", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "switch"
            }
        }
    }, 
    "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
    "type": "snmp_device", 
    "id": "edd4b769-1665-429f-aef4-f428aca34a0b", 
    "resource_type": "ese_devices"
}
```

### This is JSON data for checking "Ese Device" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/edd4b769-1665-429f-aef4-f428aca34a0b
```

- Response

```
{
    "resource_id": "718148aa-4483-47d5-bbd1-a0e0738dc018", 
    "field_name": "switch", 
    "created_at": "2018-02-15T06:52:49Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.161.0.33"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 1, 
    "link": "http://collector-agents-se:7070/targets/edd4b769-1665-429f-aef4-f428aca34a0b", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "switch"
            }
        }
    }, 
    "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
    "values": [], 
    "type": "snmp_device", 
    "id": "edd4b769-1665-429f-aef4-f428aca34a0b", 
    "resource_type": "ese_devices"
}
```
and then ...
```
{
    "resource_id": "718148aa-4483-47d5-bbd1-a0e0738dc018", 
    "field_name": "switch", 
    "created_at": "2018-02-15T06:52:49Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.161.0.33"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 1, 
    "link": "http://collector-agents-se:7070/targets/edd4b769-1665-429f-aef4-f428aca34a0b", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "switch"
            }
        }
    }, 
    "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
    "values": [
        {
            "reporter": "SnmpDeviceAgent", 
            "last_reported": "2018-02-15T06:53:49Z", 
            "last_changed": "2018-02-15T06:53:49Z", 
            "value": "UP", 
            "key": "status", 
            "fail_counter": 0
        }
    ], 
    "type": "snmp_device", 
    "id": "edd4b769-1665-429f-aef4-f428aca34a0b", 
    "resource_type": "ese_devices"
}
```
