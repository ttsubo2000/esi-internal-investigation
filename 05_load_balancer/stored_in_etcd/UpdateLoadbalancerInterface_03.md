# Stored data in etcd: Update Loadbalancer Interface

These are stored data for "heat_templates" in etcd.

* vnf_instance

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/vnf_instances/398d65ba-0060-456e-b415-5bc954450717
{
    "body": {
        "status": "PENDING_UPDATE", 
        "user_data_format": "RAW", 
        "user_data_parameters": {
            "management_ip": "", 
            "management_mask": "", 
            "management_gateway": ""
        }, 
        "description": null, 
        "availability_zone": "nova", 
        "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
        "vnf_template_id": "f2123d79-e953-4b61-8aee-a217bee284af", 
        "vnf_plan_id": "043fed11-ce3d-48fb-aa8d-13aad5804d83", 
        "networks": [
            {
                "port": "ddc14be4-3480-4e97-a978-817b18f9904c"
            }, 
            {
                "port": "23464cbc-d910-430a-93f7-3776ea07f992"
            }, 
            {
                "port": "a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f"
            }
        ], 
        "reboot": "", 
        "name": "load_balancer-b311c470-d878-4fea-8466-a4393938f2d4", 
        "management_ip": "100.64.193.3", 
        "orchestration_state": "UPDATE_IN_PROGRESS", 
        "owner_tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
        "user_data": "", 
        "operational_state": "INIT", 
        "id": "398d65ba-0060-456e-b415-5bc954450717", 
        "config_drive": false
    }, 
    "version": 2, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/jobs/all/modify:heat_worker:vnf_instance:398d65ba-0060-456e-b415-5bc954450717:2:0wakm
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "398d65ba-0060-456e-b415-5bc954450717", 
        "handler": "heat_worker", 
        "job_name": "vnf_instance:398d65ba-0060-456e-b415-5bc954450717:2", 
        "dependency": [], 
        "version": 2, 
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
                    }, 
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
                "value": 2, 
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
                    }, 
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
                        "port": "23464cbc-d910-430a-93f7-3776ea07f992"
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
        "action": "modify", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "modify:heat_worker:vnf_instance:398d65ba-0060-456e-b415-5bc954450717:2:0wakm", 
        "resource_input": {
            "status": "PENDING_UPDATE", 
            "user_data_format": "RAW", 
            "description": null, 
            "availability_zone": "nova", 
            "operational_state": "INIT", 
            "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
            "vnf_template_id": "f2123d79-e953-4b61-8aee-a217bee284af", 
            "vnf_plan_id": "043fed11-ce3d-48fb-aa8d-13aad5804d83", 
            "reboot": "", 
            "user_data": "", 
            "management_ip": "100.64.193.3", 
            "config_drive": false, 
            "orchestration_state": "UPDATE_IN_PROGRESS", 
            "owner_tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
            "id": "398d65ba-0060-456e-b415-5bc954450717", 
            "user_data_parameters": {
                "management_ip": "", 
                "management_mask": "", 
                "management_gateway": ""
            }, 
            "networks": [
                {
                    "port": "ddc14be4-3480-4e97-a978-817b18f9904c"
                }, 
                {
                    "port": "23464cbc-d910-430a-93f7-3776ea07f992"
                }, 
                {
                    "port": "a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f"
                }
            ], 
            "name": "load_balancer-b311c470-d878-4fea-8466-a4393938f2d4"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/vnf_instances/398d65ba-0060-456e-b415-5bc954450717
{
    "stack_id": "vnf_instance_398d65ba-0060-456e-b415-5bc954450717", 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "stack_status": "UPDATE_COMPLETE", 
    "output": [
        {
            "output_value": "47531b14-72e9-439d-8949-fd941457ecde", 
            "description": "A unique id for the nova server.", 
            "output_key": "server_id"
        }, 
        {
            "output_value": "ed1b9e59-0d6f-44d9-83bc-07ba4a236598", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/ed1b9e59-0d6f-44d9-83bc-07ba4a236598", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack successfully updated", 
    "id": "vnf_instance:398d65ba-0060-456e-b415-5bc954450717"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/vnf_instances/398d65ba-0060-456e-b415-5bc954450717
{
    "heat_outputs": [
        {
            "output_value": "47531b14-72e9-439d-8949-fd941457ecde", 
            "description": "A unique id for the nova server.", 
            "output_key": "server_id"
        }, 
        {
            "output_value": "ed1b9e59-0d6f-44d9-83bc-07ba4a236598", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/ed1b9e59-0d6f-44d9-83bc-07ba4a236598", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "UPDATE_COMPLETE"
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/vnf_instances/398d65ba-0060-456e-b415-5bc954450717
{
    "state": {
        "worker_state": "MODIFY_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"47531b14-72e9-439d-8949-fd941457ecde\", \"description\": \"A unique id for the nova server.\", \"output_key\": \"server_id\"}, {\"output_value\": \"ed1b9e59-0d6f-44d9-83bc-07ba4a236598\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se:7070/targets/ed1b9e59-0d6f-44d9-83bc-07ba4a236598\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "UPDATE_COMPLETE"
    }, 
    "version": 2, 
    "error": ""
}
```

### Checking stored data at the point of (6) in etcd

```
/monitoring/v2.0/vnf_instances/398d65ba-0060-456e-b415-5bc954450717
{
    "version": 2, 
    "server": "UP"
}
```
