# Stored data in etcd: Create Loadbalancer

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/load_balancer_interfaces/7f2bef0a-26f3-4ec9-89de-1aee7f04f998
{
    "stack_id": "load_balancer_interface_7f2bef0a-26f3-4ec9-89de-1aee7f04f998", 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "c2ad3511-dcc2-4e31-9702-a2e01ea39b27", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/c2ad3511-dcc2-4e31-9702-a2e01ea39b27", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "load_balancer_interface:7f2bef0a-26f3-4ec9-89de-1aee7f04f998"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/load_balancer_interfaces/7f2bef0a-26f3-4ec9-89de-1aee7f04f998
{
    "heat_outputs": [
        {
            "output_value": "c2ad3511-dcc2-4e31-9702-a2e01ea39b27", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/c2ad3511-dcc2-4e31-9702-a2e01ea39b27", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/load_balancer_interfaces/7f2bef0a-26f3-4ec9-89de-1aee7f04f998
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"c2ad3511-dcc2-4e31-9702-a2e01ea39b27\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se:7070/targets/c2ad3511-dcc2-4e31-9702-a2e01ea39b27\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
