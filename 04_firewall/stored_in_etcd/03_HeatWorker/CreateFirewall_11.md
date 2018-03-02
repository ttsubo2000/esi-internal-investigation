# Stored data in etcd: Create Firewall

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/firewall_interfaces/1c351257-d185-40b7-b04a-6272de75d434
{
    "stack_id": "firewall_interface_1c351257-d185-40b7-b04a-6272de75d434", 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "ecbc7461-e883-4c21-bcf6-b91a105a533c", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/ecbc7461-e883-4c21-bcf6-b91a105a533c", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "firewall_interface:1c351257-d185-40b7-b04a-6272de75d434"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/firewall_interfaces/1c351257-d185-40b7-b04a-6272de75d434
{
    "heat_outputs": [
        {
            "output_value": "ecbc7461-e883-4c21-bcf6-b91a105a533c", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/ecbc7461-e883-4c21-bcf6-b91a105a533c", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd
```
/state/v2.0/firewall_interfaces/1c351257-d185-40b7-b04a-6272de75d434
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"ecbc7461-e883-4c21-bcf6-b91a105a533c\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se:7070/targets/ecbc7461-e883-4c21-bcf6-b91a105a533c\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
