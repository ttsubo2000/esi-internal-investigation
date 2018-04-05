# Stored data in etcd: Create Subnet

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/subnets/67877f2d-0547-4cea-a6ce-2e3b937aa31b
{
    "stack_id": "subnet_67877f2d-0547-4cea-a6ce-2e3b937aa31b", 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "172.16.101.0/24", 
            "description": "IP prefix of local subnet.", 
            "output_key": "ip_prefix"
        }, 
        {
            "output_value": "67877f2d-0547-4cea-a6ce-2e3b937aa31b", 
            "description": "The name of the local subnet.", 
            "output_key": "name"
        }, 
        {
            "output_value": "172.16.101.1", 
            "description": "Default gateway of local subnet.", 
            "output_key": "default_gateway"
        }, 
        {
            "output_value": "6e557507-1c2a-49b1-ba90-5f616a1f1f3e", 
            "description": "A unique id for the network.", 
            "output_key": "network_id"
        }, 
        {
            "output_value": "5a79909b-2bf3-4e26-8a9c-0bf6bb175457", 
            "description": "IPAM this local subnet uses.", 
            "output_key": "ipam"
        }, 
        {
            "output_value": "4cc11376-ba13-4cc8-b7a6-f886f4a031d1", 
            "description": "A unique id for the local subnet.", 
            "output_key": "id"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "subnet:67877f2d-0547-4cea-a6ce-2e3b937aa31b"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/subnets/67877f2d-0547-4cea-a6ce-2e3b937aa31b
{
    "heat_outputs": [
        {
            "output_value": "172.16.101.0/24", 
            "description": "IP prefix of local subnet.", 
            "output_key": "ip_prefix"
        }, 
        {
            "output_value": "67877f2d-0547-4cea-a6ce-2e3b937aa31b", 
            "description": "The name of the local subnet.", 
            "output_key": "name"
        }, 
        {
            "output_value": "172.16.101.1", 
            "description": "Default gateway of local subnet.", 
            "output_key": "default_gateway"
        }, 
        {
            "output_value": "6e557507-1c2a-49b1-ba90-5f616a1f1f3e", 
            "description": "A unique id for the network.", 
            "output_key": "network_id"
        }, 
        {
            "output_value": "5a79909b-2bf3-4e26-8a9c-0bf6bb175457", 
            "description": "IPAM this local subnet uses.", 
            "output_key": "ipam"
        }, 
        {
            "output_value": "4cc11376-ba13-4cc8-b7a6-f886f4a031d1", 
            "description": "A unique id for the local subnet.", 
            "output_key": "id"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/subnets/67877f2d-0547-4cea-a6ce-2e3b937aa31b
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"172.16.101.0/24\", \"description\": \"IP prefix of local subnet.\", \"output_key\": \"ip_prefix\"}, {\"output_value\": \"67877f2d-0547-4cea-a6ce-2e3b937aa31b\", \"description\": \"The name of the local subnet.\", \"output_key\": \"name\"}, {\"output_value\": \"172.16.101.1\", \"description\": \"Default gateway of local subnet.\", \"output_key\": \"default_gateway\"}, {\"output_value\": \"6e557507-1c2a-49b1-ba90-5f616a1f1f3e\", \"description\": \"A unique id for the network.\", \"output_key\": \"network_id\"}, {\"output_value\": \"5a79909b-2bf3-4e26-8a9c-0bf6bb175457\", \"description\": \"IPAM this local subnet uses.\", \"output_key\": \"ipam\"}, {\"output_value\": \"4cc11376-ba13-4cc8-b7a6-f886f4a031d1\", \"description\": \"A unique id for the local subnet.\", \"output_key\": \"id\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
