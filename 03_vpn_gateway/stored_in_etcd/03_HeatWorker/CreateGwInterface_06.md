# Stored data in etcd: Create Gw Interface

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/ports/53eeb091-3297-4b9b-a200-b6568567e387
{
    "stack_id": "port_53eeb091-3297-4b9b-a200-b6568567e387", 
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
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
            "output_value": "aa5568e3-f399-474f-9ddb-02c0e583b91b", 
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
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/aa5568e3-f399-474f-9ddb-02c0e583b91b", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack successfully updated", 
    "id": "port:53eeb091-3297-4b9b-a200-b6568567e387"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/ports/53eeb091-3297-4b9b-a200-b6568567e387
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
            "output_value": "aa5568e3-f399-474f-9ddb-02c0e583b91b", 
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
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/aa5568e3-f399-474f-9ddb-02c0e583b91b", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "UPDATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/ports/53eeb091-3297-4b9b-a200-b6568567e387
{
    "state": {
        "worker_state": "MODIFY_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7\", \"description\": \"Fully Qualified Name of the VMI\", \"output_key\": \"fq_name\"}, {\"output_value\": {\"allowed_address_pair\": []}, \"description\": \"Virtual machine allowed address pairs.\", \"output_key\": \"allowed_address_pairs\"}, {\"output_value\": \"aa5568e3-f399-474f-9ddb-02c0e583b91b\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": [\"fa:16:3e:f7:60:7f\"], \"description\": \"Virtual machine interface mac address.\", \"output_key\": \"mac_address\"}, {\"output_value\": [[\"default-domain\", \"admin\", \"b62eefe0-0872-478d-adfe-1a606320f0e7\"]], \"description\": \"Virtual network.\", \"output_key\": \"virtual_network\"}, {\"output_value\": \"f68d0924-ef20-4c1b-ac45-0e6b879af5e7\", \"description\": \"A unique id for the virtual machine interface.\", \"output_key\": \"id\"}, {\"output_value\": \"http://collector-agents-se.monitoringrefactordocker_default:7070/targets/aa5568e3-f399-474f-9ddb-02c0e583b91b\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "UPDATE_COMPLETE"
    }, 
    "version": 2, 
    "error": ""
}
```
