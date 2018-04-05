# Stored data in etcd: Create Ese Physical Port

```
/jobs/all/create:heat_worker:ese_physical_port:887fecdd-956b-47fa-a348-8940c53a5bf9:1:hapn7
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "887fecdd-956b-47fa-a348-8940c53a5bf9", 
        "handler": "heat_worker", 
        "job_name": "ese_physical_port:887fecdd-956b-47fa-a348-8940c53a5bf9:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "xe-0/0/3", 
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
                "value": "887fecdd-956b-47fa-a348-8940c53a5bf9", 
                "param": "gohan_id"
            }
        ], 
        "resource_type": "ese_physical_port", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:ese_physical_port:887fecdd-956b-47fa-a348-8940c53a5bf9:1:hapn7", 
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
            "id": "887fecdd-956b-47fa-a348-8940c53a5bf9", 
            "name": "xe-0/0/3"
        }
    }, 
    0
]
```
