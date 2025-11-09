from flask import Flask, render_template, jsonify, request
import gridworld

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html',
        grid_size=gridworld.GRID_SIZE,
        goal_pos=gridworld.GOAL_POS
    )

@app.route('/reset', methods=['POST'])
def reset():
    agent_pos, goal_pos = gridworld.reset_agent()
    return jsonify({'agent_pos': agent_pos, 'goal_pos': list(goal_pos)})

@app.route('/step', methods=['POST'])
def step():
    result = gridworld.step_agent()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
