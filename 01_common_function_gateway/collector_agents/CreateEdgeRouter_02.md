# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Edge Router" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "2d056865-47a9-45cf-a890-ed10e3b5912a", 
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
        "device_ip": "10.79.5.184"
    }, 
    "resource_type": "edge_routers"
}
```

- Response

```
{
    "resource_id": "2d056865-47a9-45cf-a890-ed10e3b5912a", 
    "field_name": "router", 
    "created_at": "2018-04-09T04:45:39Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.79.5.184"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/ad464fbb-0810-447e-b10d-31715221cb95", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "router"
            }
        }
    }, 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "type": "snmp_device", 
    "id": "ad464fbb-0810-447e-b10d-31715221cb95", 
    "resource_type": "edge_routers"
}
```

### This is JSON data for checking "Edge Router" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/ad464fbb-0810-447e-b10d-31715221cb95
```

- Response

```
{
    "resource_id": "2d056865-47a9-45cf-a890-ed10e3b5912a", 
    "field_name": "router", 
    "created_at": "2018-04-09T04:45:39Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.79.5.184"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/ad464fbb-0810-447e-b10d-31715221cb95", 
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
    "id": "ad464fbb-0810-447e-b10d-31715221cb95", 
    "resource_type": "edge_routers"
}
```
and then ...
```
{
    "resource_id": "2d056865-47a9-45cf-a890-ed10e3b5912a", 
    "field_name": "router", 
    "created_at": "2018-04-09T04:45:39Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.79.5.184"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/ad464fbb-0810-447e-b10d-31715221cb95", 
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
            "last_reported": "2018-04-09T04:46:39Z", 
            "last_changed": "2018-04-09T04:46:39Z", 
            "value": "UP", 
            "key": "status", 
            "fail_counter": 0
        }
    ], 
    "type": "snmp_device", 
    "id": "ad464fbb-0810-447e-b10d-31715221cb95", 
    "resource_type": "edge_routers"
}
```
