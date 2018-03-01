# Stored data in etcd: Create Subnet

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/subnets/3cfa93ac-251a-4a60-9434-ff4c88bf3655
{
    "stack_id": "subnet_3cfa93ac-251a-4a60-9434-ff4c88bf3655", 
    "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "192.168.200.0/24", 
            "description": "IP prefix of local subnet.", 
            "output_key": "ip_prefix"
        }, 
        {
            "output_value": "3cfa93ac-251a-4a60-9434-ff4c88bf3655", 
            "description": "The name of the local subnet.", 
            "output_key": "name"
        }, 
        {
            "output_value": "192.168.200.1", 
            "description": "Default gateway of local subnet.", 
            "output_key": "default_gateway"
        }, 
        {
            "output_value": "35bc496f-3c0e-46b4-a5c0-33810e8e7263", 
            "description": "A unique id for the network.", 
            "output_key": "network_id"
        }, 
        {
            "output_value": "5a79909b-2bf3-4e26-8a9c-0bf6bb175457", 
            "description": "IPAM this local subnet uses.", 
            "output_key": "ipam"
        }, 
        {
            "output_value": "15711909-5d0a-46c8-83f5-c739380ebbb9", 
            "description": "A unique id for the local subnet.", 
            "output_key": "id"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "subnet:3cfa93ac-251a-4a60-9434-ff4c88bf3655"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/subnets/3cfa93ac-251a-4a60-9434-ff4c88bf3655
{
    "heat_outputs": [
        {
            "output_value": "192.168.200.0/24", 
            "description": "IP prefix of local subnet.", 
            "output_key": "ip_prefix"
        }, 
        {
            "output_value": "3cfa93ac-251a-4a60-9434-ff4c88bf3655", 
            "description": "The name of the local subnet.", 
            "output_key": "name"
        }, 
        {
            "output_value": "192.168.200.1", 
            "description": "Default gateway of local subnet.", 
            "output_key": "default_gateway"
        }, 
        {
            "output_value": "35bc496f-3c0e-46b4-a5c0-33810e8e7263", 
            "description": "A unique id for the network.", 
            "output_key": "network_id"
        }, 
        {
            "output_value": "5a79909b-2bf3-4e26-8a9c-0bf6bb175457", 
            "description": "IPAM this local subnet uses.", 
            "output_key": "ipam"
        }, 
        {
            "output_value": "15711909-5d0a-46c8-83f5-c739380ebbb9", 
            "description": "A unique id for the local subnet.", 
            "output_key": "id"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/subnets/3cfa93ac-251a-4a60-9434-ff4c88bf3655
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"192.168.200.0/24\", \"description\": \"IP prefix of local subnet.\", \"output_key\": \"ip_prefix\"}, {\"output_value\": \"3cfa93ac-251a-4a60-9434-ff4c88bf3655\", \"description\": \"The name of the local subnet.\", \"output_key\": \"name\"}, {\"output_value\": \"192.168.200.1\", \"description\": \"Default gateway of local subnet.\", \"output_key\": \"default_gateway\"}, {\"output_value\": \"35bc496f-3c0e-46b4-a5c0-33810e8e7263\", \"description\": \"A unique id for the network.\", \"output_key\": \"network_id\"}, {\"output_value\": \"5a79909b-2bf3-4e26-8a9c-0bf6bb175457\", \"description\": \"IPAM this local subnet uses.\", \"output_key\": \"ipam\"}, {\"output_value\": \"15711909-5d0a-46c8-83f5-c739380ebbb9\", \"description\": \"A unique id for the local subnet.\", \"output_key\": \"id\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
