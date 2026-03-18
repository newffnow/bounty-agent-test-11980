"""Simple buggy module for bounty-agent test"""

def add(a, b):
    # FIXED: now adds correctly
    return a + b

if __name__ == "__main__":
    # This should pass after fix
    assert add(2, 3) == 5, "add() is incorrect"