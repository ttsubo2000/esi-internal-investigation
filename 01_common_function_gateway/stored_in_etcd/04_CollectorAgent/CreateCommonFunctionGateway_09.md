# Stored data in etcd: Create Common Function Gateway

```
/state/v2.0/ports/f84496b5-dc56-4727-87b1-aa06e2471737
{
    "state": {
        "worker_state": "MODIFY_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7\", \"description\": \"Fully Qualified Name of the VMI\", \"output_key\": \"fq_name\"}, {\"output_value\": {\"allowed_address_pair\": []}, \"description\": \"Virtual machine allowed address pairs.\", \"output_key\": \"allowed_address_pairs\"}, {\"output_value\": \"5b5ef6a3-7444-4443-8c6d-4c66aee1df27\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": [\"fa:16:3e:f7:60:7f\"], \"description\": \"Virtual machine interface mac address.\", \"output_key\": \"mac_address\"}, {\"output_value\": [[\"default-domain\", \"admin\", \"b62eefe0-0872-478d-adfe-1a606320f0e7\"]], \"description\": \"Virtual network.\", \"output_key\": \"virtual_network\"}, {\"output_value\": \"f68d0924-ef20-4c1b-ac45-0e6b879af5e7\", \"description\": \"A unique id for the virtual machine interface.\", \"output_key\": \"id\"}, {\"output_value\": \"http://collector-agents-se.monitoringrefactordocker_default:7070/targets/5b5ef6a3-7444-4443-8c6d-4c66aee1df27\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "UPDATE_COMPLETE"
    }, 
    "version": 2, 
    "error": ""
}
```

### Checking stored data at the point of (6) in etcd

```
/monitoring/v2.0/ports/f84496b5-dc56-4727-87b1-aa06e2471737
{
    "version": 2, 
    "vmi": "FAIL"
}
```
