# monitoring_template: port_monitoring
This is monitoring_template of "port_monitoring" which is provided by gohan via etcd

![scope](../images/esi_interface.003.png)

### (1) Stored data in etcd
These are stored data for "heat_templates" in etcd.
```
/config/v2.0/heat_templates/port_monitoring
{
    "body": {
        "handler": "monitoring_worker", 
        "watch": [], 
        "id": "port_monitoring", 
        "template_file": "{% if device_owner and attached %}\nvmi:\n  type: virtual_machine_interface\n  uuid: {{ vmi_uuid }}\n  fq_name: {{ vmi_fq_name }}\n  timeout: 120\n{% endif %}\n{% if device_owner | match('compute') and attached %}\ndb_mappings:\n  - mapped_id: {{ vmi_fq_name | replace(':', '-') }}\n    relation: 'vmi'\n{% endif %}\n", 
        "parameter_mappings": {
            "device_owner": {
                "field": "device_owner"
            }, 
            "attached": {
                "field": "attached"
            }, 
            "vmi_fq_name": {
                "output_key": "fq_name"
            }, 
            "vmi_uuid": {
                "output_key": "id"
            }
        }
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```
You can see the retreiving of "template_file" as "Heat Template".

* virtual_machine_interface

```
{% if device_owner and attached %}
vmi:
  type: virtual_machine_interface
  uuid: {{ vmi_uuid }}
  fq_name: {{ vmi_fq_name }}
  timeout: 120
{% endif %}
{% if device_owner | match('compute') and attached %}
db_mappings:
  - mapped_id: {{ vmi_fq_name | replace(':', '-') }}
    relation: 'vmi'
{% endif %}
```

### (2) Notes for Code of Monitoring-Worker Plugin in esi-worker
* esi-worker/esi_worker/workers/monitoring_worker/resource_plugins/virtual_machine_interface.py

```
class VirtualMachineInterfacePlugin(MonitoringWorkerPlugin):
    TYPE = {
        "virtual_machine_interface": "monitor_virtual_machine_interface"
    }

    REQUIRED_PROPS = ["fq_name"]

    CONTRAIL_PATH = "analytics/uves/virtual-machine-interface"
    FLAT = "?flat"

    def _get_status_once(self, props):
        try:
            data = self._contrail_client.retrieve_object_data(
                self.CONTRAIL_PATH, props["fq_name"],
                ["UveVMInterfaceAgent", "l2_active"], params=self.FLAT)
            if not data:
                return Resource.DOWN
            return Resource.UP
        except (ContrailClientTimeoutException, KeyError):
            # why KeyError?
            logger.debug("Retrieving virtual machine interface status from "
                         "Contrail timed out")
            raise ResourcePingException()
```

### (3) Memo for myself ...
