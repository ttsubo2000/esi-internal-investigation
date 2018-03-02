# Stored data in etcd: Update Firewall Interface

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/firewalls/8e4c20be-d221-43f4-8325-0162c1f06166
{
    "stack_id": "firewall_8e4c20be-d221-43f4-8325-0162c1f06166", 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "stack_status": "UPDATE_COMPLETE", 
    "output": [
        {
            "output_value": "a5eddd6b-1de5-4199-8c1b-a4e9f3f4eab6", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/a5eddd6b-1de5-4199-8c1b-a4e9f3f4eab6", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack successfully updated", 
    "id": "firewall:8e4c20be-d221-43f4-8325-0162c1f06166"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/firewalls/8e4c20be-d221-43f4-8325-0162c1f06166
{
    "heat_outputs": [
        {
            "output_value": "a5eddd6b-1de5-4199-8c1b-a4e9f3f4eab6", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/a5eddd6b-1de5-4199-8c1b-a4e9f3f4eab6", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "UPDATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/firewalls/8e4c20be-d221-43f4-8325-0162c1f06166
{
    "state": {
        "worker_state": "MODIFY_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"a5eddd6b-1de5-4199-8c1b-a4e9f3f4eab6\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se:7070/targets/a5eddd6b-1de5-4199-8c1b-a4e9f3f4eab6\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "UPDATE_COMPLETE"
    }, 
    "version": 2, 
    "error": ""
}
```
