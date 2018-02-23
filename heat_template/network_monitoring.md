# monitoring_template: network_monitoring
This is monitoring_template of "network_monitoring" which is provided by gohan via etcd

![scope](../images/esi_interface.003.png)

### (1) Stored data in etcd
These are stored data for "heat_templates" in etcd.
```
/config/v2.0/heat_templates/network_monitoring
{
    "body": {
        "handler": "monitoring_worker", 
        "watch": [], 
        "id": "network_monitoring", 
        "template_file": "network:\n  type: virtual_network\n  uuid: {{ uuid }}\n  fq_name: {{ fq_name }}\ndb_mappings:\n  - mapped_id: {{ uuid }}\n    relation: 'instance'\n", 
        "parameter_mappings": {
            "fq_name": {
                "output_key": "fq_name"
            }, 
            "uuid": {
                "output_key": "id"
            }
        }
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```
You can see the retreiving of "template_file" as "Heat Template".

* virtual_network

```
network:
  type: virtual_network
  uuid: {{ uuid }}
  fq_name: {{ fq_name }}
db_mappings:
  - mapped_id: {{ uuid }}
    relation: 'instance'
```

### (2) Notes for Code of Monitoring-Worker Plugin in esi-worker
* esi-worker/esi_worker/workers/monitoring_worker/resource_plugins/virtual_network.py

```
class VirtualNetworkPlugin(MonitoringWorkerPlugin):
    TYPE = {
        "virtual_network": "monitor_virtual_network"
    }

    REQUIRED_PROPS = ["fq_name"]

    CONTRAIL_PATH = "analytics/uves/virtual-network"
    FLAT = "?flat"

    def _get_status_once(self, props):
        try:
            data = self._contrail_client.retrieve_object_data(
                self.CONTRAIL_PATH, props["fq_name"], [], params=self.FLAT)
            if not data:
                return Resource.DOWN
            return Resource.UP
        except (ContrailClientTimeoutException, KeyError):
            # why KeyError?
            logger.debug(
                "Retrieving virtual network status from Contrail timed out")
            raise ResourcePingException()

```

### (3) Memo for myself ...
