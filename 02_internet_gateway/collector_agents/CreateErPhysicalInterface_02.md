# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Er Physical Interface" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "d108a472-81ab-43a0-8c49-e0d1a46e6128", 
    "field_name": "interface", 
    "created_at": "2018-04-04T04:59:00Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.79.5.184", 
        "if_name": "ae0"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/79b7fc42-ebaf-4c34-adeb-20b43803a4fc", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "interface"
            }
        }
    }, 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "type": "snmp_ports_status", 
    "id": "79b7fc42-ebaf-4c34-adeb-20b43803a4fc", 
    "resource_type": "er_physical_interfaces"
}
```

- Response

```
```

### This is JSON data for checking "Er Physical Interface" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/79b7fc42-ebaf-4c34-adeb-20b43803a4fc
```

- Response

```
{
    "resource_id": "d108a472-81ab-43a0-8c49-e0d1a46e6128", 
    "field_name": "interface", 
    "created_at": "2018-04-04T04:59:00Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.79.5.184", 
        "if_name": "ae0"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/79b7fc42-ebaf-4c34-adeb-20b43803a4fc", 
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
    "id": "79b7fc42-ebaf-4c34-adeb-20b43803a4fc", 
    "resource_type": "er_physical_interfaces"
}
```
and then ...
```
{
    "resource_id": "d108a472-81ab-43a0-8c49-e0d1a46e6128", 
    "field_name": "interface", 
    "created_at": "2018-04-04T04:59:00Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.79.5.184", 
        "if_name": "ae0"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/79b7fc42-ebaf-4c34-adeb-20b43803a4fc", 
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
            "last_reported": "2018-04-04T05:00:00Z", 
            "last_changed": "2018-04-04T05:00:00Z", 
            "value": "UP", 
            "key": "status", 
            "fail_counter": 0
        }
    ], 
    "type": "snmp_ports_status", 
    "id": "79b7fc42-ebaf-4c34-adeb-20b43803a4fc", 
    "resource_type": "er_physical_interfaces"
}
```
