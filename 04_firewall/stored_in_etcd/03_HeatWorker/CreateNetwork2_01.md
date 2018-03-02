# Stored data in etcd: Create Network (admin-net)

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/networks/75c2c3ec-7fe7-494c-a35c-db3f94d3a554
{
    "stack_id": "network_75c2c3ec-7fe7-494c-a35c-db3f94d3a554", 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": [], 
            "description": "The name of the virtual network.", 
            "output_key": "route_targets"
        }, 
        {
            "output_value": "default-domain:usertenant:75c2c3ec-7fe7-494c-a35c-db3f94d3a554", 
            "description": "The FQ name of the virtual network.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "75c2c3ec-7fe7-494c-a35c-db3f94d3a554", 
            "description": "A unique id for the virtual network.", 
            "output_key": "id"
        }, 
        {
            "output_value": "75c2c3ec-7fe7-494c-a35c-db3f94d3a554", 
            "description": "The name of the virtual network.", 
            "output_key": "name"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "network:75c2c3ec-7fe7-494c-a35c-db3f94d3a554"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/networks/75c2c3ec-7fe7-494c-a35c-db3f94d3a554
{
    "heat_outputs": [
        {
            "output_value": [], 
            "description": "The name of the virtual network.", 
            "output_key": "route_targets"
        }, 
        {
            "output_value": "default-domain:usertenant:75c2c3ec-7fe7-494c-a35c-db3f94d3a554", 
            "description": "The FQ name of the virtual network.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "75c2c3ec-7fe7-494c-a35c-db3f94d3a554", 
            "description": "A unique id for the virtual network.", 
            "output_key": "id"
        }, 
        {
            "output_value": "75c2c3ec-7fe7-494c-a35c-db3f94d3a554", 
            "description": "The name of the virtual network.", 
            "output_key": "name"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/networks/75c2c3ec-7fe7-494c-a35c-db3f94d3a554
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": [], \"description\": \"The name of the virtual network.\", \"output_key\": \"route_targets\"}, {\"output_value\": \"default-domain:usertenant:75c2c3ec-7fe7-494c-a35c-db3f94d3a554\", \"description\": \"The FQ name of the virtual network.\", \"output_key\": \"fq_name\"}, {\"output_value\": \"75c2c3ec-7fe7-494c-a35c-db3f94d3a554\", \"description\": \"A unique id for the virtual network.\", \"output_key\": \"id\"}, {\"output_value\": \"75c2c3ec-7fe7-494c-a35c-db3f94d3a554\", \"description\": \"The name of the virtual network.\", \"output_key\": \"name\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
