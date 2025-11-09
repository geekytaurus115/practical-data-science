import numpy as np

GRID_SIZE = 5


def _random_goal():
    return (
        np.random.randint(0, GRID_SIZE),
        np.random.randint(0, GRID_SIZE)
    )


# Goal position initialized randomly but can change on reset
GOAL_POS = _random_goal()

# Load Q-table
q_table = np.load("../q_table.npy")  # Adjust path if needed

# Agent position stored globally
agent_pos = [0, 0]  # Starting at top-left corner

def state_to_index(pos):
    # Convert (row, col) to state index for Q-table lookup
    return pos[0] * GRID_SIZE + pos[1]

def index_to_state(index):
    # Convert index back to (row, col)
    return (index // GRID_SIZE, index % GRID_SIZE)

ACTIONS = ['Up', 'Down', 'Left', 'Right']

def reset_agent():
    global agent_pos, GOAL_POS
    agent_pos = [0, 0]  # Reset to start position
    GOAL_POS = _random_goal()
    return agent_pos, GOAL_POS

def step_agent():
    global agent_pos
    state_idx = state_to_index(agent_pos)
    action_idx = np.argmax(q_table[state_idx])
    action = ACTIONS[action_idx]

    x, y = agent_pos

    if action == 'Up':
        x = max(x - 1, 0)
    elif action == 'Down':
        x = min(x + 1, GRID_SIZE - 1)
    elif action == 'Left':
        y = max(y - 1, 0)
    elif action == 'Right':
        y = min(y + 1, GRID_SIZE - 1)

    new_pos = [x, y]
    agent_pos = new_pos

    done = (tuple(agent_pos) == GOAL_POS)

    return {
        'new_pos': agent_pos,
        'action': action,
        'done': done
    }
