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
    "resource_id": "b7e6d8ad-5377-4380-bbb4-1a62566cbd6d",
    "field_name": "router",
    "type": "snmp_device",
    "properties": {
        "community_name": "***",
        "device_ip": "10.79.5.184"
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
    "id": "1e628441-c77a-4ebe-b5fe-6bd69816456d",
    "created_at": "2018-04-16T00:03:46Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/1e628441-c77a-4ebe-b5fe-6bd69816456d",
    "type": "snmp_device",
    "resource_id": "b7e6d8ad-5377-4380-bbb4-1a62566cbd6d",
    "resource_type": "edge_routers",
    "field_name": "router",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "community_name": "***",
        "device_ip": "10.79.5.184"
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
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/1e628441-c77a-4ebe-b5fe-6bd69816456d
```

- Response

```
{
    "id": "1e628441-c77a-4ebe-b5fe-6bd69816456d",
    "created_at": "2018-04-16T00:03:46Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/1e628441-c77a-4ebe-b5fe-6bd69816456d",
    "type": "snmp_device",
    "resource_id": "b7e6d8ad-5377-4380-bbb4-1a62566cbd6d",
    "resource_type": "edge_routers",
    "field_name": "router",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "community_name": "***",
        "device_ip": "10.79.5.184"
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
    "id": "1e628441-c77a-4ebe-b5fe-6bd69816456d",
    "created_at": "2018-04-16T00:03:46Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/1e628441-c77a-4ebe-b5fe-6bd69816456d",
    "type": "snmp_device",
    "resource_id": "b7e6d8ad-5377-4380-bbb4-1a62566cbd6d",
    "resource_type": "edge_routers",
    "field_name": "router",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "community_name": "***",
        "device_ip": "10.79.5.184"
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
            "last_reported": "2018-04-16T00:04:46Z",
            "last_changed": "2018-04-16T00:04:46Z",
            "fail_counter": 0
        }
    ]
}
```
