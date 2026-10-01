import json


def new_game():
    return {'count': 0, 'closed': False, 'nodes': {1: True, 2: True}, 'edges': {(1, 2): 5}, 'items': [], 'src': 10, 'dst': 0, 'events': {1: True}, 'paused': False, 'balance': 10, 'snapshot': 5, 'value': 5, 'log': [], 'settled': False}

def bug_8(state):
    state["count"] = 0
    return True

def bug_15(state):
    if state["closed"]:
        return False
    return True

def bug_22(state):
    return (1, 2) in state["edges"]

def bug_29(state):
    state["nodes"].pop(1, None)
    for edge in [key for key in state["edges"] if 1 in key]:
        state["edges"].pop(edge, None)
    return True

def bug_6(state):
    return len(state["items"])

def bug_13(state):
    state["src"] -= 5
    state["dst"] += 5
    return True

def bug_20(state):
    state["events"].pop(1, None)
    return True

def bug_27(state):
    return any(src == dst for src, dst in state["edges"])

def bug_4(state):
    if state["paused"]:
        return False
    return True

def bug_11(state):
    if state["balance"] < 20:
        return False
    state["balance"] -= 20
    return True

def bug_30(state):
    if any(status == "failed" for _, status in state.get("log", [])):
        state["value"] = state["snapshot"]
        return False
    state["value"] = state["snapshot"]
    return True

def bug_31(state):
    if state["settled"]:
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
