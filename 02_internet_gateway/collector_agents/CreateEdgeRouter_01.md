# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Edge Router" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "cbe0fe23-8461-4a71-a7cc-a3a1d8c1fd78", 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "version": 1, 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "router"
            }
        }
    }, 
    "field_name": "router", 
    "type": "snmp_device", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.79.5.185"
    }, 
    "resource_type": "edge_routers"
}
```

- Response

```
{
    "resource_id": "cbe0fe23-8461-4a71-a7cc-a3a1d8c1fd78", 
    "field_name": "router", 
    "created_at": "2018-04-04T04:55:44Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.79.5.185"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/9363d0ec-e347-482c-8d0d-da1d8e11ad73", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "router"
            }
        }
    }, 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "type": "snmp_device", 
    "id": "9363d0ec-e347-482c-8d0d-da1d8e11ad73", 
    "resource_type": "edge_routers"
}
```

### This is JSON data for checking "Edge Router" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/9363d0ec-e347-482c-8d0d-da1d8e11ad73
```

- Response

```
{
    "resource_id": "cbe0fe23-8461-4a71-a7cc-a3a1d8c1fd78", 
    "field_name": "router", 
    "created_at": "2018-04-04T04:55:44Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.79.5.185"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/9363d0ec-e347-482c-8d0d-da1d8e11ad73", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "router"
            }
        }
    }, 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "values": [], 
    "type": "snmp_device", 
    "id": "9363d0ec-e347-482c-8d0d-da1d8e11ad73", 
    "resource_type": "edge_routers"
}
```
and then ...
```
{
    "resource_id": "cbe0fe23-8461-4a71-a7cc-a3a1d8c1fd78", 
    "field_name": "router", 
    "created_at": "2018-04-04T04:55:44Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.79.5.185"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/9363d0ec-e347-482c-8d0d-da1d8e11ad73", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "router"
            }
        }
    }, 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "values": [
        {
            "reporter": "SnmpDeviceAgent", 
            "last_reported": "2018-04-04T04:56:44Z", 
            "last_changed": "2018-04-04T04:56:44Z", 
            "value": "UP", 
            "key": "status", 
            "fail_counter": 0
        }
    ], 
    "type": "snmp_device", 
    "id": "9363d0ec-e347-482c-8d0d-da1d8e11ad73", 
    "resource_type": "edge_routers"
}
```
