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
    "resource_id": "2bc8e40d-ab01-4738-a4aa-e69d8fd30688",
    "field_name": "interface",
    "type": "snmp_ports_status",
    "properties": {
        "community_name": "***",
        "device_ip": "10.79.5.184",
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
    "id": "d80c91c1-a82c-4742-b571-03c17cbeff1c",
    "created_at": "2018-04-16T00:08:02Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/d80c91c1-a82c-4742-b571-03c17cbeff1c",
    "type": "snmp_ports_status",
    "resource_id": "2bc8e40d-ab01-4738-a4aa-e69d8fd30688",
    "resource_type": "er_physical_interfaces",
    "field_name": "interface",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "community_name": "***",
        "device_ip": "10.79.5.184",
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
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/d80c91c1-a82c-4742-b571-03c17cbeff1c
```

- Response

```
{
    "id": "d80c91c1-a82c-4742-b571-03c17cbeff1c",
    "created_at": "2018-04-16T00:08:02Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/d80c91c1-a82c-4742-b571-03c17cbeff1c",
    "type": "snmp_ports_status",
    "resource_id": "2bc8e40d-ab01-4738-a4aa-e69d8fd30688",
    "resource_type": "er_physical_interfaces",
    "field_name": "interface",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "community_name": "***",
        "device_ip": "10.79.5.184",
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
    "id": "d80c91c1-a82c-4742-b571-03c17cbeff1c",
    "created_at": "2018-04-16T00:08:02Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/d80c91c1-a82c-4742-b571-03c17cbeff1c",
    "type": "snmp_ports_status",
    "resource_id": "2bc8e40d-ab01-4738-a4aa-e69d8fd30688",
    "resource_type": "er_physical_interfaces",
    "field_name": "interface",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "community_name": "***",
        "device_ip": "10.79.5.184",
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
            "last_reported": "2018-04-16T00:08:58Z",
            "last_changed": "2018-04-16T00:08:58Z",
            "fail_counter": 0
        }
    ]
}
```
