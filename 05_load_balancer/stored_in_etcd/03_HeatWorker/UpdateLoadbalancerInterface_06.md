# Stored data in etcd: Update Loadbalancer Interface

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/load_balancer_interfaces/24580bfc-32f4-4c0f-8e8a-c7288497aa7c
{
    "stack_id": "load_balancer_interface_24580bfc-32f4-4c0f-8e8a-c7288497aa7c", 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "stack_status": "UPDATE_COMPLETE", 
    "output": [
        {
            "output_value": "9fc3003a-56fd-4a6c-9cac-0c1ab74f11c8", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/9fc3003a-56fd-4a6c-9cac-0c1ab74f11c8", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack successfully updated", 
    "id": "load_balancer_interface:24580bfc-32f4-4c0f-8e8a-c7288497aa7c"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/load_balancer_interfaces/24580bfc-32f4-4c0f-8e8a-c7288497aa7c
{
    "heat_outputs": [
        {
            "output_value": "9fc3003a-56fd-4a6c-9cac-0c1ab74f11c8", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/9fc3003a-56fd-4a6c-9cac-0c1ab74f11c8", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "UPDATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/load_balancer_interfaces/24580bfc-32f4-4c0f-8e8a-c7288497aa7c
{
    "state": {
        "worker_state": "MODIFY_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"9fc3003a-56fd-4a6c-9cac-0c1ab74f11c8\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se:7070/targets/9fc3003a-56fd-4a6c-9cac-0c1ab74f11c8\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "UPDATE_COMPLETE"
    }, 
    "version": 2, 
    "error": ""
}
```
