# Stored data in etcd: Create Firewall

These are stored data for "heat_templates" in etcd.

* firewall_interface

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/firewall_interfaces/1c351257-d185-40b7-b04a-6272de75d434
{
    "body": {
        "status": "PENDING_CREATE", 
        "type": "management", 
        "name": "dp0s3", 
        "network_id": "75c2c3ec-7fe7-494c-a35c-db3f94d3a554", 
        "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
        "vnf_interface_id": "c8fef8f8-a7a1-448f-ae76-81992e598016", 
        "operational_state": "NO_STATE", 
        "firewall_id": "8e4c20be-d221-43f4-8325-0162c1f06166", 
        "orchestration_state": "CREATE_IN_PROGRESS", 
        "slot_number": 0, 
        "ip_address": "100.64.193.3", 
        "id": "1c351257-d185-40b7-b04a-6272de75d434"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/jobs/all/create:heat_worker:firewall_interface:1c351257-d185-40b7-b04a-6272de75d434:1:249va
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "1c351257-d185-40b7-b04a-6272de75d434", 
        "handler": "heat_worker", 
        "job_name": "firewall_interface:1c351257-d185-40b7-b04a-6272de75d434:1", 
        "dependency": [
            "create:heat_worker:vnf_instance:44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb:1:64gpp", 
            "create:heat_worker:firewall:8e4c20be-d221-43f4-8325-0162c1f06166:1:uvr6e"
        ], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": 0, 
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
                "value": "1c351257-d185-40b7-b04a-6272de75d434", 
                "param": "gohan_id"
            }
        ], 
        "resource_type": "firewall_interface", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:firewall_interface:1c351257-d185-40b7-b04a-6272de75d434:1:249va", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "name": "dp0s3", 
            "network_id": "75c2c3ec-7fe7-494c-a35c-db3f94d3a554", 
            "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
            "operational_state": "NO_STATE", 
            "ip_address": "100.64.193.3", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "firewall_id": "8e4c20be-d221-43f4-8325-0162c1f06166", 
            "vnf_interface_id": "c8fef8f8-a7a1-448f-ae76-81992e598016", 
            "slot_number": 0, 
            "type": "management", 
            "id": "1c351257-d185-40b7-b04a-6272de75d434"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/firewall_interfaces/1c351257-d185-40b7-b04a-6272de75d434
{
    "stack_id": "firewall_interface_1c351257-d185-40b7-b04a-6272de75d434", 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "ecbc7461-e883-4c21-bcf6-b91a105a533c", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/ecbc7461-e883-4c21-bcf6-b91a105a533c", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "firewall_interface:1c351257-d185-40b7-b04a-6272de75d434"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/firewall_interfaces/1c351257-d185-40b7-b04a-6272de75d434
{
    "heat_outputs": [
        {
            "output_value": "ecbc7461-e883-4c21-bcf6-b91a105a533c", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/ecbc7461-e883-4c21-bcf6-b91a105a533c", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (5) in etcd
```
/state/v2.0/firewall_interfaces/1c351257-d185-40b7-b04a-6272de75d434
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"ecbc7461-e883-4c21-bcf6-b91a105a533c\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se:7070/targets/ecbc7461-e883-4c21-bcf6-b91a105a533c\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```

### Checking stored data at the point of (6) in etcd
```
/monitoring/v2.0/firewall_interfaces/1c351257-d185-40b7-b04a-6272de75d434
{
    "interface": "UP",
    "version": 1
}
```
