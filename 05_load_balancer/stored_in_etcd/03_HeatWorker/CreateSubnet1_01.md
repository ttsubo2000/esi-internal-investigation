# Stored data in etcd: Create Subnet (dummy-net)

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/subnets/6f5f33d6-2cfe-47c1-a91a-3f3d44972b1a
{
    "stack_id": "subnet_6f5f33d6-2cfe-47c1-a91a-3f3d44972b1a", 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "10.121.232.0/24", 
            "description": "IP prefix of local subnet.", 
            "output_key": "ip_prefix"
        }, 
        {
            "output_value": "6f5f33d6-2cfe-47c1-a91a-3f3d44972b1a", 
            "description": "The name of the local subnet.", 
            "output_key": "name"
        }, 
        {
            "output_value": "10.121.232.1", 
            "description": "Default gateway of local subnet.", 
            "output_key": "default_gateway"
        }, 
        {
            "output_value": "ce9a7a92-d11a-4fc6-8ae7-18061b62c98f", 
            "description": "A unique id for the network.", 
            "output_key": "network_id"
        }, 
        {
            "output_value": "5a79909b-2bf3-4e26-8a9c-0bf6bb175457", 
            "description": "IPAM this local subnet uses.", 
            "output_key": "ipam"
        }, 
        {
            "output_value": "5093b556-c4f3-465c-82b6-ac65c40a95f2", 
            "description": "A unique id for the local subnet.", 
            "output_key": "id"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "subnet:6f5f33d6-2cfe-47c1-a91a-3f3d44972b1a"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/subnets/6f5f33d6-2cfe-47c1-a91a-3f3d44972b1a
{
    "heat_outputs": [
        {
            "output_value": "10.121.232.0/24", 
            "description": "IP prefix of local subnet.", 
            "output_key": "ip_prefix"
        }, 
        {
            "output_value": "6f5f33d6-2cfe-47c1-a91a-3f3d44972b1a", 
            "description": "The name of the local subnet.", 
            "output_key": "name"
        }, 
        {
            "output_value": "10.121.232.1", 
            "description": "Default gateway of local subnet.", 
            "output_key": "default_gateway"
        }, 
        {
            "output_value": "ce9a7a92-d11a-4fc6-8ae7-18061b62c98f", 
            "description": "A unique id for the network.", 
            "output_key": "network_id"
        }, 
        {
            "output_value": "5a79909b-2bf3-4e26-8a9c-0bf6bb175457", 
            "description": "IPAM this local subnet uses.", 
            "output_key": "ipam"
        }, 
        {
            "output_value": "5093b556-c4f3-465c-82b6-ac65c40a95f2", 
            "description": "A unique id for the local subnet.", 
            "output_key": "id"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/subnets/6f5f33d6-2cfe-47c1-a91a-3f3d44972b1a
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"10.121.232.0/24\", \"description\": \"IP prefix of local subnet.\", \"output_key\": \"ip_prefix\"}, {\"output_value\": \"6f5f33d6-2cfe-47c1-a91a-3f3d44972b1a\", \"description\": \"The name of the local subnet.\", \"output_key\": \"name\"}, {\"output_value\": \"10.121.232.1\", \"description\": \"Default gateway of local subnet.\", \"output_key\": \"default_gateway\"}, {\"output_value\": \"ce9a7a92-d11a-4fc6-8ae7-18061b62c98f\", \"description\": \"A unique id for the network.\", \"output_key\": \"network_id\"}, {\"output_value\": \"5a79909b-2bf3-4e26-8a9c-0bf6bb175457\", \"description\": \"IPAM this local subnet uses.\", \"output_key\": \"ipam\"}, {\"output_value\": \"5093b556-c4f3-465c-82b6-ac65c40a95f2\", \"description\": \"A unique id for the local subnet.\", \"output_key\": \"id\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
