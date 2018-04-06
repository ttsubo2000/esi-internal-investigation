# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Ese Physical Port" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "6b29894f-8694-4865-92c1-2e78360e65a6", 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
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
        "device_ip": "10.161.0.34", 
        "if_name": "xe-0/0/4"
    }, 
    "resource_type": "ese_physical_ports"
}
```

- Response

```
{
    "resource_id": "6b29894f-8694-4865-92c1-2e78360e65a6", 
    "field_name": "port", 
    "created_at": "2018-04-04T04:54:45Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.161.0.34", 
        "if_name": "xe-0/0/4"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/02761d5d-f2ae-4806-bff6-df5851f514ed", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "port"
            }
        }
    }, 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "type": "snmp_ports_status", 
    "id": "02761d5d-f2ae-4806-bff6-df5851f514ed", 
    "resource_type": "ese_physical_ports"
}
```

### This is JSON data for checking "Ese Physical Port" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/02761d5d-f2ae-4806-bff6-df5851f514ed
```

- Response

```
{
    "resource_id": "6b29894f-8694-4865-92c1-2e78360e65a6", 
    "field_name": "port", 
    "created_at": "2018-04-04T04:54:45Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.161.0.34", 
        "if_name": "xe-0/0/4"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/02761d5d-f2ae-4806-bff6-df5851f514ed", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "port"
            }
        }
    }, 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "values": [], 
    "type": "snmp_ports_status", 
    "id": "02761d5d-f2ae-4806-bff6-df5851f514ed", 
    "resource_type": "ese_physical_ports"
}
```
and then ...
```
{
    "resource_id": "6b29894f-8694-4865-92c1-2e78360e65a6", 
    "field_name": "port", 
    "created_at": "2018-04-04T04:54:45Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.161.0.34", 
        "if_name": "xe-0/0/4"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/02761d5d-f2ae-4806-bff6-df5851f514ed", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "port"
            }
        }
    }, 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "values": [
        {
            "reporter": "SNMPPortPool", 
            "last_reported": "2018-04-04T04:55:39Z", 
            "last_changed": "2018-04-04T04:55:39Z", 
            "value": "UP", 
            "key": "status", 
            "fail_counter": 0
        }
    ], 
    "type": "snmp_ports_status", 
    "id": "02761d5d-f2ae-4806-bff6-df5851f514ed", 
    "resource_type": "ese_physical_ports"
}
```
