# Stored data in etcd: Create Edge Router

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/edge_routers/7a35974a-a19f-49e2-b907-ad7fd8692975
{
    "stack_id": "edge_router_7a35974a-a19f-49e2-b907-ad7fd8692975", 
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "cc896303-29e2-47d6-a409-a84c23b5722b", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/cc896303-29e2-47d6-a409-a84c23b5722b", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "edge_router:7a35974a-a19f-49e2-b907-ad7fd8692975"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/edge_routers/7a35974a-a19f-49e2-b907-ad7fd8692975
{
    "heat_outputs": [
        {
            "output_value": "cc896303-29e2-47d6-a409-a84c23b5722b", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/cc896303-29e2-47d6-a409-a84c23b5722b", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/edge_routers/7a35974a-a19f-49e2-b907-ad7fd8692975
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"cc896303-29e2-47d6-a409-a84c23b5722b\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se.monitoringrefactordocker_default:7070/targets/cc896303-29e2-47d6-a409-a84c23b5722b\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
