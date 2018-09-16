from .agent import Agent

class PPO(Agent):

    def __init__(self, env=None, device=None):
        Agent.__init__(self, env=env, device=device)

    def get_specs(env=None):
        specs = {
            "type": "ppo_agent",

            "states_preprocessing": {
                "type":"flatten"
            },

            "actions_exploration":{
                "type": "epsilon_decay",
                "initial_epsilon": 1.0,
                "final_epsilon": 0.1,
                "timesteps": 10000
            },

            "update_mode": {
                "unit": "episodes",
                "batch_size": 32,
                "frequency": 32
            },

            "memory": {
                "type": "latest",
                "include_next_states": False,
                "capacity": 50000
            },

            "step_optimizer": {
                "type": "adam",
                "learning_rate": 1e-3
            },

            "discount": 0.99,

            "saver": {
                "directory": None,
                "seconds": 600
            },

            "summarizer": {
                "directory": None,
                "time": 50,
                "labels": []
            }
        }
        return specs
