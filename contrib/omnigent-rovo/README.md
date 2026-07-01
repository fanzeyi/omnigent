# Rovo Community Harness

Optional Rovo Dev harness support for Omnigent from this source checkout.

Install the local package path to enable `harness: rovo` and `harness:
rovo-cli`.

```bash
uv pip install -e contrib/omnigent-rovo
```

Rovo Dev itself is launched through `acli rovodev acp`; authenticate with
Atlassian's CLI before running an Omnigent session.
