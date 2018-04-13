# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Ese Physical Port" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "9451c9ca-289d-42ba-846d-359c448e910c", 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "version": 1, 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "port"
            }
        }
    }, 
    "field_name": "port", 
    "type": "snmp_ports_status", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.161.0.34", 
        "if_name": "xe-0/0/3"
    }, 
    "resource_type": "ese_physical_ports"
}
```

- Response

```
{
    "resource_id": "9451c9ca-289d-42ba-846d-359c448e910c", 
    "field_name": "port", 
    "created_at": "2018-04-09T04:42:30Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.161.0.34", 
        "if_name": "xe-0/0/3"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/78d717f0-66d9-4f82-afe6-833c5e8f38f5", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "port"
            }
        }
    }, 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "type": "snmp_ports_status", 
    "id": "78d717f0-66d9-4f82-afe6-833c5e8f38f5", 
    "resource_type": "ese_physical_ports"
}
```

### This is JSON data for checking "Ese Physical Port" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/78d717f0-66d9-4f82-afe6-833c5e8f38f5
```

- Response

```
{
    "resource_id": "9451c9ca-289d-42ba-846d-359c448e910c", 
    "field_name": "port", 
    "created_at": "2018-04-09T04:42:30Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.161.0.34", 
        "if_name": "xe-0/0/3"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/78d717f0-66d9-4f82-afe6-833c5e8f38f5", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "port"
            }
        }
    }, 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "values": [], 
    "type": "snmp_ports_status", 
    "id": "78d717f0-66d9-4f82-afe6-833c5e8f38f5", 
    "resource_type": "ese_physical_ports"
}
```
and then ...
```
{
    "resource_id": "9451c9ca-289d-42ba-846d-359c448e910c", 
    "field_name": "port", 
    "created_at": "2018-04-09T04:42:30Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.161.0.34", 
        "if_name": "xe-0/0/3"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/78d717f0-66d9-4f82-afe6-833c5e8f38f5", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "port"
            }
        }
    }, 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "values": [
        {
            "reporter": "SNMPPortPool", 
            "last_reported": "2018-04-09T04:43:30Z", 
            "last_changed": "2018-04-09T04:43:30Z", 
            "value": "UP", 
            "key": "status", 
            "fail_counter": 0
        }
    ], 
    "type": "snmp_ports_status", 
    "id": "78d717f0-66d9-4f82-afe6-833c5e8f38f5", 
    "resource_type": "ese_physical_ports"
}
```
