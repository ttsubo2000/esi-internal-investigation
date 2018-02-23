# heat_template: qos_option_aws
This is heat_template of "qos_option_aws" which is provided by gohan via etcd

![scope](../images/esi_interface.002.png)

### (1) Stored data in etcd
These are stored data for "heat_templates" in etcd.
```
/config/v2.0/heat_templates/qos_option_aws
{
    "body": {
        "handler": "heat_worker", 
        "watch": [], 
        "id": "qos_option_aws", 
        "template_file": "heat_template_version: 2013-05-23\n\ndescription: >\n  QoS Option\n\nparameters:\n  primary_device_ip:\n    description: Ip address that will be used to establish ssh connection to the Primary Device.\n    label: Ip address of the device.\n    type: string\n  primary_device_port:\n    description: Port that will be used to establish ssh connection to the Primary Device.\n    label: Port of the ssh connection.\n    type: number\n  primary_device_username:\n    description: Name of the user which will be used to log onto the Primary Device.\n    label: User name to log on to device.\n    type: string\n  primary_device_password:\n    description: Password of the user which will be used to log onto the Primary Device.\n    label: Users password.\n    type: string\n  secondary_device_ip:\n    description: Ip address that will be used to establish ssh connection to the Secondary Device.\n    label: Ip address of the device.\n    type: string\n  secondary_device_port:\n    description: Port that will be used to establish ssh connection to the Secondary Device.\n    label: Port of the ssh connection.\n    type: number\n  secondary_device_username:\n    description: Name of the user which will be used to log onto the Secondary Device.\n    label: User name to log on to device.\n    type: string\n  secondary_device_password:\n    description: Password of the user which will be used to log onto the Secondary Device.\n    label: Users password.\n    type: string\n  incoming_policer_name:\n    description: Name of created incoming policer\n    label: Incoming policer name\n    type: string\n  incoming_policer_config:\n    description: Configuration of incoming policer\n    label: Incoming policer config\n    type: string\n  outgoing_policer_name:\n    description: Name of created outgoing policer\n    label: Outgoing policer name\n    type: string\n  outgoing_policer_config:\n    description: Configuration of outgoing policer\n    label: Outgoing policer config\n    type: string\n  neighbour_prefix:\n    description: Name of prefix list used to specify traffic source/destination\n    label: Neighbour prefix\n    type: string\nresources:\n{% set forewarding_class = be_forwarding_class if qos_type == \"besteffort\" else ga_forwarding_class %}\n{% for device in [\"primary\", \"secondary\"] %}\n  netconf_configure_{{ device }}:\n    type: OS::Contrail::NetconfNamedConfigs\n    properties:\n      lock_timeout: 3000\n      device_ip:\n        get_param: {{ device }}_device_ip\n      password:\n        get_param: {{ device }}_device_password\n      port:\n        get_param: {{ device }}_device_port\n      username:\n        get_param: {{ device }}_device_username\n      configs:\n      - config:\n          { get_param: incoming_policer_config }\n        path:\n          - config_type: tag\n            xml_type: tag\n            tag: firewall\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: three-color-policer\n            name: { get_param: incoming_policer_name }\n      - config:\n          { get_param: outgoing_policer_config }\n        path:\n          - config_type: tag\n            xml_type: tag\n            tag: firewall\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: policer\n            name: { get_param: outgoing_policer_name }\n      - config:\n          str_replace:\n            params:\n              $PREFIX:\n                get_param: neighbour_prefix\n              $CLASS:\n                {% if jinja_type == \"besteffort\" %} {{ jinja_be_forwarding_class }} {% else %} {{ jinja_ga_forwarding_class }} {% endif %}\n              $POLICER_NAME:\n                get_param: incoming_policer_name\n            template: |\n               term bgp-accept {\n                   from {\n                       source-prefix-list {\n                           $PREFIX;\n                       }\n                       protocol tcp;\n                       port bgp;\n                   }\n                   then accept;\n               }\n               term vrrp-accept {\n                   from {\n                       source-prefix-list {\n                           $PREFIX;\n                       }\n                       protocol vrrp;\n                   }\n                   then policer 10K-RE;\n                   then accept;\n               }\n               term qos {\n                   then {\n                       three-color-policer {\n                           {% if jinja_type == \"besteffort\" %}two-rate{% else %}single-rate{% endif %} $POLICER_NAME;\n                       }\n                       forwarding-class $CLASS;\n                       accept;\n                   }\n               }\n        path:\n          - config_type: tag\n            xml_type: tag\n            tag: firewall\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: filter\n            name:\n              str_replace:\n                params:\n                  $NAME:\n                    get_param: incoming_policer_name\n                template: |\n                  FILTER_$NAME\n      - config:\n          str_replace:\n            params:\n              $PREFIX:\n                get_param: neighbour_prefix\n              $POLICER_NAME:\n                get_param: outgoing_policer_name\n            template: |\n               term bgp-accept {\n                   from {\n                       destination-prefix-list {\n                           $PREFIX;\n                       }\n                       protocol tcp;\n                       port bgp;\n                   }\n                   then accept;\n               }\n               term vrrp-accept {\n                   from {\n                       protocol vrrp;\n                   }\n                   then accept;\n               }\n               term policer {\n                   then {\n                       policer $POLICER_NAME;\n                       accept;\n                   }\n               }\n        path:\n          - config_type: tag\n            xml_type: tag\n            tag: firewall\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: filter\n            name:\n              str_replace:\n                params:\n                  $NAME:\n                    get_param: outgoing_policer_name\n                template: |\n                  FILTER_$NAME\n{% endfor %}\n", 
        "parameter_mappings": {
            "secondary_device_password": "Fha_router+ha_router_id:edge_router+secondary_router_id:password", 
            "jinja_be_forwarding_class": "Faws_service+aws_service_id:be_forwarding_class", 
            "primary_device_password": "Fha_router+ha_router_id:edge_router+primary_router_id:password", 
            "jinja_ga_forwarding_class": "Faws_service+aws_service_id:ga_forwarding_class", 
            "incoming_policer_name": "Pincoming_policer_name", 
            "jinja_type": "Pqos_type", 
            "secondary_device_port": "Fha_router+ha_router_id:edge_router+secondary_router_id:ssh_port", 
            "primary_device_ip": "Fha_router+ha_router_id:edge_router+primary_router_id:ip", 
            "heat_timeout": "C60", 
            "outgoing_policer_config": "Poutgoing_policer_config", 
            "incoming_policer_config": "Pincoming_policer_config", 
            "outgoing_policer_name": "Poutgoing_policer_name", 
            "neighbour_prefix": "Faws_service+aws_service_id:neighbour_prefix", 
            "secondary_device_username": "Fha_router+ha_router_id:edge_router+secondary_router_id:login", 
            "primary_device_port": "Fha_router+ha_router_id:edge_router+primary_router_id:ssh_port", 
            "secondary_device_ip": "Fha_router+ha_router_id:edge_router+secondary_router_id:ip", 
            "primary_device_username": "Fha_router+ha_router_id:edge_router+primary_router_id:login"
        }
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```
You can see the retreiving of "template_file" as "Heat Template".

