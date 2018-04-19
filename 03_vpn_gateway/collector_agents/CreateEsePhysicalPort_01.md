# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Ese Physical Port" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "resource_id": "0078808a-c28e-46e1-887d-8ec65f90c446",
    "field_name": "port",
    "type": "snmp_ports_status",
    "properties": {
        "community_name": "***",
        "device_ip": "10.161.0.34",
        "if_name": "xe-0/0/3"
    },
    "resource_type": "ese_physical_ports",
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "port"
            }
        }
    }
}
```

- Response

```
{
    "id": "28c45b87-a1c0-41f0-8f69-85c60d47713f",
    "created_at": "2018-04-16T00:00:37Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/28c45b87-a1c0-41f0-8f69-85c60d47713f",
    "type": "snmp_ports_status",
    "resource_id": "0078808a-c28e-46e1-887d-8ec65f90c446",
    "resource_type": "ese_physical_ports",
    "field_name": "port",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "community_name": "***",
        "device_ip": "10.161.0.34",
        "if_name": "xe-0/0/3"
    },
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "port"
            }
        }
    }
}
```

### This is JSON data for checking "Ese Physical Port" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/28c45b87-a1c0-41f0-8f69-85c60d47713f
```

- Response

```
{
    "id": "28c45b87-a1c0-41f0-8f69-85c60d47713f",
    "created_at": "2018-04-16T00:00:37Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/28c45b87-a1c0-41f0-8f69-85c60d47713f",
    "type": "snmp_ports_status",
    "resource_id": "0078808a-c28e-46e1-887d-8ec65f90c446",
    "resource_type": "ese_physical_ports",
    "field_name": "port",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "community_name": "***",
        "device_ip": "10.161.0.34",
        "if_name": "xe-0/0/3"
    },
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "port"
            }
        }
    },
    "values": []
}
```
and then ...
```
{
    "id": "28c45b87-a1c0-41f0-8f69-85c60d47713f",
    "created_at": "2018-04-16T00:00:37Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/28c45b87-a1c0-41f0-8f69-85c60d47713f",
    "type": "snmp_ports_status",
    "resource_id": "0078808a-c28e-46e1-887d-8ec65f90c446",
    "resource_type": "ese_physical_ports",
    "field_name": "port",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "community_name": "***",
        "device_ip": "10.161.0.34",
        "if_name": "xe-0/0/3"
    },
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "port"
            }
        }
    },
    "values": [
        {
            "reporter": "SNMPPortPool",
            "key": "status",
            "value": "UP",
            "last_reported": "2018-04-16T00:01:37Z",
            "last_changed": "2018-04-16T00:01:37Z",
            "fail_counter": 0
        }
    ]
}
```
