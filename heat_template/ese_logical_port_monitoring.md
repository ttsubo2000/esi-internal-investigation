# monitoring_template: ese_logical_port_monitoring
This is monitoring_template of "ese_logical_port_monitoring" which is provided by gohan via etcd

![scope](../images/esi_interface.003.png)

### (1) Stored data in etcd
These are stored data for "heat_templates" in etcd.
```
/config/v2.0/heat_templates/ese_logical_port_monitoring
{
    "body": {
        "handler": "monitoring_worker", 
        "watch": [], 
        "id": "ese_logical_port_monitoring", 
        "template_file": "logical_port:\n  type: logical_port\n  community_name: {{ community_name }}\n  device_ip: {{ device_ip }}\n  name: {{ name }}\n{% for port_id in port_ids %}\ndb_mappings:\n  - mapped_id: {{ device_ip }}-{{ name }}\n    resource_id: {{ port_id }}\n    resource_type: port\n    relation: baremetal\n{% endfor %}\n", 
        "parameter_mappings": {
            "name": {
                "field": "name"
            }, 
            "port_ids": {
                "field": "port_ids"
            }, 
            "device_ip": {
                "field": "management_ip_address", 
                "path": [
                    "ese_physical_port_id", 
                    "ese_device_id"
                ]
            }, 
            "contarail_port_id": {
                "output_key": "id"
            }, 
            "community_name": {
                "constant": "ESE_NODE_COMMUNITY"
            }, 
            "id": {
                "field": "id"
            }
        }
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```
You can see the retreiving of "template_file" as "Heat Template".

* logical_port

```
logical_port:
  type: logical_port
  community_name: {{ community_name }}
  device_ip: {{ device_ip }}
  name: {{ name }}
{% for port_id in port_ids %}
db_mappings:
  - mapped_id: {{ device_ip }}-{{ name }}
    resource_id: {{ port_id }}
    resource_type: port
    relation: baremetal
{% endfor %}
```

### (2) Notes for Code of Monitoring-Worker Plugin in esi-worker
* esi-worker/esi_worker/workers/monitoring_worker/resource_plugins/physical_logical_port.py

```
class PhysicalLogicalPortPlugin(MonitoringWorkerPlugin):
    TYPE = {
        "physical_port": "monitor_physical_port",
        "logical_port": "monitor_logical_port",
    }

    REQUIRED_PROPS = ["device_ip", "community_name", "name"]

    IfOperStatusUP = 1
    Interfaces_OID = "1.3.6.1.2.1.31.1.1.1.1"
    IfOperStatus_OID = "1.3.6.1.2.1.2.2.1.8"

    def _get_status_once(self, props):
        host = props["device_ip"]
        port = props.get("port", self._snmp_client.SNMP_DEFAULT_PORT)
        community = props["community_name"]
        name = props["name"]

        try:
            interfaces = self._snmp_client.\
                read_all_under_oid(host, port, community, self.Interfaces_OID)
            index = self._get_interface_idx(interfaces, name)
            oid = self.IfOperStatus_OID + "." + index
            resp = self._snmp_client.read_value(host, port, community, [oid])
            if int(resp[oid]) != self.IfOperStatusUP:
                logger.debug("Interface {}-{} is down".format(host, name))
                return Resource.DOWN
            return Resource.UP
        except SNMPException as e:
            logger.debug("SNMP exception: " + e.message)
            raise ResourcePingException()

    def _get_interface_idx(self, interfaces, name):
        oid = self.Interfaces_OID
        for key, value in interfaces.iteritems():
            if value == name:
                return key[len(oid) + 1:]
        logger.debug('Interface "{}" not found under oid {}'.
                     format(name, self.Interfaces_OID))
        raise ResourcePingException()
```

### (3) Memo for myself ...
