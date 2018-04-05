# Stored data in etcd: Create Gw Interface

```
/jobs/all/create:heat_worker:ese_logical_port:02112bb1-389c-4ff8-9354-94ab43459892:1:7a64g
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "02112bb1-389c-4ff8-9354-94ab43459892", 
        "handler": "heat_worker", 
        "job_name": "ese_logical_port:02112bb1-389c-4ff8-9354-94ab43459892:1", 
        "dependency": [
            "create:heat_worker:port:f3867a99-de18-4512-8e94-f9aaa7b05c3a:1:wrrh0"
        ], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "L2", 
                "param": "logical_port_type"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": 1025, 
                "param": "logical_port_vlan_id"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "06d6b792b31c40daa546fb0f4e35980d", 
                "param": "tenant_id"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ese_physical_port", 
                        "resource_id": "887fecdd-956b-47fa-a348-8940c53a5bf9"
                    }, 
                    {
                        "resource_type": "ese_device", 
                        "resource_id": "3fb53223-b614-46b6-92e8-25c3bcbed214"
                    }
                ], 
                "type": "value", 
                "value": "10.161.0.34", 
                "param": "device_ip"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "6", 
                "param": "heat_timeout"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": [
                    "f3867a99-de18-4512-8e94-f9aaa7b05c3a"
                ], 
                "param": "jinja_port_ids"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": 1, 
                "param": "version"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "port", 
                        "resource_id": "f3867a99-de18-4512-8e94-f9aaa7b05c3a"
                    }
                ], 
                "type": "list", 
                "value": [
                    {
                        "param": "virtual_machine_interface_ids", 
                        "type": "output_key", 
                        "value": {
                            "output_key": "id", 
                            "resource_type": "port", 
                            "resource_id": "f3867a99-de18-4512-8e94-f9aaa7b05c3a"
                        }, 
                        "resources": []
                    }
                ], 
                "param": "virtual_machine_interface_ids"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "xe-0/0/3.1025", 
                "param": "logical_port_name"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "02112bb1-389c-4ff8-9354-94ab43459892", 
                "param": "gohan_id"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ese_physical_port", 
                        "resource_id": "887fecdd-956b-47fa-a348-8940c53a5bf9"
                    }
                ], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "ese_physical_port", 
                    "resource_id": "887fecdd-956b-47fa-a348-8940c53a5bf9"
                }, 
                "param": "physical_port_id"
            }
        ], 
        "resource_type": "ese_logical_port", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:ese_logical_port:02112bb1-389c-4ff8-9354-94ab43459892:1:7a64g", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "name": "xe-0/0/3.1025", 
            "tags": {}, 
            "network_id": "6e557507-1c2a-49b1-ba90-5f616a1f1f3e", 
            "gw_interface_id": "ce8831fd-d30c-41e3-95de-feaee0b95405", 
            "port_ids": [
                "f3867a99-de18-4512-8e94-f9aaa7b05c3a"
            ], 
            "operational_state": "NO_STATE", 
            "vlan_id": 1025, 
            "ese_physical_port_id": "887fecdd-956b-47fa-a348-8940c53a5bf9", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
            "type": "L2", 
            "id": "02112bb1-389c-4ff8-9354-94ab43459892", 
            "connected_resource": "gw_interface", 
            "description": "ESE Logical port for Port f3867a99-de18-4512-8e94-f9aaa7b05c3a"
        }
    }, 
    0
]
```
