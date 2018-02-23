# monitoring_template: ese_device_monitoring
This is monitoring_template of "ese_device_monitoring" which is provided by gohan via etcd

![scope](../images/esi_interface.003.png)

### (1) Stored data in etcd
These are stored data for "heat_templates" in etcd.
```
/config/v2.0/heat_templates/ese_device_monitoring
{
    "body": {
        "handler": "monitoring_worker", 
        "watch": [], 
        "id": "ese_device_monitoring", 
        "template_file": "switch:\n  type: switch\n  community_name: {{ community_name }}\n  ip: {{ device_ip }}\n  mibs: []\n", 
        "parameter_mappings": {
            "community_name": {
                "constant": "ESE_NODE_COMMUNITY"
            }, 
            "device_ip": {
                "field": "management_ip_address"
            }
        }
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```
You can see the retreiving of "template_file" as "Heat Template".

* switch

```
switch:
  type: switch
  community_name: {{ community_name }}
  ip: {{ device_ip }}
  mibs: []
```

### (2) Notes for Code of Monitoring-Worker Plugin in esi-worker
* esi-worker/esi_worker/workers/monitoring_worker/resource_plugins/mx_qfx.py

```
class QFXSwitchPlugin(MonitoringWorkerPlugin):
    TYPE = {
        "switch": "monitor_snmp_device",
        "router": "monitor_snmp_device"
    }

    REQUIRED_PROPS = ["ip", "community_name"]

    def _get_status_once(self, props):
        host = props["ip"]
        port = props.get("port", self._snmp_client.SNMP_DEFAULT_PORT)
        community = props["community_name"]

        oid = ["1.3.6.1.2.1.1.3.0"]

        try:
            uptime1 = self._snmp_client.read_value(host, port, community, oid)
            time.sleep(1)
            uptime2 = self._snmp_client.read_value(host, port, community, oid)
            if uptime2 <= uptime1:
                logger.debug("Invalid sysUpTime values retrieved.")
                return Resource.DOWN
            return Resource.UP
        except SNMPException as e:
            logger.debug("SNMP Exception: " + e.message)
            raise ResourcePingException()
```

### (3) Memo for myself ...
