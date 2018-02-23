# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Firewall(vnf_instance)" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb", 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "version": 1, 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "server"
            }
        }
    }, 
    "field_name": "server", 
    "type": "compute", 
    "properties": {
        "server_id": "2e555b09-e0d7-4cce-8854-c481a2363917"
    }, 
    "resource_type": "vnf_instances"
}
```

- Response

```
{
    "resource_id": "44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb", 
    "field_name": "server", 
    "created_at": "2018-02-12T07:44:46Z", 
    "properties": {
        "server_id": "2e555b09-e0d7-4cce-8854-c481a2363917"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 1, 
    "link": "http://collector-agents-se:7070/targets/4d5db024-8232-458d-bd72-7256fbceb446", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "server"
            }
        }
    }, 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "type": "compute", 
    "id": "4d5db024-8232-458d-bd72-7256fbceb446", 
    "resource_type": "vnf_instances"
}
```

### This is JSON data for checking "Firewall(vnf_instance)" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/4d5db024-8232-458d-bd72-7256fbceb446
```

- Response

```
{
    "resource_id": "44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb", 
    "field_name": "server", 
    "created_at": "2018-02-12T07:44:46Z", 
    "properties": {
        "server_id": "2e555b09-e0d7-4cce-8854-c481a2363917"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 1, 
    "link": "http://collector-agents-se:7070/targets/4d5db024-8232-458d-bd72-7256fbceb446", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "server"
            }
        }
    }, 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "values": [], 
    "type": "compute", 
    "id": "4d5db024-8232-458d-bd72-7256fbceb446", 
    "resource_type": "vnf_instances"
}
```
and then ...
```
{
    "resource_id": "44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb", 
    "field_name": "server", 
    "created_at": "2018-02-12T07:44:46Z", 
    "properties": {
        "server_id": "2e555b09-e0d7-4cce-8854-c481a2363917"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 1, 
    "link": "http://collector-agents-se:7070/targets/4d5db024-8232-458d-bd72-7256fbceb446", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "server"
            }
        }
    }, 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "values": [
        {
            "reporter": "NovaAgent", 
            "last_reported": "2018-02-12T07:45:46Z", 
            "last_changed": "2018-02-12T07:45:46Z", 
            "value": "UP", 
            "key": "status", 
            "fail_counter": 0
        }
    ], 
    "type": "compute", 
    "id": "4d5db024-8232-458d-bd72-7256fbceb446", 
    "resource_type": "vnf_instances"
}
```
