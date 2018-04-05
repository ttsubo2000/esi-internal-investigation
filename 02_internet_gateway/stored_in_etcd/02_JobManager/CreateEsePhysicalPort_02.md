# Stored data in etcd: Create Ese Physical Port

```
/jobs/all/create:heat_worker:ese_physical_port:6b29894f-8694-4865-92c1-2e78360e65a6:1:xkegm
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "6b29894f-8694-4865-92c1-2e78360e65a6", 
        "handler": "heat_worker", 
        "job_name": "ese_physical_port:6b29894f-8694-4865-92c1-2e78360e65a6:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "xe-0/0/4", 
                "param": "physical_port_name"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "06d6b792b31c40daa546fb0f4e35980d", 
                "param": "tenant_id"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ese_device", 
                        "resource_id": "3fb53223-b614-46b6-92e8-25c3bcbed214"
                    }
                ], 
                "type": "value", 
                "value": "10.161.0.34", 
                "param": "device_ip"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ese_device", 
                        "resource_id": "3fb53223-b614-46b6-92e8-25c3bcbed214"
                    }
                ], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "ese_device", 
                    "resource_id": "3fb53223-b614-46b6-92e8-25c3bcbed214"
                }, 
                "param": "physical_device"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "6", 
                "param": "heat_timeout"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": 1, 
                "param": "version"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "6b29894f-8694-4865-92c1-2e78360e65a6", 
                "param": "gohan_id"
            }
        ], 
        "resource_type": "ese_physical_port", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:ese_physical_port:6b29894f-8694-4865-92c1-2e78360e65a6:1:xkegm", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "connected_port_owner": "mx_downlink", 
            "tags": {}, 
            "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
            "description": "", 
            "existing": "new", 
            "connected_port_id": "", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "ese_device_id": "3fb53223-b614-46b6-92e8-25c3bcbed214", 
            "operational_state": "NO_STATE", 
            "id": "6b29894f-8694-4865-92c1-2e78360e65a6", 
            "name": "xe-0/0/4"
        }
    }, 
    0
]
```
