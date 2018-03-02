# Stored data in etcd: Create Firewall

```
/jobs/all/create:heat_worker:vnf_instance:44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb:1:64gpp
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb", 
        "handler": "heat_worker", 
        "job_name": "vnf_instance:44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "RAW", 
                "param": "user_data_format"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "firewall-8e4c20be-d221-43f4-8325-0162c1f06166", 
                "param": "name"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "nova", 
                "param": "availability_zone"
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
                        "resource_type": "vnf_template", 
                        "resource_id": "5a84974a-9d8b-4887-898b-8e3c095e744d"
                    }
                ], 
                "type": "value", 
                "value": "vyatta-0108-2016", 
                "param": "image"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "", 
                "param": "reboot"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "", 
                "param": "user_data"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "18", 
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
                "value": "44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb", 
                "param": "gohan_id"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "vnf_plan", 
                        "resource_id": "60791395-2267-4553-b115-a38fad3ebf69"
                    }
                ], 
                "type": "value", 
                "value": "m1.large", 
                "param": "flavor"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": [
                    {
                        "port": "cdde9cfd-a898-4911-b812-b6849f611549"
                    }, 
                    {
                        "port": "dea87c7b-b43f-4936-8e32-8995b038b3f8"
                    }, 
                    {
                        "port": "fd09eda4-10b1-4534-984a-7124c338c69d"
                    }
                ], 
                "param": "networks"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": false, 
                "param": "config_drive"
            }
        ], 
        "resource_type": "vnf_instance", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:vnf_instance:44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb:1:64gpp", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "user_data_format": "RAW", 
            "name": "firewall-8e4c20be-d221-43f4-8325-0162c1f06166", 
            "availability_zone": "nova", 
            "operational_state": "NO_STATE", 
            "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
            "vnf_template_id": "5a84974a-9d8b-4887-898b-8e3c095e744d", 
            "vnf_plan_id": "60791395-2267-4553-b115-a38fad3ebf69", 
            "networks": [
                {
                    "port": "cdde9cfd-a898-4911-b812-b6849f611549"
                }, 
                {
                    "port": "dea87c7b-b43f-4936-8e32-8995b038b3f8"
                }, 
                {
                    "port": "fd09eda4-10b1-4534-984a-7124c338c69d"
                }
            ], 
            "reboot": "", 
            "user_data": "", 
            "management_ip": "100.64.193.3", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "owner_tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
            "user_data_parameters": {}, 
            "id": "44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb", 
            "config_drive": false
        }
    }, 
    0
]
```
