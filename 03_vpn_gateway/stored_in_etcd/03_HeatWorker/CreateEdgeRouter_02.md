# Stored data in etcd: Create Edge Router

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/edge_routers/b7e6d8ad-5377-4380-bbb4-1a62566cbd6d
{
    "stack_id": "edge_router_b7e6d8ad-5377-4380-bbb4-1a62566cbd6d", 
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "1e628441-c77a-4ebe-b5fe-6bd69816456d", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/1e628441-c77a-4ebe-b5fe-6bd69816456d", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "edge_router:b7e6d8ad-5377-4380-bbb4-1a62566cbd6d"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/edge_routers/b7e6d8ad-5377-4380-bbb4-1a62566cbd6d
{
    "heat_outputs": [
        {
            "output_value": "1e628441-c77a-4ebe-b5fe-6bd69816456d", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/1e628441-c77a-4ebe-b5fe-6bd69816456d", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/edge_routers/b7e6d8ad-5377-4380-bbb4-1a62566cbd6d
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"1e628441-c77a-4ebe-b5fe-6bd69816456d\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se.monitoringrefactordocker_default:7070/targets/1e628441-c77a-4ebe-b5fe-6bd69816456d\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
