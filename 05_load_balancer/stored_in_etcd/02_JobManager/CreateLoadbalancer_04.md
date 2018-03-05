# Stored data in etcd: Create Loadbalancer

```
/jobs/all/create:heat_worker:vnf_instance:398d65ba-0060-456e-b415-5bc954450717:1:pcx6h
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "398d65ba-0060-456e-b415-5bc954450717", 
        "handler": "heat_worker", 
        "job_name": "vnf_instance:398d65ba-0060-456e-b415-5bc954450717:1", 
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
                "value": "load_balancer-b311c470-d878-4fea-8466-a4393938f2d4", 
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
                "value": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
                "param": "tenant_id"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "vnf_template", 
                        "resource_id": "f2123d79-e953-4b61-8aee-a217bee284af"
                    }
                ], 
                "type": "value", 
                "value": "NSVPX-KVM-10.5-57.7_nc", 
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
                "value": "398d65ba-0060-456e-b415-5bc954450717", 
                "param": "gohan_id"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "vnf_plan", 
                        "resource_id": "043fed11-ce3d-48fb-aa8d-13aad5804d83"
                    }
                ], 
                "type": "value", 
                "value": "m1.xlarge", 
                "param": "flavor"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": [
                    {
                        "port": "ddc14be4-3480-4e97-a978-817b18f9904c"
                    }, 
                    {
                        "port": "db3bff62-cf93-48ce-8d6b-cfb2f7fd7dfc"
                    }, 
                    {
                        "port": "a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f"
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
        "id": "create:heat_worker:vnf_instance:398d65ba-0060-456e-b415-5bc954450717:1:pcx6h", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "user_data_format": "RAW", 
            "name": "load_balancer-b311c470-d878-4fea-8466-a4393938f2d4", 
            "availability_zone": "nova", 
            "operational_state": "NO_STATE", 
            "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
            "vnf_template_id": "f2123d79-e953-4b61-8aee-a217bee284af", 
            "vnf_plan_id": "043fed11-ce3d-48fb-aa8d-13aad5804d83", 
            "networks": [
                {
                    "port": "ddc14be4-3480-4e97-a978-817b18f9904c"
                }, 
                {
                    "port": "db3bff62-cf93-48ce-8d6b-cfb2f7fd7dfc"
                }, 
                {
                    "port": "a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f"
                }
            ], 
            "reboot": "", 
            "user_data": "", 
            "management_ip": "100.64.193.3", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "owner_tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
            "user_data_parameters": {
                "management_ip": "", 
                "management_mask": "", 
                "management_gateway": ""
            }, 
            "id": "398d65ba-0060-456e-b415-5bc954450717", 
            "config_drive": false
        }
    }, 
    0
]
```
