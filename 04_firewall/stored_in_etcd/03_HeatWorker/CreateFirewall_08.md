# Stored data in etcd: Create Firewall

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/firewalls/8e4c20be-d221-43f4-8325-0162c1f06166
{
    "stack_id": "firewall_8e4c20be-d221-43f4-8325-0162c1f06166", 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "346eb30d-1ae0-4375-a1d6-7d83c699e2d3", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/346eb30d-1ae0-4375-a1d6-7d83c699e2d3", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "firewall:8e4c20be-d221-43f4-8325-0162c1f06166"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/firewalls/8e4c20be-d221-43f4-8325-0162c1f06166
{
    "heat_outputs": [
        {
            "output_value": "346eb30d-1ae0-4375-a1d6-7d83c699e2d3", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/346eb30d-1ae0-4375-a1d6-7d83c699e2d3", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/firewalls/8e4c20be-d221-43f4-8325-0162c1f06166
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"346eb30d-1ae0-4375-a1d6-7d83c699e2d3\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se:7070/targets/346eb30d-1ae0-4375-a1d6-7d83c699e2d3\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
