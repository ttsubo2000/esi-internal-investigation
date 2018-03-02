# Stored data in etcd: Create Firewall

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/firewall_interfaces/cdf30a48-8cf7-4935-9f8a-5b51f1177704
{
    "stack_id": "firewall_interface_cdf30a48-8cf7-4935-9f8a-5b51f1177704", 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "9d7a43c7-40e2-4703-9205-d76939462572", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/9d7a43c7-40e2-4703-9205-d76939462572", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "firewall_interface:cdf30a48-8cf7-4935-9f8a-5b51f1177704"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/firewall_interfaces/cdf30a48-8cf7-4935-9f8a-5b51f1177704
{
    "heat_outputs": [
        {
            "output_value": "9d7a43c7-40e2-4703-9205-d76939462572", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/9d7a43c7-40e2-4703-9205-d76939462572", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd
```
/state/v2.0/firewall_interfaces/cdf30a48-8cf7-4935-9f8a-5b51f1177704
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"9d7a43c7-40e2-4703-9205-d76939462572\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se:7070/targets/9d7a43c7-40e2-4703-9205-d76939462572\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
