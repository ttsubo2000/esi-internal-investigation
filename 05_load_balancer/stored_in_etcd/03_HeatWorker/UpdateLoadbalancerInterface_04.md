# Stored data in etcd: Update Loadbalancer Interface

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/load_balancer_confs/1d2023e1-0cf4-48a1-af42-ab32466b2acb
{
    "stack_id": "load_balancer_conf_1d2023e1-0cf4-48a1-af42-ab32466b2acb", 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "stack_status": "UPDATE_COMPLETE", 
    "output": [], 
    "status_reason": "Stack successfully updated", 
    "id": "load_balancer_conf:1d2023e1-0cf4-48a1-af42-ab32466b2acb"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/load_balancer_confs/1d2023e1-0cf4-48a1-af42-ab32466b2acb
{
    "heat_outputs": [], 
    "orchestration_state": "UPDATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/load_balancer_confs/1d2023e1-0cf4-48a1-af42-ab32466b2acb
{
    "state": {
        "worker_state": "MODIFY_COMPLETED", 
        "heat_outputs": "[]", 
        "orchestration_state": "UPDATE_COMPLETE"
    }, 
    "version": 2, 
    "error": ""
}
```
