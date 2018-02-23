# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Loadbalancer(vnf_instance)" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "398d65ba-0060-456e-b415-5bc954450717", 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
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
        "server_id": "47531b14-72e9-439d-8949-fd941457ecde"
    }, 
    "resource_type": "vnf_instances"
}
```

- Response

```
{
    "resource_id": "398d65ba-0060-456e-b415-5bc954450717", 
    "field_name": "server", 
    "created_at": "2018-02-19T05:21:54Z", 
    "properties": {
        "server_id": "47531b14-72e9-439d-8949-fd941457ecde"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 1, 
    "link": "http://collector-agents-se:7070/targets/8bc1f992-4810-4d3c-af4f-26d93419fb2b", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "server"
            }
        }
    }, 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "type": "compute", 
    "id": "8bc1f992-4810-4d3c-af4f-26d93419fb2b", 
    "resource_type": "vnf_instances"
}
```

### This is JSON data for checking "Loadbalancer(vnf_instance)" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/8bc1f992-4810-4d3c-af4f-26d93419fb2b
```

- Response

```
{
    "resource_id": "398d65ba-0060-456e-b415-5bc954450717", 
    "field_name": "server", 
    "created_at": "2018-02-19T05:21:54Z", 
    "properties": {
        "server_id": "47531b14-72e9-439d-8949-fd941457ecde"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 1, 
    "link": "http://collector-agents-se:7070/targets/8bc1f992-4810-4d3c-af4f-26d93419fb2b", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "server"
            }
        }
    }, 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "values": [], 
    "type": "compute", 
    "id": "8bc1f992-4810-4d3c-af4f-26d93419fb2b", 
    "resource_type": "vnf_instances"
}
```
and then ...
```
{
    "resource_id": "398d65ba-0060-456e-b415-5bc954450717", 
    "field_name": "server", 
    "created_at": "2018-02-19T05:21:54Z", 
    "properties": {
        "server_id": "47531b14-72e9-439d-8949-fd941457ecde"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 1, 
    "link": "http://collector-agents-se:7070/targets/8bc1f992-4810-4d3c-af4f-26d93419fb2b", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "server"
            }
        }
    }, 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "values": [
        {
            "reporter": "NovaAgent", 
            "last_reported": "2018-02-19T05:22:54Z", 
            "last_changed": "2018-02-19T05:22:54Z", 
            "value": "UP", 
            "key": "status", 
            "fail_counter": 0
        }
    ], 
    "type": "compute", 
    "id": "8bc1f992-4810-4d3c-af4f-26d93419fb2b", 
    "resource_type": "vnf_instances"
}
```
