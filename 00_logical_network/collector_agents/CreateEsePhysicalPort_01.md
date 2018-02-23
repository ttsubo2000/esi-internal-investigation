# HTTP Methods for RESTful between heat-engine and CollectorAgents

### These are stored data for "Create Ese Physical Port" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "24dd42cf-b343-47a9-966a-8f7486378c46", 
    "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
    "version": 1, 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "port"
            }
        }
    }, 
    "field_name": "port", 
    "type": "snmp_ports_status", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.161.0.33", 
        "if_name": "xe-0/0/1"
    }, 
    "resource_type": "ese_physical_ports"
}
```

- Response

```
{
    "resource_id": "24dd42cf-b343-47a9-966a-8f7486378c46", 
    "field_name": "port", 
    "created_at": "2018-02-15T06:54:01Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.161.0.33", 
        "if_name": "xe-0/0/1"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 1, 
    "link": "http://collector-agents-se:7070/targets/a481c2c4-e9cd-41f3-8e27-3a4184119abf", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "port"
            }
        }
    }, 
    "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
    "type": "snmp_ports_status", 
    "id": "a481c2c4-e9cd-41f3-8e27-3a4184119abf", 
    "resource_type": "ese_physical_ports"
}
```

### This is JSON data for checking "Ese Physical Port" in HTTP Methods from heat-engine.

- Request

```
http://collector-agents-se.monitoringrefactordocker_default:7070/targets/a481c2c4-e9cd-41f3-8e27-3a4184119abf
```

- Response

```
{
    "resource_id": "24dd42cf-b343-47a9-966a-8f7486378c46", 
    "field_name": "port", 
    "created_at": "2018-02-15T06:54:01Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.161.0.33", 
        "if_name": "xe-0/0/1"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 1, 
    "link": "http://collector-agents-se:7070/targets/a481c2c4-e9cd-41f3-8e27-3a4184119abf", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "port"
            }
        }
    }, 
    "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
    "values": [], 
    "type": "snmp_ports_status", 
    "id": "a481c2c4-e9cd-41f3-8e27-3a4184119abf", 
    "resource_type": "ese_physical_ports"
}
```
and then ...
```
{
    "resource_id": "24dd42cf-b343-47a9-966a-8f7486378c46", 
    "field_name": "port", 
    "created_at": "2018-02-15T06:54:01Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.161.0.33", 
        "if_name": "xe-0/0/1"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 1, 
    "link": "http://collector-agents-se:7070/targets/a481c2c4-e9cd-41f3-8e27-3a4184119abf", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "port"
            }
        }
    }, 
    "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
    "values": [
        {
            "reporter": "SNMPPortPool", 
            "last_reported": "2018-02-15T06:55:01Z", 
            "last_changed": "2018-02-15T06:55:01Z", 
            "value": "UP", 
            "key": "status", 
            "fail_counter": 0
        }
    ], 
    "type": "snmp_ports_status", 
    "id": "a481c2c4-e9cd-41f3-8e27-3a4184119abf", 
    "resource_type": "ese_physical_ports"
}
```
