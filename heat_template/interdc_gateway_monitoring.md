# monitoring_template: interdc_gateway_monitoring
This is monitoring_template of "interdc_gateway_monitoring" which is provided by gohan via etcd

![scope](../images/esi_interface.003.png)

### (1) Stored data in etcd
These are stored data for "heat_templates" in etcd.
```
/config/v2.0/heat_templates/interdc_gateway_monitoring
{
    "body": {
        "handler": "monitoring_worker", 
        "watch": [], 
        "id": "interdc_gateway_monitoring", 
        "template_file": "downlink:\n  type: etcd_reader\n  etcd_type: ha_interface\n  etcd_id: {{ downlink_interface_id }}\n  timeout: 120\ndb_mappings:\n  - mapped_id: {{gohan_id}}\n    relation: 'instance'\n", 
        "parameter_mappings": {
            "downlink_interface_id": {
                "field": "downlink_interface_id"
            }, 
            "gohan_id": {
                "field": "id"
            }
        }
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```
You can see the retreiving of "template_file" as "Heat Template".

* etcd_reader

```
downlink:
  type: etcd_reader
  etcd_type: ha_interface
  etcd_id: {{ downlink_interface_id }}
  timeout: 120
db_mappings:
  - mapped_id: {{gohan_id}}
    relation: 'instance'
```

### (2) Notes for Code of Monitoring-Worker Plugin in esi-worker
* esi-worker/esi_worker/workers/monitoring_worker/resource_plugins/etcd_reader.py

```
class ETCDReaderPlugin(MonitoringWorkerPlugin):
    # This plugin should not longer be required, it's logic is already
    # handled by gohan extension (monitoring.js)

    TYPE = {
        "etcd_reader": ""
    }

    DEFAULT_PROPS = {
        "time_between_retries": 10
    }

    REQUIRED_PROPS = ["etcd_type", "etcd_id"]

    def _get_status_once(self, props):
        try:
            state = self._etcd_client.get_resource_monitoring_state(
                props["etcd_type"], props["etcd_id"])
        except (worker_exceptions.StateNotFound, ValueError):
            # why ValueError?
            logger.debug("{}:{} state not found"
                         .format(props["etcd_type"], props["etcd_id"]))
            raise ResourcePingException()

        for dep_name, status in state.items():
            if status != Resource.UP:
                logger.debug((
                    "etcd_reader: {}:{} status of {} is not ACTIVE".format(
                        props["etcd_type"], props["etcd_id"], dep_name)))
                return Resource.DOWN
        return Resource.UP
```

### (3) Memo for myself ...
