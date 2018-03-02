# Stored data in etcd: Create Network (user-net)

```
/jobs/all/create:heat_worker:network:82712b89-c35c-4276-83cb-818860d41f9e:1:bsexy
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "82712b89-c35c-4276-83cb-818860d41f9e", 
        "handler": "heat_worker", 
        "job_name": "network:82712b89-c35c-4276-83cb-818860d41f9e:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "82712b89-c35c-4276-83cb-818860d41f9e", 
                "param": "uuid"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "3", 
                "param": "heat_timeout"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "82712b89-c35c-4276-83cb-818860d41f9e", 
                "param": "name"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": true, 
                "param": "admin_state_up"
            }
        ], 
        "resource_type": "network", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:network:82712b89-c35c-4276-83cb-818860d41f9e:1:bsexy", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "subnets": [], 
            "description": "firewall network", 
            "tags": {}, 
            "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
            "admin_state_up": true, 
            "plane": "data", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "shared": false, 
            "id": "82712b89-c35c-4276-83cb-818860d41f9e", 
            "name": "sample-fw-net"
        }
    }, 
    0
]
```
