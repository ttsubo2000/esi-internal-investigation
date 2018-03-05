# Stored data in etcd: Create Loadbalancer

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/load_balancer_interfaces/63121c05-53c3-4cff-9c27-5d4055541a63
{
    "stack_id": "load_balancer_interface_63121c05-53c3-4cff-9c27-5d4055541a63", 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "130f173c-2799-4337-8ee5-d1a93a9882a9", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/130f173c-2799-4337-8ee5-d1a93a9882a9", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "load_balancer_interface:63121c05-53c3-4cff-9c27-5d4055541a63"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/load_balancer_interfaces/63121c05-53c3-4cff-9c27-5d4055541a63
{
    "heat_outputs": [
        {
            "output_value": "130f173c-2799-4337-8ee5-d1a93a9882a9", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/130f173c-2799-4337-8ee5-d1a93a9882a9", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/load_balancer_interfaces/63121c05-53c3-4cff-9c27-5d4055541a63
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"130f173c-2799-4337-8ee5-d1a93a9882a9\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se:7070/targets/130f173c-2799-4337-8ee5-d1a93a9882a9\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
