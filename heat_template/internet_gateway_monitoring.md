# monitoring_template: internet_gateway_monitoring.md
This is monitoring_template of "internet_gateway_monitoring.md" which is provided by gohan via etcd

![scope](../images/esi_interface.003.png)

### (1) Stored data in etcd
These are stored data for "heat_templates" in etcd.
```
/config/v2.0/heat_templates/internet_gateway_monitoring
{
    "body": {
        "handler": "monitoring_worker", 
        "watch": [], 
        "id": "internet_gateway_monitoring", 
        "template_file": "uplink:\n  type: etcd_reader\n  etcd_type: ha_interface\n  etcd_id: {{ uplink_interface_id }}\n  timeout: 120\ndownlink:\n  type: etcd_reader\n  etcd_type: ha_interface\n  etcd_id: {{ downlink_interface_id }}\n  timeout: 120\ncounter_primary:\n  type: kafka_messenger\n  kafka_topic: monitor_igs_counter\n  in_firewall_name: {{ inet_in_filter }}\n  out_firewall_name: {{ inet_out_filter }}\n  counter_name_in_primary: {{ counter_name_in_primary }}\n  counter_name_out_primary: {{ counter_name_out_primary }}\n  counter_name_in_secondary: {{ counter_name_in_secondary }}\n  counter_name_out_secondary: {{ counter_name_out_secondary }}\n  server_username: {{ username }}\n  server_password: {{ password }}\n  server_ssh_port: {{ ssh_port }}\n  primary_server_ip: {{ primary_server_ip }}\n  secondary_server_ip: {{ secondary_server_ip }}\ndb_mappings:\n  - mapped_id: {{ primary_server_ip }}-{{ inet_in_filter }}-{{ counter_name_in_primary }}\n    relation: primary_in\n  - mapped_id: {{ primary_server_ip }}-{{ inet_out_filter }}-{{ counter_name_out_primary }}\n    relation: primary_out\n  - mapped_id: {{ secondary_server_ip }}-{{ inet_in_filter }}-{{ counter_name_in_secondary }}\n    relation: secondary_in\n  - mapped_id: {{ secondary_server_ip }}-{{ inet_out_filter }}-{{ counter_name_out_secondary }}\n    relation: secondary_out\n", 
        "parameter_mappings": {
            "username": {
                "field": "login", 
                "path": [
                    "downlink_interface_id", 
                    "ha_router_id", 
                    "primary_router_id"
                ]
            }, 
            "password": {
                "field": "password", 
                "path": [
                    "downlink_interface_id", 
                    "ha_router_id", 
                    "primary_router_id"
                ]
            }, 
            "counter_name_out_secondary": {
                "concatenate": [
                    {
                        "field": "vrf_name"
                    }, 
                    {
                        "constant": "_OUT"
                    }
                ]
            }, 
            "inet_out_filter": {
                "field": "inet_out_filter", 
                "path": [
                    "internet_service_id"
                ]
            }, 
            "ssh_port": {
                "field": "ssh_port", 
                "path": [
                    "downlink_interface_id", 
                    "ha_router_id", 
                    "primary_router_id"
                ]
            }, 
            "downlink_interface_id": {
                "field": "downlink_interface_id"
            }, 
            "primary_server_ip": {
                "field": "ip", 
                "path": [
                    "downlink_interface_id", 
                    "ha_router_id", 
                    "primary_router_id"
                ]
            }, 
            "counter_name_in_secondary": {
                "concatenate": [
                    {
                        "field": "vrf_name"
                    }, 
                    {
                        "constant": "_IN"
                    }
                ]
            }, 
            "counter_name_in_primary": {
                "concatenate": [
                    {
                        "field": "vrf_name"
                    }, 
                    {
                        "constant": "_IN"
                    }
                ]
            }, 
            "secondary_server_ip": {
                "field": "ip", 
                "path": [
                    "downlink_interface_id", 
                    "ha_router_id", 
                    "secondary_router_id"
                ]
            }, 
            "uplink_interface_id": {
                "field": "associated_uplink_id"
            }, 
            "inet_in_filter": {
                "field": "inet_in_filter", 
                "path": [
                    "internet_service_id"
                ]
            }, 
            "counter_name_out_primary": {
                "concatenate": [
                    {
                        "field": "vrf_name"
                    }, 
                    {
                        "constant": "_OUT"
                    }
                ]
            }
        }
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```
You can see the retreiving of "template_file" as "Heat Template".

* etcd_reader
* kafka_messenger

```
uplink:
  type: etcd_reader
  etcd_type: ha_interface
  etcd_id: {{ uplink_interface_id }}
  timeout: 120
downlink:
  type: etcd_reader
  etcd_type: ha_interface
  etcd_id: {{ downlink_interface_id }}
  timeout: 120
counter_primary:
  type: kafka_messenger
  kafka_topic: monitor_igs_counter
  in_firewall_name: {{ inet_in_filter }}
  out_firewall_name: {{ inet_out_filter }}
  counter_name_in_primary: {{ counter_name_in_primary }}
  counter_name_out_primary: {{ counter_name_out_primary }}
  counter_name_in_secondary: {{ counter_name_in_secondary }}
  counter_name_out_secondary: {{ counter_name_out_secondary }}
  server_username: {{ username }}
  server_password: {{ password }}
  server_ssh_port: {{ ssh_port }}
  primary_server_ip: {{ primary_server_ip }}
  secondary_server_ip: {{ secondary_server_ip }}
db_mappings:
  - mapped_id: {{ primary_server_ip }}-{{ inet_in_filter }}-{{ counter_name_in_primary }}
    relation: primary_in
  - mapped_id: {{ primary_server_ip }}-{{ inet_out_filter }}-{{ counter_name_out_primary }}
    relation: primary_out
  - mapped_id: {{ secondary_server_ip }}-{{ inet_in_filter }}-{{ counter_name_in_secondary }}
    relation: secondary_in
  - mapped_id: {{ secondary_server_ip }}-{{ inet_out_filter }}-{{ counter_name_out_secondary }}
    relation: secondary_out
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

* esi-worker/esi_worker/workers/monitoring_worker/resource_plugins/kafka_messenger.py

```
class KafkaMessengerPlugin(MonitoringWorkerPlugin):
    TYPE = {
        "kafka_messenger": ""
    }

    REQUIRED_PROPS = ["kafka_topic"]

    def get_status(self, props):
        pass
```

### (3) Memo for myself ...
