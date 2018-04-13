# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Er Physical Interface" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "b9c7c1f4-1b90-4a7a-8161-34276bb2ed10", 
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
        "device_ip": "10.79.5.184", 
        "if_name": "ae0"
    }, 
    "resource_type": "er_physical_interfaces"
}
```

- Response

```
{
    "resource_id": "b9c7c1f4-1b90-4a7a-8161-34276bb2ed10", 
    "field_name": "interface", 
    "created_at": "2018-04-09T04:47:50Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.79.5.184", 
        "if_name": "ae0"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/17d442df-0ac4-4c5e-bbef-34fc7e4c4b06", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "interface"
            }
        }
    }, 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "type": "snmp_ports_status", 
    "id": "17d442df-0ac4-4c5e-bbef-34fc7e4c4b06", 
    "resource_type": "er_physical_interfaces"
}
```

### This is JSON data for checking "Er Physical Interface" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/17d442df-0ac4-4c5e-bbef-34fc7e4c4b06
```

- Response

```
{
    "resource_id": "b9c7c1f4-1b90-4a7a-8161-34276bb2ed10", 
    "field_name": "interface", 
    "created_at": "2018-04-09T04:47:50Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.79.5.184", 
        "if_name": "ae0"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/17d442df-0ac4-4c5e-bbef-34fc7e4c4b06", 
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
    "id": "17d442df-0ac4-4c5e-bbef-34fc7e4c4b06", 
    "resource_type": "er_physical_interfaces"
}
```
and then ...
```
{
    "resource_id": "b9c7c1f4-1b90-4a7a-8161-34276bb2ed10", 
    "field_name": "interface", 
    "created_at": "2018-04-09T04:47:50Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.79.5.184", 
        "if_name": "ae0"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/17d442df-0ac4-4c5e-bbef-34fc7e4c4b06", 
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
            "last_reported": "2018-04-09T04:48:50Z", 
            "last_changed": "2018-04-09T04:48:50Z", 
            "value": "UP", 
            "key": "status", 
            "fail_counter": 0
        }
    ], 
    "type": "snmp_ports_status", 
    "id": "17d442df-0ac4-4c5e-bbef-34fc7e4c4b06", 
    "resource_type": "er_physical_interfaces"
}
```
