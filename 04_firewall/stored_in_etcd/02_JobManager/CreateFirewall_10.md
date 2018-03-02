# Stored data in etcd: Create Firewall

```
/jobs/all/create:heat_worker:firewall_interface:3543155d-0d9a-43a3-ae77-3479cf8a0e4a:1:37zym
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "3543155d-0d9a-43a3-ae77-3479cf8a0e4a", 
        "handler": "heat_worker", 
        "job_name": "firewall_interface:3543155d-0d9a-43a3-ae77-3479cf8a0e4a:1", 
        "dependency": [
            "create:heat_worker:vnf_instance:44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb:1:64gpp", 
            "create:heat_worker:firewall:8e4c20be-d221-43f4-8325-0162c1f06166:1:uvr6e"
        ], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": 1, 
                "param": "jinja_slot_number"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "0f40dffa48614d9baa7eaac7e7532099", 
                "param": "tenant_id"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "firewall", 
                        "resource_id": "8e4c20be-d221-43f4-8325-0162c1f06166"
                    }, 
                    {
                        "resource_type": "vnf_instance", 
                        "resource_id": "44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb"
                    }
                ], 
                "type": "value", 
                "value": "100.64.193.3", 
                "param": "management_ip"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": 3, 
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
                "value": "3543155d-0d9a-43a3-ae77-3479cf8a0e4a", 
                "param": "gohan_id"
            }
        ], 
        "resource_type": "firewall_interface", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:firewall_interface:3543155d-0d9a-43a3-ae77-3479cf8a0e4a:1:37zym", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "name": "dp0s4", 
            "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
            "operational_state": "NO_STATE", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "firewall_id": "8e4c20be-d221-43f4-8325-0162c1f06166", 
            "vnf_interface_id": "c6cf2771-be40-4d16-ba15-20a62f8b78f6", 
            "slot_number": 1, 
            "type": "user", 
            "id": "3543155d-0d9a-43a3-ae77-3479cf8a0e4a"
        }
    }, 
    0
]
```
