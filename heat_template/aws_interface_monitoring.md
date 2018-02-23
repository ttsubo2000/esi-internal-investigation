# monitoring_template: aws_interface_monitoring
This is monitoring_template of "aws_interface_monitoring" which is provided by gohan via etcd

![scope](../images/esi_interface.003.png)

### (1) Stored data in etcd
These are stored data for "heat_templates" in etcd.
```
/config/v2.0/heat_templates/aws_interface_monitoring
{
    "body": {
        "handler": "monitoring_worker", 
        "watch": [], 
        "id": "aws_interface_monitoring", 
        "template_file": "primary:\n  type: bgp_session\n  host: {{ primary_device_ip }}\n  port: {{ primary_device_port }}\n  login: {{ primary_device_login }}\n  password: {{ primary_device_password }}\n  peer_address: {{ primary_peer_ip }}\n  instance: {{ vrf_name }}\n  timeout: 120\nprimary_uplink:\n  type: logical_port\n  community_name: {{ community_name }}\n  device_ip: {{ primary_device_ip }}\n  name: {{ primary_port }}\nsecondary:\n  type: bgp_session\n  host: {{ secondary_device_ip }}\n  port: {{ secondary_device_port }}\n  login: {{ secondary_device_login }}\n  password: {{ secondary_device_password }}\n  peer_address: {{ secondary_peer_ip }}\n  instance: {{ vrf_name }}\n  timeout: 120\nsecondary_uplink:\n  type: logical_port\n  community_name: {{ community_name }}\n  device_ip: {{ secondary_device_ip }}\n  name: {{ secondary_port }}\ndb_mappings:\n  - mapped_id: {{ primary_device_ip }}-{{ primary_port }}\n    relation: \"primary\"\n  - mapped_id: {{ secondary_device_ip }}-{{ secondary_port }}\n    relation: \"secondary\"\n", 
        "parameter_mappings": {
            "secondary_device_password": {
                "field": "password", 
                "path": [
                    "aws_gw_id", 
                    "downlink_interface_id", 
                    "ha_router_id", 
                    "secondary_router_id"
                ]
            }, 
            "secondary_peer_ip": {
                "nested": [
                    "secondary", 
                    "bgp_peer_ip"
                ]
            }, 
            "primary_peer_ip": {
                "nested": [
                    "primary", 
                    "bgp_peer_ip"
                ]
            }, 
            "secondary_device_port": {
                "field": "ssh_port", 
                "path": [
                    "aws_gw_id", 
                    "downlink_interface_id", 
                    "ha_router_id", 
                    "secondary_router_id"
                ]
            }, 
            "primary_device_ip": {
                "field": "ip", 
                "path": [
                    "aws_gw_id", 
                    "downlink_interface_id", 
                    "ha_router_id", 
                    "primary_router_id"
                ]
            }, 
            "community_name": {
                "constant": "EDGE_ROUTER_COMMUNITY"
            }, 
            "primary_device_password": {
                "field": "password", 
                "path": [
                    "aws_gw_id", 
                    "downlink_interface_id", 
                    "ha_router_id", 
                    "primary_router_id"
                ]
            }, 
            "vrf_name": {
                "field": "vrf_name", 
                "path": [
                    "aws_gw_id"
                ]
            }, 
            "secondary_port": {
                "field": "secondary_logical_uplink_interface_name", 
                "path": [
                    "aws_gw_id"
                ]
            }, 
            "secondary_device_login": {
                "field": "login", 
                "path": [
                    "aws_gw_id", 
                    "downlink_interface_id", 
                    "ha_router_id", 
                    "secondary_router_id"
                ]
            }, 
            "primary_port": {
                "field": "primary_logical_uplink_interface_name", 
                "path": [
                    "aws_gw_id"
                ]
            }, 
            "primary_device_login": {
                "field": "login", 
                "path": [
                    "aws_gw_id", 
                    "downlink_interface_id", 
                    "ha_router_id", 
                    "primary_router_id"
                ]
            }, 
            "primary_device_port": {
                "field": "ssh_port", 
                "path": [
                    "aws_gw_id", 
                    "downlink_interface_id", 
                    "ha_router_id", 
                    "primary_router_id"
                ]
            }, 
            "secondary_device_ip": {
                "field": "ip", 
                "path": [
                    "aws_gw_id", 
                    "downlink_interface_id", 
                    "ha_router_id", 
                    "secondary_router_id"
                ]
            }
        }
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```
You can see the retreiving of "template_file" as "Heat Template".

* bgp_session
* logical_port

```
primary:
  type: bgp_session
  host: {{ primary_device_ip }}
  port: {{ primary_device_port }}
  login: {{ primary_device_login }}
  password: {{ primary_device_password }}
  peer_address: {{ primary_peer_ip }}
  instance: {{ vrf_name }}
  timeout: 120
primary_uplink:
  type: logical_port
  community_name: {{ community_name }}
  device_ip: {{ primary_device_ip }}
  name: {{ primary_port }}
secondary:
  type: bgp_session
  host: {{ secondary_device_ip }}
  port: {{ secondary_device_port }}
  login: {{ secondary_device_login }}
  password: {{ secondary_device_password }}
  peer_address: {{ secondary_peer_ip }}
  instance: {{ vrf_name }}
  timeout: 120
secondary_uplink:
  type: logical_port
  community_name: {{ community_name }}
  device_ip: {{ secondary_device_ip }}
  name: {{ secondary_port }}
db_mappings:
  - mapped_id: {{ primary_device_ip }}-{{ primary_port }}
    relation: "primary"
  - mapped_id: {{ secondary_device_ip }}-{{ secondary_port }}
    relation: "secondary"
```

### (2) Notes for Code of Monitoring-Worker Plugin in esi-worker
* esi-worker/esi_worker/workers/monitoring_worker/resource_plugins/bgp_session.py

```
class BGPSessionPlugin(MonitoringWorkerPlugin):
    TYPE = {
        "bgp_session": "monitor_vpn_interface"
    }

    REQUIRED_PROPS = ["instance", "peer_address", "host", "port", "login",
                      "password"]
    DEFAULT_PROPS = {
        "timeout": 60 * 5,
    }

    @staticmethod
    def get_bgp_summary(manager, instance):
        cmd = """
        <get-bgp-summary-information>
            <exact-instance>{instance}</exact-instance>
        </get-bgp-summary-information>
        """.format(instance=instance)
        return manager.rpc(cmd)

    @staticmethod
    def _retry_on_result(result, props):
        return result != "ESTABLISHED"

    def _get_status_once(self, props):
        rpc_timeout = self._worker_conf.getint('monitoring',
                                               'netconf_rpc_timeout')
        client = NCClient(props["host"], props["port"],
                          props["login"], props["password"],
                          rpc_timeout=rpc_timeout)
        try:
            response = client.execute(self.get_bgp_summary, props["instance"],
                                      max_retries=1)
        except Exception as e:
            logger.debug(e.message)
            raise ResourcePingException()

        for peer in response.find("bgp-information").findall("bgp-peer"):
            if peer.find("peer-address").text == props["peer_address"]:
                state = peer.find("peer-state").text.upper()
                logger.debug(
                    'eBGP peer {} on instance {} returned state "{}"'
                    .format(props["peer_address"], props["instance"], state))
                return state
```

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
