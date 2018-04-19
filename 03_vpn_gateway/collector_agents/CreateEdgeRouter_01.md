# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Edge Router" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "resource_id": "7a35974a-a19f-49e2-b907-ad7fd8692975",
    "field_name": "router",
    "type": "snmp_device",
    "properties": {
        "community_name": "***",
        "device_ip": "10.79.5.185"
    },
    "resource_type": "edge_routers",
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "router"
            }
        }
    }
}
```

- Response

```
{
    "id": "cc896303-29e2-47d6-a409-a84c23b5722b",
    "created_at": "2018-04-16T00:02:42Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/cc896303-29e2-47d6-a409-a84c23b5722b",
    "type": "snmp_device",
    "resource_id": "7a35974a-a19f-49e2-b907-ad7fd8692975",
    "resource_type": "edge_routers",
    "field_name": "router",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "community_name": "***",
        "device_ip": "10.79.5.185"
    },
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "router"
            }
        }
    }
}
```

### This is JSON data for checking "Edge Router" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/cc896303-29e2-47d6-a409-a84c23b5722b
```

- Response

```
{
    "id": "cc896303-29e2-47d6-a409-a84c23b5722b",
    "created_at": "2018-04-16T00:02:42Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/cc896303-29e2-47d6-a409-a84c23b5722b",
    "type": "snmp_device",
    "resource_id": "7a35974a-a19f-49e2-b907-ad7fd8692975",
    "resource_type": "edge_routers",
    "field_name": "router",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "community_name": "***",
        "device_ip": "10.79.5.185"
    },
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "router"
            }
        }
    },
    "values": []
}
```
and then ...
```
{
    "id": "cc896303-29e2-47d6-a409-a84c23b5722b",
    "created_at": "2018-04-16T00:02:42Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/cc896303-29e2-47d6-a409-a84c23b5722b",
    "type": "snmp_device",
    "resource_id": "7a35974a-a19f-49e2-b907-ad7fd8692975",
    "resource_type": "edge_routers",
    "field_name": "router",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "community_name": "***",
        "device_ip": "10.79.5.185"
    },
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "router"
            }
        }
    },
    "values": [
        {
            "reporter": "SnmpDeviceAgent",
            "key": "status",
            "value": "UP",
            "last_reported": "2018-04-16T00:03:42Z",
            "last_changed": "2018-04-16T00:03:42Z",
            "fail_counter": 0
        }
    ]
}
```
