# Stored data in etcd: Create Physical Port

No stored data for "heat_templates" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/physical_ports/7ff183de-0188-46bf-b7d0-68d08ad2b54f
{
    "body": {
        "status": "PENDING_CREATE", 
        "description": "", 
        "tags": {}, 
        "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
        "service_owner": "server", 
        "plane": "data", 
        "segmentation_ranges": [
            {
                "start": 3, 
                "end": 4093
            }
        ], 
        "service_id": "server", 
        "id": "7ff183de-0188-46bf-b7d0-68d08ad2b54f", 
        "name": "qfx-nw01-xe001"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/physical_ports/7ff183de-0188-46bf-b7d0-68d08ad2b54f
{
    "state": {
        "worker_state": "READ_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
