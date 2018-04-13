# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Edge Router" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "f4f54175-93fe-406b-ae66-dbca4df99e03", 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
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
    "resource_id": "f4f54175-93fe-406b-ae66-dbca4df99e03", 
    "field_name": "router", 
    "created_at": "2018-04-09T04:44:35Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.79.5.185"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/b88cbb53-f850-44f2-9960-95ade457e46c", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "router"
            }
        }
    }, 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "type": "snmp_device", 
    "id": "b88cbb53-f850-44f2-9960-95ade457e46c", 
    "resource_type": "edge_routers"
}
```

### This is JSON data for checking "Edge Router" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/b88cbb53-f850-44f2-9960-95ade457e46c
```

- Response

```
{
    "resource_id": "f4f54175-93fe-406b-ae66-dbca4df99e03", 
    "field_name": "router", 
    "created_at": "2018-04-09T04:44:35Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.79.5.185"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/b88cbb53-f850-44f2-9960-95ade457e46c", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "router"
            }
        }
    }, 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "values": [], 
    "type": "snmp_device", 
    "id": "b88cbb53-f850-44f2-9960-95ade457e46c", 
    "resource_type": "edge_routers"
}
```
and then ...
```
{
    "resource_id": "f4f54175-93fe-406b-ae66-dbca4df99e03", 
    "field_name": "router", 
    "created_at": "2018-04-09T04:44:35Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.79.5.185"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/b88cbb53-f850-44f2-9960-95ade457e46c", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "router"
            }
        }
    }, 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "values": [
        {
            "reporter": "SnmpDeviceAgent", 
            "last_reported": "2018-04-09T04:45:35Z", 
            "last_changed": "2018-04-09T04:45:35Z", 
            "value": "UP", 
            "key": "status", 
            "fail_counter": 0
        }
    ], 
    "type": "snmp_device", 
    "id": "b88cbb53-f850-44f2-9960-95ade457e46c", 
    "resource_type": "edge_routers"
}
```
