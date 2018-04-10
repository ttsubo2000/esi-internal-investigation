# Stored data in etcd: Create Common Function Gateway

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/subnets/cf9356ae-b4e1-4a91-8193-089fdc12173d
{
    "stack_id": "subnet_cf9356ae-b4e1-4a91-8193-089fdc12173d", 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "169.254.0.0/17", 
            "description": "IP prefix of local subnet.", 
            "output_key": "ip_prefix"
        }, 
        {
            "output_value": "cf9356ae-b4e1-4a91-8193-089fdc12173d", 
            "description": "The name of the local subnet.", 
            "output_key": "name"
        }, 
        {
            "output_value": "0.0.0.0", 
            "description": "Default gateway of local subnet.", 
            "output_key": "default_gateway"
        }, 
        {
            "output_value": "fc8814a7-eb1e-4f59-8422-7de500e72782", 
            "description": "A unique id for the network.", 
            "output_key": "network_id"
        }, 
        {
            "output_value": "5a79909b-2bf3-4e26-8a9c-0bf6bb175457", 
            "description": "IPAM this local subnet uses.", 
            "output_key": "ipam"
        }, 
        {
            "output_value": "8f52422a-7115-4304-99cf-fc021562c352", 
            "description": "A unique id for the local subnet.", 
            "output_key": "id"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "subnet:cf9356ae-b4e1-4a91-8193-089fdc12173d"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/subnets/cf9356ae-b4e1-4a91-8193-089fdc12173d
{
    "heat_outputs": [
        {
            "output_value": "169.254.0.0/17", 
            "description": "IP prefix of local subnet.", 
            "output_key": "ip_prefix"
        }, 
        {
            "output_value": "cf9356ae-b4e1-4a91-8193-089fdc12173d", 
            "description": "The name of the local subnet.", 
            "output_key": "name"
        }, 
        {
            "output_value": "0.0.0.0", 
            "description": "Default gateway of local subnet.", 
            "output_key": "default_gateway"
        }, 
        {
            "output_value": "fc8814a7-eb1e-4f59-8422-7de500e72782", 
            "description": "A unique id for the network.", 
            "output_key": "network_id"
        }, 
        {
            "output_value": "5a79909b-2bf3-4e26-8a9c-0bf6bb175457", 
            "description": "IPAM this local subnet uses.", 
            "output_key": "ipam"
        }, 
        {
            "output_value": "8f52422a-7115-4304-99cf-fc021562c352", 
            "description": "A unique id for the local subnet.", 
            "output_key": "id"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/subnets/cf9356ae-b4e1-4a91-8193-089fdc12173d
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"169.254.0.0/17\", \"description\": \"IP prefix of local subnet.\", \"output_key\": \"ip_prefix\"}, {\"output_value\": \"cf9356ae-b4e1-4a91-8193-089fdc12173d\", \"description\": \"The name of the local subnet.\", \"output_key\": \"name\"}, {\"output_value\": \"0.0.0.0\", \"description\": \"Default gateway of local subnet.\", \"output_key\": \"default_gateway\"}, {\"output_value\": \"fc8814a7-eb1e-4f59-8422-7de500e72782\", \"description\": \"A unique id for the network.\", \"output_key\": \"network_id\"}, {\"output_value\": \"5a79909b-2bf3-4e26-8a9c-0bf6bb175457\", \"description\": \"IPAM this local subnet uses.\", \"output_key\": \"ipam\"}, {\"output_value\": \"8f52422a-7115-4304-99cf-fc021562c352\", \"description\": \"A unique id for the local subnet.\", \"output_key\": \"id\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
