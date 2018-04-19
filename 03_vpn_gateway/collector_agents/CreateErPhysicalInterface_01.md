# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Er Physical Interface" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "resource_id": "f3ecf585-5c3b-445a-97a7-d8e124c99e16",
    "field_name": "interface",
    "type": "snmp_ports_status",
    "properties": {
        "community_name": "***",
        "device_ip": "10.79.5.185",
        "if_name": "ge-0/0/1"
    },
    "resource_type": "er_physical_interfaces",
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "interface"
            }
        }
    }
}
```

- Response

```
{
    "id": "03bc2bdc-e6b0-4ae6-acda-b76a5da84fb6",
    "created_at": "2018-04-16T00:04:53Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/03bc2bdc-e6b0-4ae6-acda-b76a5da84fb6",
    "type": "snmp_ports_status",
    "resource_id": "f3ecf585-5c3b-445a-97a7-d8e124c99e16",
    "resource_type": "er_physical_interfaces",
    "field_name": "interface",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "community_name": "***",
        "device_ip": "10.79.5.185",
        "if_name": "ge-0/0/1"
    },
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "interface"
            }
        }
    }
}
```

### This is JSON data for checking "Er Physical Interface" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/03bc2bdc-e6b0-4ae6-acda-b76a5da84fb6
```

- Response

```
{
    "id": "03bc2bdc-e6b0-4ae6-acda-b76a5da84fb6",
    "created_at": "2018-04-16T00:04:53Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/03bc2bdc-e6b0-4ae6-acda-b76a5da84fb6",
    "type": "snmp_ports_status",
    "resource_id": "f3ecf585-5c3b-445a-97a7-d8e124c99e16",
    "resource_type": "er_physical_interfaces",
    "field_name": "interface",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "community_name": "***",
        "device_ip": "10.79.5.185",
        "if_name": "ge-0/0/1"
    },
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "interface"
            }
        }
    },
    "values": []
}
```
and then ...
```
{
    "id": "03bc2bdc-e6b0-4ae6-acda-b76a5da84fb6",
    "created_at": "2018-04-16T00:04:53Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/03bc2bdc-e6b0-4ae6-acda-b76a5da84fb6",
    "type": "snmp_ports_status",
    "resource_id": "f3ecf585-5c3b-445a-97a7-d8e124c99e16",
    "resource_type": "er_physical_interfaces",
    "field_name": "interface",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "community_name": "***",
        "device_ip": "10.79.5.185",
        "if_name": "ge-0/0/1"
    },
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "interface"
            }
        }
    },
    "values": [
        {
            "reporter": "SNMPPortPool",
            "key": "status",
            "value": "UP",
            "last_reported": "2018-04-16T00:05:53Z",
            "last_changed": "2018-04-16T00:05:53Z",
            "fail_counter": 0
        }
    ]
}
```
