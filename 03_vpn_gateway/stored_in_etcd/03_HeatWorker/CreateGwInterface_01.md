# Stored data in etcd: Create Gw Interface

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/gw_interfaces/3dbcfce5-bca5-4182-991a-c23de685fcf1
{
    "stack_id": "gw_interface_3dbcfce5-bca5-4182-991a-c23de685fcf1", 
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "8ac03032-a027-4965-b636-32a7b1281bfc", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/8ac03032-a027-4965-b636-32a7b1281bfc", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "gw_interface:3dbcfce5-bca5-4182-991a-c23de685fcf1"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/gw_interfaces/3dbcfce5-bca5-4182-991a-c23de685fcf1
{
    "heat_outputs": [
        {
            "output_value": "8ac03032-a027-4965-b636-32a7b1281bfc", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/8ac03032-a027-4965-b636-32a7b1281bfc", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/gw_interfaces/3dbcfce5-bca5-4182-991a-c23de685fcf1
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"8ac03032-a027-4965-b636-32a7b1281bfc\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se.monitoringrefactordocker_default:7070/targets/8ac03032-a027-4965-b636-32a7b1281bfc\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
