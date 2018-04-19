# Stored data in etcd: Create Subnet

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/subnets/e825f4e4-ba44-4d9e-9578-a31ad45bedda
{
    "stack_id": "subnet_e825f4e4-ba44-4d9e-9578-a31ad45bedda", 
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "172.16.101.0/24", 
            "description": "IP prefix of local subnet.", 
            "output_key": "ip_prefix"
        }, 
        {
            "output_value": "e825f4e4-ba44-4d9e-9578-a31ad45bedda", 
            "description": "The name of the local subnet.", 
            "output_key": "name"
        }, 
        {
            "output_value": "172.16.101.1", 
            "description": "Default gateway of local subnet.", 
            "output_key": "default_gateway"
        }, 
        {
            "output_value": "afa0d9d6-84dc-4755-9c6e-db2f23f9dde2", 
            "description": "A unique id for the network.", 
            "output_key": "network_id"
        }, 
        {
            "output_value": "5a79909b-2bf3-4e26-8a9c-0bf6bb175457", 
            "description": "IPAM this local subnet uses.", 
            "output_key": "ipam"
        }, 
        {
            "output_value": "323017d2-b9fc-4407-b998-e4776b16aee8", 
            "description": "A unique id for the local subnet.", 
            "output_key": "id"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "subnet:e825f4e4-ba44-4d9e-9578-a31ad45bedda"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/subnets/e825f4e4-ba44-4d9e-9578-a31ad45bedda
{
    "heat_outputs": [
        {
            "output_value": "172.16.101.0/24", 
            "description": "IP prefix of local subnet.", 
            "output_key": "ip_prefix"
        }, 
        {
            "output_value": "e825f4e4-ba44-4d9e-9578-a31ad45bedda", 
            "description": "The name of the local subnet.", 
            "output_key": "name"
        }, 
        {
            "output_value": "172.16.101.1", 
            "description": "Default gateway of local subnet.", 
            "output_key": "default_gateway"
        }, 
        {
            "output_value": "afa0d9d6-84dc-4755-9c6e-db2f23f9dde2", 
            "description": "A unique id for the network.", 
            "output_key": "network_id"
        }, 
        {
            "output_value": "5a79909b-2bf3-4e26-8a9c-0bf6bb175457", 
            "description": "IPAM this local subnet uses.", 
            "output_key": "ipam"
        }, 
        {
            "output_value": "323017d2-b9fc-4407-b998-e4776b16aee8", 
            "description": "A unique id for the local subnet.", 
            "output_key": "id"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/subnets/e825f4e4-ba44-4d9e-9578-a31ad45bedda
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"172.16.101.0/24\", \"description\": \"IP prefix of local subnet.\", \"output_key\": \"ip_prefix\"}, {\"output_value\": \"e825f4e4-ba44-4d9e-9578-a31ad45bedda\", \"description\": \"The name of the local subnet.\", \"output_key\": \"name\"}, {\"output_value\": \"172.16.101.1\", \"description\": \"Default gateway of local subnet.\", \"output_key\": \"default_gateway\"}, {\"output_value\": \"afa0d9d6-84dc-4755-9c6e-db2f23f9dde2\", \"description\": \"A unique id for the network.\", \"output_key\": \"network_id\"}, {\"output_value\": \"5a79909b-2bf3-4e26-8a9c-0bf6bb175457\", \"description\": \"IPAM this local subnet uses.\", \"output_key\": \"ipam\"}, {\"output_value\": \"323017d2-b9fc-4407-b998-e4776b16aee8\", \"description\": \"A unique id for the local subnet.\", \"output_key\": \"id\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
