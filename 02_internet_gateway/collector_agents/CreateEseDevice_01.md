# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Ese Device" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "3fb53223-b614-46b6-92e8-25c3bcbed214", 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
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
        "device_ip": "10.161.0.34"
    }, 
    "resource_type": "ese_devices"
}
```

- Response

```
{
    "resource_id": "3fb53223-b614-46b6-92e8-25c3bcbed214", 
    "field_name": "switch", 
    "created_at": "2018-04-04T04:52:29Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.161.0.34"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/bd8bbbcc-b175-4ea2-bfce-9821677d4da4", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "switch"
            }
        }
    }, 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "type": "snmp_device", 
    "id": "bd8bbbcc-b175-4ea2-bfce-9821677d4da4", 
    "resource_type": "ese_devices"
}
```

### This is JSON data for checking "Ese Device" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/bd8bbbcc-b175-4ea2-bfce-9821677d4da4
```

- Response

```
{
    "resource_id": "3fb53223-b614-46b6-92e8-25c3bcbed214", 
    "field_name": "switch", 
    "created_at": "2018-04-04T04:52:29Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.161.0.34"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/bd8bbbcc-b175-4ea2-bfce-9821677d4da4", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "switch"
            }
        }
    }, 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "values": [], 
    "type": "snmp_device", 
    "id": "bd8bbbcc-b175-4ea2-bfce-9821677d4da4", 
    "resource_type": "ese_devices"
}
```
and then ...
```
{
    "resource_id": "3fb53223-b614-46b6-92e8-25c3bcbed214", 
    "field_name": "switch", 
    "created_at": "2018-04-04T04:52:29Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.161.0.34"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/bd8bbbcc-b175-4ea2-bfce-9821677d4da4", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "switch"
            }
        }
    }, 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "values": [
        {
            "reporter": "SnmpDeviceAgent", 
            "last_reported": "2018-04-04T04:53:29Z", 
            "last_changed": "2018-04-04T04:53:29Z", 
            "value": "UP", 
            "key": "status", 
            "fail_counter": 0
        }
    ], 
    "type": "snmp_device", 
    "id": "bd8bbbcc-b175-4ea2-bfce-9821677d4da4", 
    "resource_type": "ese_devices"
}
```
