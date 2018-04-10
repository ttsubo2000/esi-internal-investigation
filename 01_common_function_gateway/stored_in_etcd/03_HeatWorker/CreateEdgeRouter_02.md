# Stored data in etcd: Create Edge Router

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/edge_routers/2d056865-47a9-45cf-a890-ed10e3b5912a
{
    "stack_id": "edge_router_2d056865-47a9-45cf-a890-ed10e3b5912a", 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "ad464fbb-0810-447e-b10d-31715221cb95", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/ad464fbb-0810-447e-b10d-31715221cb95", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "edge_router:2d056865-47a9-45cf-a890-ed10e3b5912a"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/edge_routers/2d056865-47a9-45cf-a890-ed10e3b5912a
{
    "heat_outputs": [
        {
            "output_value": "ad464fbb-0810-447e-b10d-31715221cb95", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/ad464fbb-0810-447e-b10d-31715221cb95", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/edge_routers/2d056865-47a9-45cf-a890-ed10e3b5912a
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"ad464fbb-0810-447e-b10d-31715221cb95\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se.monitoringrefactordocker_default:7070/targets/ad464fbb-0810-447e-b10d-31715221cb95\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
