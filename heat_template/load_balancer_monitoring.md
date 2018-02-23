# monitoring_template: load_balancer_monitoring.md
This is monitoring_template of "load_balancer_monitoring.md" which is provided by gohan via etcd

![scope](../images/esi_interface.003.png)

### (1) Stored data in etcd
These are stored data for "heat_templates" in etcd.
```
/config/v2.0/heat_templates/load_balancer_monitoring
{
    "body": {
        "handler": "monitoring_worker", 
        "watch": [], 
        "id": "load_balancer_monitoring", 
        "template_file": "vnf_instance:\n  type: etcd_reader\n  etcd_type: vnf_instance\n  etcd_id: {{ vnf_instance_id }}\nload_balancer_conf:\n  type: etcd_reader\n  etcd_type: load_balancer_conf\n  etcd_id: {{ load_balancer_conf_id }}\nload_balancer:\n  type: router\n  community_name: {{ community_name }}\n  ip: {{ instance_ip }}\n  mibs: [\n    [\"resCpuUsage\", \"1.3.6.1.4.1.5951.4.1.1.41.1\"],\n    [\"resMemUsage\", \"1.3.6.1.4.1.5951.4.1.1.41.2\"],\n    [\"httpTotRequests\", \"1.3.6.1.4.1.5951.4.1.1.48.67\"],\n    [\"tcpCurClientConn\", \"1.3.6.1.4.1.5951.4.1.1.46.2\"],\n    [\"tcpCurServerConn\", \"1.3.6.1.4.1.5951.4.1.1.46.1\"]\n  ]\n  timeout: 180\n  time_between_retries: 3\ndb_mappings:\n  - mapped_id: {{ instance_ip }}\n    relation: 'instance'\n", 
        "parameter_mappings": {
            "community_name": {
                "constant": "LOAD_BALANCER_COMMUNITY"
            }, 
            "vnf_instance_id": {
                "field": "vnf_instance_id"
            }, 
            "load_balancer_id": {
                "field": "id"
            }, 
            "instance_ip": {
                "field": "management_ip", 
                "path": [
                    "vnf_instance_id"
                ]
            }, 
            "load_balancer_conf_id": {
                "field": "load_balancer_conf_id"
            }
        }
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```
You can see the retreiving of "template_file" as "Heat Template".

* etcd_reader
* router

```
vnf_instance:
  type: etcd_reader
  etcd_type: vnf_instance
  etcd_id: {{ vnf_instance_id }}
load_balancer_conf:
  type: etcd_reader
  etcd_type: load_balancer_conf
  etcd_id: {{ load_balancer_conf_id }}
load_balancer:
  type: router
  community_name: {{ community_name }}
  ip: {{ instance_ip }}
  mibs: [
    ["resCpuUsage", "1.3.6.1.4.1.5951.4.1.1.41.1"],
    ["resMemUsage", "1.3.6.1.4.1.5951.4.1.1.41.2"],
    ["httpTotRequests", "1.3.6.1.4.1.5951.4.1.1.48.67"],
    ["tcpCurClientConn", "1.3.6.1.4.1.5951.4.1.1.46.2"],
    ["tcpCurServerConn", "1.3.6.1.4.1.5951.4.1.1.46.1"]
  ]
  timeout: 180
  time_between_retries: 3
db_mappings:
  - mapped_id: {{ instance_ip }}
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