OS::Contrail::NetconfNamedConfigs

```
heat_template_version: 2013-05-23

description: >
  QoS Option

parameters:
  primary_device_ip:
    description: Ip address that will be used to establish ssh connection to the Primary Device.
    label: Ip address of the device.
    type: string
  primary_device_port:
    description: Port that will be used to establish ssh connection to the Primary Device.
    label: Port of the ssh connection.
    type: number
  primary_device_username:
    description: Name of the user which will be used to log onto the Primary Device.
    label: User name to log on to device.
    type: string
  primary_device_password:
    description: Password of the user which will be used to log onto the Primary Device.
    label: Users password.
    type: string
  secondary_device_ip:
    description: Ip address that will be used to establish ssh connection to the Secondary Device.
    label: Ip address of the device.
    type: string
  secondary_device_port:
    description: Port that will be used to establish ssh connection to the Secondary Device.
    label: Port of the ssh connection.
    type: number
  secondary_device_username:
    description: Name of the user which will be used to log onto the Secondary Device.
    label: User name to log on to device.
    type: string
  secondary_device_password:
    description: Password of the user which will be used to log onto the Secondary Device.
    label: Users password.
    type: string
  incoming_policer_name:
    description: Name of created incoming policer
    label: Incoming policer name
    type: string
  incoming_policer_config:
    description: Configuration of incoming policer
    label: Incoming policer config
    type: string
  outgoing_policer_name:
    description: Name of created outgoing policer
    label: Outgoing policer name
    type: string
  outgoing_policer_config:
    description: Configuration of outgoing policer
    label: Outgoing policer config
    type: string
  neighbour_prefix:
    description: Name of prefix list used to specify traffic source/destination
    label: Neighbour prefix
    type: string
resources:
{% set forewarding_class = be_forwarding_class if qos_type == "besteffort" else ga_forwarding_class %}
{% for device in ["primary", "secondary"] %}
  netconf_configure_{{ device }}:
    type: OS::Contrail::NetconfNamedConfigs
    properties:
      lock_timeout: 3000
      device_ip:
        get_param: {{ device }}_device_ip
      password:
        get_param: {{ device }}_device_password
      port:
        get_param: {{ device }}_device_port
      username:
        get_param: {{ device }}_device_username
      configs:
      - config:
          { get_param: incoming_policer_config }
        path:
          - config_type: tag
            xml_type: tag
            tag: firewall
          - config_type: named_tag
            xml_type: named_tag
            tag: three-color-policer
            name: { get_param: incoming_policer_name }
      - config:
          { get_param: outgoing_policer_config }
        path:
          - config_type: tag
            xml_type: tag
            tag: firewall
          - config_type: named_tag
            xml_type: named_tag
            tag: policer
            name: { get_param: outgoing_policer_name }
      - config:
          str_replace:
            params:
              $PREFIX:
                get_param: neighbour_prefix
              $CLASS:
                {% if jinja_type == "besteffort" %} {{ jinja_be_forwarding_class }} {% else %} {{ jinja_ga_forwarding_class }} {% endif %}
              $POLICER_NAME:
                get_param: incoming_policer_name
            template: |
               term bgp-accept {
                   from {
                       source-prefix-list {
                           $PREFIX;
                       }
                       protocol tcp;
                       port bgp;
                   }
                   then accept;
               }
               term vrrp-accept {
                   from {
                       source-prefix-list {
                           $PREFIX;
                       }
                       protocol vrrp;
                   }
                   then policer 10K-RE;
                   then accept;
               }
               term qos {
                   then {
                       three-color-policer {
                           {% if jinja_type == "besteffort" %}two-rate{% else %}single-rate{% endif %} $POLICER_NAME;
                       }
                       forwarding-class $CLASS;
                       accept;
                   }
               }
        path:
          - config_type: tag
            xml_type: tag
            tag: firewall
          - config_type: named_tag
            xml_type: named_tag
            tag: filter
            name:
              str_replace:
                params:
                  $NAME:
                    get_param: incoming_policer_name
                template: |
                  FILTER_$NAME
      - config:
          str_replace:
            params:
              $PREFIX:
                get_param: neighbour_prefix
              $POLICER_NAME:
                get_param: outgoing_policer_name
            template: |
               term bgp-accept {
                   from {
                       destination-prefix-list {
                           $PREFIX;
                       }
                       protocol tcp;
                       port bgp;
                   }
                   then accept;
               }
               term vrrp-accept {
                   from {
                       protocol vrrp;
                   }
                   then accept;
               }
               term policer {
                   then {
                       policer $POLICER_NAME;
                       accept;
                   }
               }
        path:
          - config_type: tag
            xml_type: tag
            tag: firewall
          - config_type: named_tag
            xml_type: named_tag
            tag: filter
            name:
              str_replace:
                params:
                  $NAME:
                    get_param: outgoing_policer_name
                template: |
                  FILTER_$NAME
{% endfor %}
```

