# Stored data in etcd: Update Loadbalancer Interface

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/load_balancers/b311c470-d878-4fea-8466-a4393938f2d4
{
    "stack_id": "load_balancer_b311c470-d878-4fea-8466-a4393938f2d4", 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "stack_status": "UPDATE_COMPLETE", 
    "output": [
        {
            "output_value": "668aabd6-71fe-4e0a-9842-421dce35d777", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/668aabd6-71fe-4e0a-9842-421dce35d777", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack successfully updated", 
    "id": "load_balancer:b311c470-d878-4fea-8466-a4393938f2d4"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/load_balancers/b311c470-d878-4fea-8466-a4393938f2d4
{
    "heat_outputs": [
        {
            "output_value": "668aabd6-71fe-4e0a-9842-421dce35d777", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/668aabd6-71fe-4e0a-9842-421dce35d777", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "UPDATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/load_balancers/b311c470-d878-4fea-8466-a4393938f2d4
{
    "state": {
        "worker_state": "MODIFY_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"668aabd6-71fe-4e0a-9842-421dce35d777\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se:7070/targets/668aabd6-71fe-4e0a-9842-421dce35d777\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "UPDATE_COMPLETE"
    }, 
    "version": 2, 
    "error": ""
}
```
