# Stored data in etcd: Update Loadbalancer Interface

```
/jobs/all/modify:heat_worker:port:23464cbc-d910-430a-93f7-3776ea07f992:2:v7x4k
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "23464cbc-d910-430a-93f7-3776ea07f992", 
        "handler": "heat_worker", 
        "job_name": "port:23464cbc-d910-430a-93f7-3776ea07f992:2", 
        "dependency": [], 
        "version": 2, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": false, 
                "param": "jinja_attached"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "network", 
                        "resource_id": "774acf45-316f-4431-b31b-08770b76d761"
                    }, 
                    {
                        "resource_type": "network", 
                        "resource_id": "774acf45-316f-4431-b31b-08770b76d761"
                    }
                ], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "network", 
                    "resource_id": "774acf45-316f-4431-b31b-08770b76d761"
                }, 
                "param": "virtual_network"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "47531b14-72e9-439d-8949-fd941457ecde", 
                "param": "virtual_machine"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "23464cbc-d910-430a-93f7-3776ea07f992", 
                "param": "name"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": true, 
                "param": "admin_state_up"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
                "param": "tenant_id"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "13", 
                "param": "heat_timeout"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": [], 
                "param": "virtual_machine_interface_allowed_address_pairs"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "fa:16:3e:84:84:13", 
                "param": "virtual_machine_interface_mac_address"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "compute:nova", 
                "param": "device_owner"
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
                "value": [], 
                "param": "security_groups"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": null, 
                "param": "jinja_force_dependency_gw_interface"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": [
                    {
                        "subnet_id": "c2c9520b-026d-444a-8db9-c1cb9d71c130", 
                        "ip_address": "10.225.225.3"
                    }
                ], 
                "param": "jinja_fixed_ips"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": null, 
                "param": "jinja_force_dependency_cfg"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "compute:nova", 
                "param": "jinja_device_owner"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "subnet", 
                        "resource_id": "c2c9520b-026d-444a-8db9-c1cb9d71c130"
                    }, 
                    {
                        "resource_type": "subnet", 
                        "resource_id": "c2c9520b-026d-444a-8db9-c1cb9d71c130"
                    }
                ], 
                "type": "list", 
                "value": [
                    {
                        "param": "jinja_subnets", 
                        "type": "output_key", 
                        "value": {
                            "output_key": "id", 
                            "resource_type": "subnet", 
                            "resource_id": "c2c9520b-026d-444a-8db9-c1cb9d71c130"
                        }, 
                        "resources": []
                    }
                ], 
                "param": "jinja_subnets"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "23464cbc-d910-430a-93f7-3776ea07f992", 
                "param": "uuid"
            }
        ], 
        "resource_type": "port", 
        "action": "modify", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "modify:heat_worker:port:23464cbc-d910-430a-93f7-3776ea07f992:2:v7x4k", 
        "resource_input": {
            "ese_logical_port_id": null, 
            "allowed_address_pairs": [], 
            "device_owner": "compute:nova", 
            "fake_delete": true, 
            "fixed_ips": [
                {
                    "subnet_id": "c2c9520b-026d-444a-8db9-c1cb9d71c130", 
                    "ip_address": "10.225.225.3"
                }
            ], 
            "id": "23464cbc-d910-430a-93f7-3776ea07f992", 
            "security_groups": [], 
            "binding:vif_type": "vrouter", 
            "mac_address": "fa:16:3e:84:84:13", 
            "status": "PENDING_UPDATE", 
            "description": "", 
            "tags": {}, 
            "segmentation_id": 0, 
            "device_id": "47531b14-72e9-439d-8949-fd941457ecde", 
            "name": "load_balancer-user-port", 
            "managed_by_service": false, 
            "network_id": "774acf45-316f-4431-b31b-08770b76d761", 
            "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
            "admin_state_up": true, 
            "attached": false, 
            "operational_state": "NO_STATE", 
            "orchestration_state": "UPDATE_IN_PROGRESS", 
            "segmentation_type": "flat"
        }
    }, 
    0
]
```
