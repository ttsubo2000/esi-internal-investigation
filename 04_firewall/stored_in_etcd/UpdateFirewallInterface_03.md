# Stored data in etcd: Update Firewall Interface

These are stored data for "heat_templates" in etcd.

* vnf_instance

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/vnf_instances/44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb
{
    "body": {
        "status": "PENDING_UPDATE", 
        "user_data_format": "RAW", 
        "user_data_parameters": {}, 
        "description": null, 
        "availability_zone": "nova", 
        "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
        "vnf_template_id": "5a84974a-9d8b-4887-898b-8e3c095e744d", 
        "vnf_plan_id": "60791395-2267-4553-b115-a38fad3ebf69", 
        "networks": [
            {
                "port": "cdde9cfd-a898-4911-b812-b6849f611549"
            }, 
            {
                "port": "472879c4-4611-4762-a069-293e0081bcbf"
            }, 
            {
                "port": "fd09eda4-10b1-4534-984a-7124c338c69d"
            }
        ], 
        "reboot": "", 
        "name": "firewall-8e4c20be-d221-43f4-8325-0162c1f06166", 
        "management_ip": "100.64.193.3", 
        "orchestration_state": "UPDATE_IN_PROGRESS", 
        "owner_tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
        "user_data": "", 
        "operational_state": "INIT", 
        "id": "44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb", 
        "config_drive": false
    }, 
    "version": 2, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/jobs/all/modify:heat_worker:vnf_instance:44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb:2:wqq3h
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb", 
        "handler": "heat_worker", 
        "job_name": "vnf_instance:44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb:2", 
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
                    }, 
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
                "value": 2, 
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
                    }, 
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
                        "port": "472879c4-4611-4762-a069-293e0081bcbf"
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
        "action": "modify", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "modify:heat_worker:vnf_instance:44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb:2:wqq3h", 
        "resource_input": {
            "status": "PENDING_UPDATE", 
            "user_data_format": "RAW", 
            "description": null, 
            "availability_zone": "nova", 
            "operational_state": "INIT", 
            "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
            "vnf_template_id": "5a84974a-9d8b-4887-898b-8e3c095e744d", 
            "vnf_plan_id": "60791395-2267-4553-b115-a38fad3ebf69", 
            "reboot": "", 
            "user_data": "", 
            "management_ip": "100.64.193.3", 
            "config_drive": false, 
            "orchestration_state": "UPDATE_IN_PROGRESS", 
            "owner_tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
            "id": "44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb", 
            "user_data_parameters": {}, 
            "networks": [
                {
                    "port": "cdde9cfd-a898-4911-b812-b6849f611549"
                }, 
                {
                    "port": "472879c4-4611-4762-a069-293e0081bcbf"
                }, 
                {
                    "port": "fd09eda4-10b1-4534-984a-7124c338c69d"
                }
            ], 
            "name": "firewall-8e4c20be-d221-43f4-8325-0162c1f06166"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/vnf_instances/44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb
{
    "stack_id": "vnf_instance_44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb", 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "stack_status": "UPDATE_COMPLETE", 
    "output": [
        {
            "output_value": "2e555b09-e0d7-4cce-8854-c481a2363917", 
            "description": "A unique id for the nova server.", 
            "output_key": "server_id"
        }, 
        {
            "output_value": "99de7768-161e-46ef-a973-2e794fd84382", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/99de7768-161e-46ef-a973-2e794fd84382", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack successfully updated", 
    "id": "vnf_instance:44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/vnf_instances/44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb
{
    "heat_outputs": [
        {
            "output_value": "2e555b09-e0d7-4cce-8854-c481a2363917", 
            "description": "A unique id for the nova server.", 
            "output_key": "server_id"
        }, 
        {
            "output_value": "99de7768-161e-46ef-a973-2e794fd84382", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/99de7768-161e-46ef-a973-2e794fd84382", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "UPDATE_COMPLETE"
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/vnf_instances/44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb
{
    "state": {
        "worker_state": "MODIFY_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"2e555b09-e0d7-4cce-8854-c481a2363917\", \"description\": \"A unique id for the nova server.\", \"output_key\": \"server_id\"}, {\"output_value\": \"99de7768-161e-46ef-a973-2e794fd84382\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se:7070/targets/99de7768-161e-46ef-a973-2e794fd84382\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "UPDATE_COMPLETE"
    }, 
    "version": 2, 
    "error": ""
}
```

### Checking stored data at the point of (6) in etcd

```
/monitoring/v2.0/vnf_instances/44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb
{
    "version": 2, 
    "server": "UP"
}
```
