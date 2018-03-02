# Stored data in etcd: Create Firewall

```
/jobs/all/create:heat_worker:firewall:8e4c20be-d221-43f4-8325-0162c1f06166:1:uvr6e
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "8e4c20be-d221-43f4-8325-0162c1f06166", 
        "handler": "heat_worker", 
        "job_name": "firewall:8e4c20be-d221-43f4-8325-0162c1f06166:1", 
        "dependency": [
            "create:heat_worker:vnf_instance:44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb:1:64gpp"
        ], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "192.168.1.1", 
                "param": "default_gateway"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "0f40dffa48614d9baa7eaac7e7532099", 
                "param": "tenant_id"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "k3cjZ4FNRrkX", 
                "param": "user_password"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "", 
                "param": "other_username"
            }, 
            {
                "resources": [
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
                "value": "user-admin", 
                "param": "admin_username"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "user-read", 
                "param": "user_username"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": 13, 
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
                "value": "", 
                "param": "other_password"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "f5UhAERVGmYS", 
                "param": "admin_password"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "vnf_instance", 
                        "resource_id": "44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb"
                    }, 
                    {
                        "resource_type": "vnf_template", 
                        "resource_id": "5a84974a-9d8b-4887-898b-8e3c095e744d"
                    }
                ], 
                "type": "value", 
                "value": {
                    "username": "vfwadmin", 
                    "password": "password"
                }, 
                "param": "credentials"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "8e4c20be-d221-43f4-8325-0162c1f06166", 
                "param": "gohan_id"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": [
                    {
                        "ifname": "dp0s4", 
                        "type": "disable"
                    }, 
                    {
                        "ifname": "dp0s5", 
                        "type": "disable"
                    }
                ], 
                "param": "networks"
            }
        ], 
        "resource_type": "firewall", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:firewall:8e4c20be-d221-43f4-8325-0162c1f06166:1:uvr6e", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "description": "", 
            "default_gateway": "192.168.1.1", 
            "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
            "interfaces": [], 
            "other_username": "", 
            "admin_username": "user-admin", 
            "vnf_instance_id": "44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb", 
            "user_username": "user-read", 
            "user_password": "k3cjZ4FNRrkX", 
            "other_password": "", 
            "admin_password": "f5UhAERVGmYS", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "availability_zone": "nova", 
            "id": "8e4c20be-d221-43f4-8325-0162c1f06166", 
            "operational_state": "NO_STATE", 
            "networks": [
                {
                    "ifname": "dp0s4", 
                    "type": "disable"
                }, 
                {
                    "ifname": "dp0s5", 
                    "type": "disable"
                }
            ], 
            "firewall_plan_id": "40520774-4f10-4e8c-90fa-550bd4cdf101", 
            "name": ""
        }
    }, 
    0
]
```
