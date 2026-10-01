import json


def new_game():
    return {'count': 0, 'closed': False, 'nodes': {1: True, 2: True}, 'edges': {(1, 2): 5}, 'items': [], 'src': 10, 'dst': 0, 'events': {1: True}, 'paused': False, 'balance': 10, 'snapshot': 5, 'value': 5, 'log': [], 'settled': False}

def bug_8(state):
    state["count"] = 0
    return True

def bug_15(state):
    if state.get("closed"):
        return False
    return True

def bug_22(state):
    nodes = state.get("nodes", {})
    return any(u in nodes and v in nodes for u, v in state.get("edges", {}))

def bug_29(state):
    state["nodes"].pop(1, None)
    state["edges"] = {
        (u, v): w for (u, v), w in state["edges"].items() if u != 1 and v != 1
    }
    return True

def bug_6(state):
    return len(state["items"])

def bug_13(state):
    amount = 5
    if state["src"] < amount:
        return False
    state["src"] -= amount
    state["dst"] += amount
    return True

def bug_20(state):
    state["events"].pop(1, None)
    return True

def bug_27(state):
    nodes = state.get("nodes", {})
    if any(u == v for u, v in state.get("edges", {})):
        return False
    candidate = state.get("pending_edge")
    if candidate is not None and candidate[0] == candidate[1]:
        return False
    if not nodes or candidate is None:
        return False
    return True

def bug_4(state):
    if state.get("paused"):
        return False
    return True

def bug_11(state):
    amount = 20
    if state["balance"] < amount:
        return False
    state["balance"] -= amount
    return True

def bug_30(state):
    if any(op == "op" and result == "failed" for op, result in state.get("log", [])):
        state["value"] = state["snapshot"]
        return False
    state["snapshot"] = state["value"]
    return True

def bug_31(state):
    if state.get("settled"):
        return False
    return True

def main():
    print("命令: run/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()
