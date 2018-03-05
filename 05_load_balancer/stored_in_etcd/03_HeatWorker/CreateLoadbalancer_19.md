# Stored data in etcd: Create Loadbalancer

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/ports/a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f
{
    "stack_id": "port_a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f", 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "stack_status": "UPDATE_COMPLETE", 
    "output": [
        {
            "output_value": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7", 
            "description": "Fully Qualified Name of the VMI", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": {
                "allowed_address_pair": []
            }, 
            "description": "Virtual machine allowed address pairs.", 
            "output_key": "allowed_address_pairs"
        }, 
        {
            "output_value": "794f28f6-0c97-4a0e-af7a-5696dcd4c3c7", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": [
                "fa:16:3e:f7:60:7f"
            ], 
            "description": "Virtual machine interface mac address.", 
            "output_key": "mac_address"
        }, 
        {
            "output_value": [
                [
                    "default-domain", 
                    "admin", 
                    "b62eefe0-0872-478d-adfe-1a606320f0e7"
                ]
            ], 
            "description": "Virtual network.", 
            "output_key": "virtual_network"
        }, 
        {
            "output_value": "f68d0924-ef20-4c1b-ac45-0e6b879af5e7", 
            "description": "A unique id for the virtual machine interface.", 
            "output_key": "id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/794f28f6-0c97-4a0e-af7a-5696dcd4c3c7", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack successfully updated", 
    "id": "port:a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/ports/a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f
{
    "heat_outputs": [
        {
            "output_value": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7", 
            "description": "Fully Qualified Name of the VMI", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": {
                "allowed_address_pair": []
            }, 
            "description": "Virtual machine allowed address pairs.", 
            "output_key": "allowed_address_pairs"
        }, 
        {
            "output_value": "794f28f6-0c97-4a0e-af7a-5696dcd4c3c7", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": [
                "fa:16:3e:f7:60:7f"
            ], 
            "description": "Virtual machine interface mac address.", 
            "output_key": "mac_address"
        }, 
        {
            "output_value": [
                [
                    "default-domain", 
                    "admin", 
                    "b62eefe0-0872-478d-adfe-1a606320f0e7"
                ]
            ], 
            "description": "Virtual network.", 
            "output_key": "virtual_network"
        }, 
        {
            "output_value": "f68d0924-ef20-4c1b-ac45-0e6b879af5e7", 
            "description": "A unique id for the virtual machine interface.", 
            "output_key": "id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/794f28f6-0c97-4a0e-af7a-5696dcd4c3c7", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "UPDATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/ports/a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f
{
    "state": {
        "worker_state": "MODIFY_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7\", \"description\": \"Fully Qualified Name of the VMI\", \"output_key\": \"fq_name\"}, {\"output_value\": {\"allowed_address_pair\": []}, \"description\": \"Virtual machine allowed address pairs.\", \"output_key\": \"allowed_address_pairs\"}, {\"output_value\": \"794f28f6-0c97-4a0e-af7a-5696dcd4c3c7\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": [\"fa:16:3e:f7:60:7f\"], \"description\": \"Virtual machine interface mac address.\", \"output_key\": \"mac_address\"}, {\"output_value\": [[\"default-domain\", \"admin\", \"b62eefe0-0872-478d-adfe-1a606320f0e7\"]], \"description\": \"Virtual network.\", \"output_key\": \"virtual_network\"}, {\"output_value\": \"f68d0924-ef20-4c1b-ac45-0e6b879af5e7\", \"description\": \"A unique id for the virtual machine interface.\", \"output_key\": \"id\"}, {\"output_value\": \"http://collector-agents-se:7070/targets/794f28f6-0c97-4a0e-af7a-5696dcd4c3c7\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "UPDATE_COMPLETE"
    }, 
    "version": 3, 
    "error": ""
}
```
