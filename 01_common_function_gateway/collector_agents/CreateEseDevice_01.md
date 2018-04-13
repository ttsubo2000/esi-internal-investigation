# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Ese Device" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "cc214b6a-2f09-4094-b7cd-a9590f64b854", 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
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
    "resource_id": "cc214b6a-2f09-4094-b7cd-a9590f64b854", 
    "field_name": "switch", 
    "created_at": "2018-04-09T04:41:23Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.161.0.34"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/2762cfcb-575c-45cc-a07b-ca19f5b007cd", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "switch"
            }
        }
    }, 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "type": "snmp_device", 
    "id": "2762cfcb-575c-45cc-a07b-ca19f5b007cd", 
    "resource_type": "ese_devices"
}
```

### This is JSON data for checking "Ese Device" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/2762cfcb-575c-45cc-a07b-ca19f5b007cd
```

- Response

```
{
    "resource_id": "cc214b6a-2f09-4094-b7cd-a9590f64b854", 
    "field_name": "switch", 
    "created_at": "2018-04-09T04:41:23Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.161.0.34"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/2762cfcb-575c-45cc-a07b-ca19f5b007cd", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "switch"
            }
        }
    }, 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "values": [], 
    "type": "snmp_device", 
    "id": "2762cfcb-575c-45cc-a07b-ca19f5b007cd", 
    "resource_type": "ese_devices"
}
```
and then ...
```
{
    "resource_id": "cc214b6a-2f09-4094-b7cd-a9590f64b854", 
    "field_name": "switch", 
    "created_at": "2018-04-09T04:41:23Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.161.0.34"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/2762cfcb-575c-45cc-a07b-ca19f5b007cd", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "switch"
            }
        }
    }, 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "values": [
        {
            "reporter": "SnmpDeviceAgent", 
            "last_reported": "2018-04-09T04:42:23Z", 
            "last_changed": "2018-04-09T04:42:23Z", 
            "value": "UP", 
            "key": "status", 
            "fail_counter": 0
        }
    ], 
    "type": "snmp_device", 
    "id": "2762cfcb-575c-45cc-a07b-ca19f5b007cd", 
    "resource_type": "ese_devices"
}
```
