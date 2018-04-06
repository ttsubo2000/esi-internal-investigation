# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Er Physical Interface" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "53712736-354c-4374-be82-6f07bea9d1bd", 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
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
    "resource_id": "53712736-354c-4374-be82-6f07bea9d1bd", 
    "field_name": "interface", 
    "created_at": "2018-04-04T04:57:55Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.79.5.185", 
        "if_name": "ae0"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/c38b03bf-0c61-44ff-9dec-599c9951df58", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "interface"
            }
        }
    }, 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "type": "snmp_ports_status", 
    "id": "c38b03bf-0c61-44ff-9dec-599c9951df58", 
    "resource_type": "er_physical_interfaces"
}
```

### This is JSON data for checking "Er Physical Interface" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/c38b03bf-0c61-44ff-9dec-599c9951df58
```

- Response

```
{
    "resource_id": "53712736-354c-4374-be82-6f07bea9d1bd", 
    "field_name": "interface", 
    "created_at": "2018-04-04T04:57:55Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.79.5.185", 
        "if_name": "ae0"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/c38b03bf-0c61-44ff-9dec-599c9951df58", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "interface"
            }
        }
    }, 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "values": [], 
    "type": "snmp_ports_status", 
    "id": "c38b03bf-0c61-44ff-9dec-599c9951df58", 
    "resource_type": "er_physical_interfaces"
}
```
and then ...
```
{
    "resource_id": "53712736-354c-4374-be82-6f07bea9d1bd", 
    "field_name": "interface", 
    "created_at": "2018-04-04T04:57:55Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.79.5.185", 
        "if_name": "ae0"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/c38b03bf-0c61-44ff-9dec-599c9951df58", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "interface"
            }
        }
    }, 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "values": [
        {
            "reporter": "SNMPPortPool", 
            "last_reported": "2018-04-04T04:58:55Z", 
            "last_changed": "2018-04-04T04:58:55Z", 
            "value": "UP", 
            "key": "status", 
            "fail_counter": 0
        }
    ], 
    "type": "snmp_ports_status", 
    "id": "c38b03bf-0c61-44ff-9dec-599c9951df58", 
    "resource_type": "er_physical_interfaces"
}
```
