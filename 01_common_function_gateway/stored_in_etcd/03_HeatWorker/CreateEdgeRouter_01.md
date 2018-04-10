# Stored data in etcd: Create Edge Router

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/edge_routers/f4f54175-93fe-406b-ae66-dbca4df99e03
{
    "stack_id": "edge_router_f4f54175-93fe-406b-ae66-dbca4df99e03", 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "b88cbb53-f850-44f2-9960-95ade457e46c", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/b88cbb53-f850-44f2-9960-95ade457e46c", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "edge_router:f4f54175-93fe-406b-ae66-dbca4df99e03"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/edge_routers/f4f54175-93fe-406b-ae66-dbca4df99e03
{
    "heat_outputs": [
        {
            "output_value": "b88cbb53-f850-44f2-9960-95ade457e46c", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/b88cbb53-f850-44f2-9960-95ade457e46c", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/edge_routers/f4f54175-93fe-406b-ae66-dbca4df99e03
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"b88cbb53-f850-44f2-9960-95ade457e46c\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se.monitoringrefactordocker_default:7070/targets/b88cbb53-f850-44f2-9960-95ade457e46c\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
