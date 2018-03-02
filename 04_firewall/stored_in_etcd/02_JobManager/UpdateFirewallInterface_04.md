# Stored data in etcd: Update Firewall Interface

```
/jobs/all/modify:heat_worker:firewall_interface:3543155d-0d9a-43a3-ae77-3479cf8a0e4a:2:ur5by
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "3543155d-0d9a-43a3-ae77-3479cf8a0e4a", 
        "handler": "heat_worker", 
        "job_name": "firewall_interface:3543155d-0d9a-43a3-ae77-3479cf8a0e4a:2", 
        "dependency": [
            "modify:heat_worker:vnf_instance:44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb:2:wqq3h"
        ], 
        "version": 2, 
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
                    }, 
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
                "value": 2, 
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
        "action": "modify", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "modify:heat_worker:firewall_interface:3543155d-0d9a-43a3-ae77-3479cf8a0e4a:2:ur5by", 
        "resource_input": {
            "status": "PENDING_UPDATE", 
            "virtual_ip_properties": null, 
            "description": null, 
            "network_id": "82712b89-c35c-4276-83cb-818860d41f9e", 
            "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
            "operational_state": "INIT", 
            "ip_address": "10.98.76.3", 
            "orchestration_state": "UPDATE_IN_PROGRESS", 
            "firewall_id": "8e4c20be-d221-43f4-8325-0162c1f06166", 
            "vnf_interface_id": "c6cf2771-be40-4d16-ba15-20a62f8b78f6", 
            "slot_number": 1, 
            "virtual_ip_address": null, 
            "type": "user", 
            "id": "3543155d-0d9a-43a3-ae77-3479cf8a0e4a", 
            "name": "dp0s4"
        }
    }, 
    0
]
```
