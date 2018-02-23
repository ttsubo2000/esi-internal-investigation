# Stored data in etcd: Create Network (user-net)

These are stored data for "heat_templates" in etcd.

* network

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/networks/82712b89-c35c-4276-83cb-818860d41f9e
{
    "body": {
        "status": "PENDING_CREATE", 
        "subnets": [], 
        "description": "firewall network", 
        "admin_state_up": true, 
        "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
        "tags": {}, 
        "plane": "data", 
        "orchestration_state": "CREATE_IN_PROGRESS", 
        "shared": false, 
        "id": "82712b89-c35c-4276-83cb-818860d41f9e", 
        "name": "sample-fw-net"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

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

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/networks/82712b89-c35c-4276-83cb-818860d41f9e
{
    "stack_id": "network_82712b89-c35c-4276-83cb-818860d41f9e", 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": [], 
            "description": "The name of the virtual network.", 
            "output_key": "route_targets"
        }, 
        {
            "output_value": "default-domain:usertenant:82712b89-c35c-4276-83cb-818860d41f9e", 
            "description": "The FQ name of the virtual network.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "82712b89-c35c-4276-83cb-818860d41f9e", 
            "description": "A unique id for the virtual network.", 
            "output_key": "id"
        }, 
        {
            "output_value": "82712b89-c35c-4276-83cb-818860d41f9e", 
            "description": "The name of the virtual network.", 
            "output_key": "name"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "network:82712b89-c35c-4276-83cb-818860d41f9e"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/networks/82712b89-c35c-4276-83cb-818860d41f9e
{
    "heat_outputs": [
        {
            "output_value": [], 
            "description": "The name of the virtual network.", 
            "output_key": "route_targets"
        }, 
        {
            "output_value": "default-domain:usertenant:82712b89-c35c-4276-83cb-818860d41f9e", 
            "description": "The FQ name of the virtual network.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "82712b89-c35c-4276-83cb-818860d41f9e", 
            "description": "A unique id for the virtual network.", 
            "output_key": "id"
        }, 
        {
            "output_value": "82712b89-c35c-4276-83cb-818860d41f9e", 
            "description": "The name of the virtual network.", 
            "output_key": "name"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/networks/82712b89-c35c-4276-83cb-818860d41f9e
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": [], \"description\": \"The name of the virtual network.\", \"output_key\": \"route_targets\"}, {\"output_value\": \"default-domain:usertenant:82712b89-c35c-4276-83cb-818860d41f9e\", \"description\": \"The FQ name of the virtual network.\", \"output_key\": \"fq_name\"}, {\"output_value\": \"82712b89-c35c-4276-83cb-818860d41f9e\", \"description\": \"A unique id for the virtual network.\", \"output_key\": \"id\"}, {\"output_value\": \"82712b89-c35c-4276-83cb-818860d41f9e\", \"description\": \"The name of the virtual network.\", \"output_key\": \"name\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
