# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Edge Router" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "ca43aedb-bc30-4355-a931-7bb1d9040659", 
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
        "device_ip": "10.79.5.184"
    }, 
    "resource_type": "edge_routers"
}
```

- Response

```
{
    "resource_id": "ca43aedb-bc30-4355-a931-7bb1d9040659", 
    "field_name": "router", 
    "created_at": "2018-04-04T04:56:48Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.79.5.184"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/538cfead-67e3-4e5b-87a4-ad8f32b14366", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "router"
            }
        }
    }, 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "type": "snmp_device", 
    "id": "538cfead-67e3-4e5b-87a4-ad8f32b14366", 
    "resource_type": "edge_routers"
}
```

### This is JSON data for checking "Edge Router" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/538cfead-67e3-4e5b-87a4-ad8f32b14366
```

- Response

```
{
    "resource_id": "ca43aedb-bc30-4355-a931-7bb1d9040659", 
    "field_name": "router", 
    "created_at": "2018-04-04T04:56:48Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.79.5.184"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/538cfead-67e3-4e5b-87a4-ad8f32b14366", 
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
    "id": "538cfead-67e3-4e5b-87a4-ad8f32b14366", 
    "resource_type": "edge_routers"
}
```
and then ...
```
{
    "resource_id": "ca43aedb-bc30-4355-a931-7bb1d9040659", 
    "field_name": "router", 
    "created_at": "2018-04-04T04:56:48Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.79.5.184"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/538cfead-67e3-4e5b-87a4-ad8f32b14366", 
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
            "last_reported": "2018-04-04T04:57:48Z", 
            "last_changed": "2018-04-04T04:57:48Z", 
            "value": "UP", 
            "key": "status", 
            "fail_counter": 0
        }
    ], 
    "type": "snmp_device", 
    "id": "538cfead-67e3-4e5b-87a4-ad8f32b14366", 
    "resource_type": "edge_routers"
}
```
