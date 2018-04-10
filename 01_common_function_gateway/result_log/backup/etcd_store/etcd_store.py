import argparse
import code
import json
import readline
import zlib

import etcd


def add_to_dict(key, value, data):
    tmp = data
    path = key.split('/')
    name = path.pop()
    for part in path:
        if part not in tmp:
            tmp[part] = {}
        tmp = tmp[part]
    if name in tmp:
        raise ValueError('Duplicate entry for key {}'.format(key))
    tmp[name] = value

def get_subdict(key, data):
    tmp = data
    path = key.split('/')
    for part in path:
        if part:
            tmp = tmp[part]
    return tmp

def get_subdict_for_heatstack(key, data):
    tmp = json.loads(get_subdict(key, data))
    buf = json.loads(tmp["body"])
    for k, v in buf.items():
        if k == "output":
            output = json.loads(v)
            buf[k] = output
        if k == "input":
            input = json.loads(v)
            buf[k] = input
        if k == "template_file":
            template = v.split('\n')
            template_file = "\n".join(template)
            print ("-------- [template_file] -------")
            print ("%s" % template_file)
            print ("-------- [template_file] -------")
    if "template_file" in buf:
        buf["template_file"] = "... snip (Please check the above)"
    tmp["body"] = buf
    return tmp

def parse_message(node):
    if node.dir:
        result = {}
        for child in node.children:
            if child.key == node.key or child.dir:
                continue
            add_to_dict(child.key, child.value, result)
        if result.keys() == ['']:
            return result['']
        return result
    else:
        return node.value

def load_etcd(host='127.0.0.1', port=2379, prefix='/'):
    c = etcd.Client(host, port)
    data = c.read(prefix, recursive=True)
    return parse_message(data)

def store(host, port, filename, path):
    data = load_etcd(host, port, path)
    data = zlib.compress(json.dumps(data))
    with open(filename, 'wb') as f:
        f.write(data)

def load_file(filename):
    with open(filename, 'rb') as f:
        data = zlib.decompress(f.read())
    return json.loads(data)

def interactive(host, port, filename, path):
    data = load_file(filename)
    from pprint import pprint as pp
    vars = globals().copy()
    vars.update(locals())
    shell = code.InteractiveConsole(vars)
    print '** etcd dump available as a dict under "data" global variable **'
    print '**                         enjoy :)                           **'
    shell.interact()

def ls(host, port, filename, path):
    data = load_file(filename)
    for key in get_subdict(path, data):
        print key

def get(host, port, filename, path):
    data = load_file(filename)
    try:
        result = json.loads(get_subdict(path, data))
        print json.dumps(result, indent=4)
    except:
        print json.dumps(get_subdict(path, data), indent=4)

def get_stack(host, port, filename, path):
    data = load_file(filename)
    print json.dumps(get_subdict_for_heatstack(path, data), indent=4)


def _lsr(prefix, data):
    if isinstance(data, dict):
        for k, v in data.iteritems():
            _lsr(prefix + [k], v)
    else:
        print '/'.join(prefix)

def lsr(host, port, filename, path):
    data = load_file(filename)
    data = get_subdict(path, data)
    _lsr([''], data)


ACTIONS = ['lsr', 'ls', 'get', 'get_stack', 'store', 'interactive']
HANDLERS = [lsr, ls, get, get_stack, store, interactive]
HANDLER_MAP = dict(zip(ACTIONS, HANDLERS))
DESCRIPTION = ("Simple script for dumping etcd state and later parsing the dump. \n"
               "There are a few different actions the script can take (based on the action parameter). "
               "Some config options may be ignored for some actions. "
               "Available actions are:\n\n"
               "store - dump current etcd state to a file\n"
               "ls - parse stored file and list specified directory\n"
               "lsr - parse stored file and list specified directory recursively\n"
               "get - parse stored file and retrieve a specific key\n"
               "interactive - parse stored file and start interactive python console with the data available")


def main():
    parser = argparse.ArgumentParser(description=DESCRIPTION, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-i", "--ip_address", help="etcd host (only used for store)",
                        default="127.0.0.1")
    parser.add_argument("-p", "--port", help="etcd port (only used for store)",
                        default=2379, type=int)
    parser.add_argument("-f", "--file", help="name of file to read/write",
                        default="etcd.dump")
    parser.add_argument("action", choices=ACTIONS)
    parser.add_argument("path", help="etcd path", default='/', nargs='?')
    args = parser.parse_args()
    HANDLER_MAP[args.action](args.ip_address, args.port, args.file, args.path)


if __name__ == '__main__':
    main()