### (2) Notes for Code of Heat Plugin in contrail-heat
* contrail-heat/contrail_heat/resources/netconf_named.py

```
class ContrailNetconfNamedConfigs(netconf.ContrailNetconf):

    ConfigEntity = collections.namedtuple('ConfigEntity',
                                          'path config')

    PROPERTIES = (
        DEVICE_IP, USERNAME, PASSWORD, PORT, CONFIGS, ON_UPDATE, LOCK_TIMEOUT
    ) = (
        'device_ip', 'username', 'password', 'port', 'configs', 'on_update',
        'lock_timeout'
    )

    CONFIG_KEYS = (PATH, CONFIG, ADDITIONAL_COMMANDS) = (
        'path', 'config', 'additional_commands')

    PATH_KEYS = (
        CONFIG_TYPE, XML_TYPE, TAG, NAME
    ) = (
        "config_type", "xml_type", "tag", "name",
    )

    path_schema = properties.Schema(
        properties.Schema.MAP,
        schema={
            CONFIG_TYPE: properties.Schema(
                properties.Schema.STRING,
                _('Type of node in juniper cli format'),
                constraints=[
                    constraints.AllowedValues(['tag', 'named_tag', 'name']),
                ],
                default='tag'
            ),
            XML_TYPE: properties.Schema(
                properties.Schema.STRING,
                _('Type of node in netconf xml'),
                constraints=[
                    constraints.AllowedValues(['tag', 'named_tag']),
                ],
                default='tag'
            ),
            TAG: properties.Schema(
                properties.Schema.STRING,
                _('Tag value for path'),
                default=''
            ),
            NAME: properties.Schema(
                properties.Schema.STRING,
                _('Name value for path'),
                default=''
            ),
        })

    properties_schema = {
        DEVICE_IP: properties.Schema(
            properties.Schema.STRING,
            _('Ip address of the device.'),
            required=True,
        ),
        USERNAME: properties.Schema(
            properties.Schema.STRING,
            _('User name to log on to device.'),
            required=True,
            update_allowed=True
        ),
        PASSWORD: properties.Schema(
            properties.Schema.STRING,
            _('Users password.'),
            required=True,
            update_allowed=True
        ),
        PORT: properties.Schema(
            properties.Schema.INTEGER,
            _('Port of the ssh connection.'),
            default=22,
            update_allowed=True
        ),
        ON_UPDATE: properties.Schema(
            properties.Schema.STRING,
            _("JUNOS action run on update. "
              "Default action is to delete old config "
              "and apply new. "
              "Rest of them are action passed to netconf as "
              "action parameter on load_configuration."),
            constraints=[
                constraints.AllowedValues(
                    ['delete-and-create', 'merge', 'override',
                     'replace', 'update']),
            ],
            default='delete-and-create',
            update_allowed=False
        ),
        CONFIGS: properties.Schema(
            properties.Schema.LIST,
            _('A list of named config entities (ex. interfaces, '
              'routing-policies, etc.)'),
            schema=properties.Schema(
                properties.Schema.MAP,
                schema={
                    PATH: properties.Schema(
                        properties.Schema.LIST,
                        _('Path of config in config tree.'),
                        required=True,
                        schema=path_schema,
                        update_allowed=False,
                    ),
                    CONFIG: properties.Schema(
                        properties.Schema.STRING,
                        _('Config in junos cli format.'),
                        required=True,
                        update_allowed=True,
                    ),
                    ADDITIONAL_COMMANDS: properties.Schema(
                        properties.Schema.STRING,
                        _("Additional JUNOS CLI commands to"
                          " run after create."),
                        required=False,
                    ),
                }
            ),
            required=True,
            update_allowed=True
        ),
        LOCK_TIMEOUT: properties.Schema(
            properties.Schema.INTEGER,
            _('Timeout on trying to get the config lock in seconds.'),
            default=120,
            update_allowed=True
        ),
    }

    XML_EDIT_CONFIG = '''
                 <edit-config>
                   <target>
                     <candidate/>
                   </target>
                   <default-operation>none</default-operation>
                   <config>
                     <configuration>
                       {config}
                     </configuration>
                   </config>
                 </edit-config>'''

    update_allowed_keys = ('Properties',)

    # templates for building xml and config strings
    _xml_open_templates = {
        "tag": "<{tag}{operation}>",
        "named_tag": """<{tag}{operation}>
        <name><![CDATA[{name}]]></name>""",
    }
    _xml_close_templates = collections.defaultdict(lambda: "</{tag}>")

    _config_templates = {
        "tag": "{tag}",
        "name": "{name}",
        "named_tag": "{tag} {name}",
    }

    class TreeNode(object):
        def __init__(self, path_element):
            self.path_element = path_element
            self.children = []
            self.value = None

    NOT_FOUND_PATTERNS = [
        re.compile("^Referenced filter '.+' is not defined$", re.I),
        re.compile("^statement not found: .+$", re.I)]

    def _is_not_found_error(self, rpc_error):
        message = rpc_error.message
        for pattern in self.NOT_FOUND_PATTERNS:
            if pattern.search(message) is not None:
                return True
        return False

    def _build_config_tree(self, configs):
        root = []
        for conf in configs:
            curr_node = root
            new_node = None
            if not conf.path:
                raise ValueError(_("Tree for config is empty"))
            for path_element in conf.path:
                found = False
                for node in curr_node:
                    if node.path_element == path_element:
                        curr_node = node.children
                        found = True
                        break
                if not found:
                    new_node = self.TreeNode(path_element)
                    curr_node.append(new_node)
                    curr_node = new_node.children
            if not new_node:
                raise ValueError(_("You are trying to overwrite other config "
                                 "from this stack."))
            new_node.value = conf.config
        return root

    def _build_config_string(self, tree):
        result = []
        for node in tree:
            path_el = node.path_element
            result.append(self._config_templates[
                path_el["config_type"]].format(tag=path_el.get("tag"),
                                               name=path_el.get("name")))
            if node.children:
                if node.value:
                    # we don't allow this as it will make deletion harder
                    # and it may be even easier to just
                    # insert child's config in parent's config
                    raise ValueError(_(
                        "You can't add a child to the parent created "
                        "in this stack. If you need this "
                        "insert child config as "
                        "string in parent config."))
                result.append(' {{\n{} }}\n'.format(
                              self._build_config_string(node.children)))
            elif node.value:
                result.append(' {{\n{} }}\n'.format(node.value))
            else:
                # no children or value - we don't need to open scope,
                # just add statement
                result.append(";\n")
        return ''.join(result)

    def _build_xml_string(self, tree, operation=""):
        result = []
        for node in tree:
            path_el = node.path_element
            template_args = collections.defaultdict(
                str, tag=path_el.get("tag"), name=path_el.get("name"))
            if not node.children:
                template_args["operation"] = operation
            result.append(string.Formatter().vformat(
                self._xml_open_templates[path_el["xml_type"]], (),
                template_args))
            if node.children:
                result.append(self._build_xml_string(node.children, operation))
            result.append(string.Formatter().vformat(
                self._xml_close_templates[path_el["xml_type"]], (),
                template_args))
            LOG.info(result)
        return ''.join(result)

    def _create_config(self):
        configs = self._get_configs()
        tree = self._build_config_tree(configs)
        return self._build_config_string(tree)

    def _create_delete_rpcs(self):
        configs = self._get_configs()
        xmls = []
        for config in configs:
            tree = self._build_config_tree([config])
            xmls.append(self._build_xml_string(tree, " operation=\"delete\""))
        rpcs = []
        for xml in xmls:
            rpcs.append(self.XML_EDIT_CONFIG.format(config=xml))
        return rpcs

    def _get_configs(self):
        return [self.ConfigEntity(p[self.PATH],
                                  p[self.CONFIG])
                for p in self.properties[self.CONFIGS]]

    def _execute_additional_commands(self, manager):
        cmds = '\n'.join(p[self.ADDITIONAL_COMMANDS]
                         for p in self.properties[self.CONFIGS]
                         if bool(p[self.ADDITIONAL_COMMANDS]))
        if cmds:
            manager.load_configuration(target="candidate",
                                    config=cmds,
                                    format='text',
                                    action="set")

    def _create(self, manager, config, action='merge'):
        # merge is default action for load_configuration

        LOG.info('Constructed netconf create payload for %s: %s',
                 self.properties[self.DEVICE_IP], config)
        manager.load_configuration(target="candidate",
                                   action=action,
                                   config=config,
                                   format='text')
        self._execute_additional_commands(manager)

    def _delete(self, manager, configs):
        LOG.info('Constructed netconf delete rpcs %s: %s',
                 self.properties[self.DEVICE_IP], '\n'.join(configs))
        for config in configs:
            try:
                manager.rpc(config)
            except RPCError as e:
                if not self._is_not_found_error(e):
                    raise
                else:
                    LOG.warn("Resource not found for config: \n %s \n."
                             "  Skipping...", config)

    def _update(self, manager, delete_configs, new_config):
        if self.properties[self.ON_UPDATE] == 'delete-and-create':
            LOG.debug("Running delete-and-create.")
            self._delete(manager, delete_configs)
            self._create(manager, new_config)
        else:
            LOG.debug("Running update with action %s",
                      self.properties[self.ON_UPDATE])
            self._create(manager, new_config,
                         action=self.properties[self.ON_UPDATE])

    def handle_create(self):
        self.resource_id_set(str(uuid.uuid4()))
        config = self._create_config()
        self._client.execute_in_transaction(self._create, config)

    def handle_update(self, json_snippet=None, tmpl_diff=None, prop_diff=None):
        if not prop_diff:
            LOG.info("No update required.")
            return

        # create cmd to remove old config
        delete_configs = self._create_delete_rpcs()

        self.properties = json_snippet.properties(self.properties_schema,
                                                  self.context)

        # create updated config
        new_config = self._create_config()
        # execute delete and create with single commit
        self._client.execute_in_transaction(
                self._update, delete_configs, new_config)

    def handle_delete(self):
        configs = self._create_delete_rpcs()
        self._client.execute_in_transaction(self._delete, configs)


def resource_mapping():
    return {
        'OS::Contrail::NetconfNamedConfigs': ContrailNetconfNamedConfigs,
    }
```

### (3) Memo for myself ...
* It looks that master branch is not used in repository of "contrail-heat".
* The codes of processing via netconf is included in repository of "esi-python-modules".

![scope](../memo/Intenal_processing_fornetconf.001.png)