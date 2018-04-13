# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Er Physical Interface" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "c2576120-00b0-461e-a2ae-f7bbff9465d0", 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "version": 1, 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "interface"
            }
        }
    }, 
    "field_name": "interface", 
    "type": "snmp_ports_status", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.79.5.185", 
        "if_name": "ae0"
    }, 
    "resource_type": "er_physical_interfaces"
}
```

- Response

```
{
    "resource_id": "c2576120-00b0-461e-a2ae-f7bbff9465d0", 
    "field_name": "interface", 
    "created_at": "2018-04-09T04:46:45Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.79.5.185", 
        "if_name": "ae0"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/23d9d390-e1e3-41c7-b926-479d6909aeeb", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "interface"
            }
        }
    }, 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "type": "snmp_ports_status", 
    "id": "23d9d390-e1e3-41c7-b926-479d6909aeeb", 
    "resource_type": "er_physical_interfaces"
}
```

### This is JSON data for checking "Er Physical Interface" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/23d9d390-e1e3-41c7-b926-479d6909aeeb
```

- Response

```
{
    "resource_id": "c2576120-00b0-461e-a2ae-f7bbff9465d0", 
    "field_name": "interface", 
    "created_at": "2018-04-09T04:46:45Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.79.5.185", 
        "if_name": "ae0"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/23d9d390-e1e3-41c7-b926-479d6909aeeb", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "interface"
            }
        }
    }, 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "values": [], 
    "type": "snmp_ports_status", 
    "id": "23d9d390-e1e3-41c7-b926-479d6909aeeb", 
    "resource_type": "er_physical_interfaces"
}
```
and then ...
```
{
    "resource_id": "c2576120-00b0-461e-a2ae-f7bbff9465d0", 
    "field_name": "interface", 
    "created_at": "2018-04-09T04:46:45Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.79.5.185", 
        "if_name": "ae0"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/23d9d390-e1e3-41c7-b926-479d6909aeeb", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "interface"
            }
        }
    }, 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "values": [
        {
            "reporter": "SNMPPortPool", 
            "last_reported": "2018-04-09T04:47:45Z", 
            "last_changed": "2018-04-09T04:47:45Z", 
            "value": "UP", 
            "key": "status", 
            "fail_counter": 0
        }
    ], 
    "type": "snmp_ports_status", 
    "id": "23d9d390-e1e3-41c7-b926-479d6909aeeb", 
    "resource_type": "er_physical_interfaces"
}
```
