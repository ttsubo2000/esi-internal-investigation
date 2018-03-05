# Stored data in etcd: Create Subnet (admin-net)

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/subnets/707847d0-89d9-4b98-93a2-8b376709c5f3
{
    "stack_id": "subnet_707847d0-89d9-4b98-93a2-8b376709c5f3", 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "100.64.193.0/24", 
            "description": "IP prefix of local subnet.", 
            "output_key": "ip_prefix"
        }, 
        {
            "output_value": "707847d0-89d9-4b98-93a2-8b376709c5f3", 
            "description": "The name of the local subnet.", 
            "output_key": "name"
        }, 
        {
            "output_value": "100.64.193.1", 
            "description": "Default gateway of local subnet.", 
            "output_key": "default_gateway"
        }, 
        {
            "output_value": "168c1535-9001-49c7-bb05-21844570a83c", 
            "description": "A unique id for the network.", 
            "output_key": "network_id"
        }, 
        {
            "output_value": "5a79909b-2bf3-4e26-8a9c-0bf6bb175457", 
            "description": "IPAM this local subnet uses.", 
            "output_key": "ipam"
        }, 
        {
            "output_value": "a2fc1444-c7f4-4a72-8376-a920889c4a43", 
            "description": "A unique id for the local subnet.", 
            "output_key": "id"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "subnet:707847d0-89d9-4b98-93a2-8b376709c5f3"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/subnets/707847d0-89d9-4b98-93a2-8b376709c5f3
{
    "heat_outputs": [
        {
            "output_value": "100.64.193.0/24", 
            "description": "IP prefix of local subnet.", 
            "output_key": "ip_prefix"
        }, 
        {
            "output_value": "707847d0-89d9-4b98-93a2-8b376709c5f3", 
            "description": "The name of the local subnet.", 
            "output_key": "name"
        }, 
        {
            "output_value": "100.64.193.1", 
            "description": "Default gateway of local subnet.", 
            "output_key": "default_gateway"
        }, 
        {
            "output_value": "168c1535-9001-49c7-bb05-21844570a83c", 
            "description": "A unique id for the network.", 
            "output_key": "network_id"
        }, 
        {
            "output_value": "5a79909b-2bf3-4e26-8a9c-0bf6bb175457", 
            "description": "IPAM this local subnet uses.", 
            "output_key": "ipam"
        }, 
        {
            "output_value": "a2fc1444-c7f4-4a72-8376-a920889c4a43", 
            "description": "A unique id for the local subnet.", 
            "output_key": "id"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/subnets/707847d0-89d9-4b98-93a2-8b376709c5f3
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"100.64.193.0/24\", \"description\": \"IP prefix of local subnet.\", \"output_key\": \"ip_prefix\"}, {\"output_value\": \"707847d0-89d9-4b98-93a2-8b376709c5f3\", \"description\": \"The name of the local subnet.\", \"output_key\": \"name\"}, {\"output_value\": \"100.64.193.1\", \"description\": \"Default gateway of local subnet.\", \"output_key\": \"default_gateway\"}, {\"output_value\": \"168c1535-9001-49c7-bb05-21844570a83c\", \"description\": \"A unique id for the network.\", \"output_key\": \"network_id\"}, {\"output_value\": \"5a79909b-2bf3-4e26-8a9c-0bf6bb175457\", \"description\": \"IPAM this local subnet uses.\", \"output_key\": \"ipam\"}, {\"output_value\": \"a2fc1444-c7f4-4a72-8376-a920889c4a43\", \"description\": \"A unique id for the local subnet.\", \"output_key\": \"id\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
