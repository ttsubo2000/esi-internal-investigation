# monitoring_template: vnf_instance_monitoring
This is monitoring_template of "vnf_instance_monitoring" which is provided by gohan via etcd

![scope](../images/esi_interface.003.png)

### (1) Stored data in etcd
These are stored data for "heat_templates" in etcd.
```
/config/v2.0/heat_templates/vnf_instance_monitoring
{
    "body": {
        "handler": "monitoring_worker", 
        "watch": [], 
        "id": "vnf_instance_monitoring", 
        "template_file": "server:\n  type: nova_vm\n  server_id: {{ server_id }}\n", 
        "parameter_mappings": {
            "server_id": {
                "output_key": "server_id"
            }, 
            "instance_ip": {
                "field": "management_ip"
            }
        }
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```
You can see the retreiving of "template_file" as "Heat Template".

* nova_vm

```
server:
  type: nova_vm
  server_id: {{ server_id }}
```

### (2) Notes for Code of Monitoring-Worker Plugin in esi-worker
* esi-worker/esi_worker/workers/monitoring_worker/resource_plugins/nova_vm.py

```
class NovaVMPlugin(MonitoringWorkerPlugin):
    TYPE = {
        "nova_vm": "monitor_nova_vm"
    }

    REQUIRED_PROPS = ["server_id"]

    def _get_status_once(self, props):
        server_id = props["server_id"]
        if self._nova_client.get_vm_state(props["server_id"]) != 'ACTIVE':
            logger.debug("VM {} is not responding".format(server_id))
            return Resource.DOWN
        return Resource.UP
```

### (3) Memo for myself ...
