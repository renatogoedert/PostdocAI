# Selected solution

After thorough consideration of all algorithms stated before, the two most
applicable to the problem were Search (A*) and Reinforcement Learning. As the system aims to be applied in multiple houses, the computation resource needed to train a model would be divided by multiple users, making it more viable, and, combined with the probability of an expansion with energy suppliers and grid providers to create a data-driven system, reinforcement learning was chosen as the most suitable one, as its adaptive paradigm would make it perfect to receive and adapt to the data of the grid in an eventual demand-side flexibility system.

## Archtecture

The system would be designed as a Markov Decision Process (MDP). Sutton and Barto (2018) explain this system as a mathematical framework for sequential decision-making problems in environments where outcomes are partly under control and partly random. They are divided into:

S – a finite set of states, representing all possible configurations the environment can be in.

A – a finite set of actions available to the agent in each state.

P(s′|s, a) – a transition probability function, which defines the probability of moving to state s′ given that the agent took action a in state s.

R(s, a) – a reward function, specifying the immediate numerical reward received after taking action a in state s.

γ – a discount factor, 0 ≤ 𝛾 ≤ 1, which determines how much the agent values future rewards compared to immediate ones.

On this, the agent would learn a policy π(a∣s) that maximizes the expected cumulative reward over time; the state would include time, appliance status, tariff band, and carbon intensity; the actions would be selecting an appliance start time,; finally the reward would penalize/reward costs, emissions, and comfort violations.

However, Lapan (2020) brings to attention that the rewarding and penalizing should be well designed, as if the AI gets a sequence of punishments, it could get stuck, as it would learn that no matter what it does, it would get punished. So techniques like giving rewards per progress and offering relative rewards would be beneficial to a proper learning phase. With that in mind, the proposed reward function is

Reward=−α⋅Cost−β⋅Emissions−γ⋅Penaltycomfort​+δ⋅ApplianceBonus

The reward weights (α, β, γ, and δ) should be predefined for training but also may be adjusted during iterations of the training phase to allow improvement of the policy.

## Algorithms

One of the main expectations for this system would be a fast inference capability, even when applied to computationally constrained hardware. Therefore, among the algorithms researched, the ones that use the Q-value, Q-learning and Deep Q-Network, were selected for a more in-depth analysis due to their efficiency and simplicity.

The foundation of both of these algorithms is the Q-value function, which calculates the expected cumulative reward of an agent, considering starting in a state s, taking an action a, and following one particular policy afterwards. (Sutton and Barto, 2018)

- Q-learning: This algorithm creates a Q-table that stores the values of each pair (state and action). During inference the model performs a simple lookup to find, in the table, the highest Q value and select the related actions. This is a lightweight and effective solution for low-dimensional states problems

- Deep Q-Network (DQN): DQN replaces the Q-table with a small neural network that approximates the q-values using deep learning techniques. This paradigm change permits the algorithm to handle larger state spaces where a simple table is impractical; because of that, DQNs are suited to systems with more state variables while still focusing on simplicity.

## Data Sources

As this own report arises, RL AI systems demand a substantial amount of data for training. Fortunately, much of the data sources were already collected and publicly available for training. Not just that, but companies like energy suppliers, grid operators, and appliance builders usually offer high-structured, high-precision data, removing from the solution development: a heavy data wrangling process. The data source for the system would be

- Tariff data: ESB Networks and Electric Ireland documentation on Time-of-Use tariffs
- Carbon intensity: EirGrid Smart Grid Dashboard and published CO₂ emission datasets.
- Appliance usage patterns: Derived from demand-side management literature and residential energy surveys

# Implemetation

The report would consissts on only the impementation of the Ai system, all extra hardware is not be going to be taken into consideration. For this implementation would be considered both technical and human resourses, It also would focus on the development on the MVP for proving the capability of the AI as a early comersalisation and to develop the estrategies with the elecirity supliers and grid operadors companies

Human Resources:

| Role           | Description                                                                             | Estimated Time|
|----------------|-----------------------------------------------------------------------------------------|---------------|
| AI Engineer    | Develop and train the Ai models, as handles data preprocessing and hyperparameter tuning| 210hours      |
| Data Analist   | Curates and validates training datasets from public sources                             |  40hours      |
| FS Developer   | Build the interface and Integrate the model into a usable software                      | 140hours      |
| Project Manager| Oversees progress, documentation and ethical compliance                                 |  40hours      |

For calculate the Technical resources, most of the tools and data for the traning and developing are open source, inferring no costs, the deployment in a big cloud provider is cents per day, so we are going to consider 100 euros to keep it running for months without no issue. For the traning of the algorithm we will consider:

- Input: time, tarif band, carbon intensity, appliance status - 128 features 
- Output: time slots - 48
- Hidden Layers: 3-4 layers
- Neurons per Layer: 128-256 neurons




Technical resources 
| Role                | Description                                                                        | Estimated Cost|
|----------------------|-----------------------------------------------------------------------------------|---------------|
| Computational Infra  | Access to a GPU instance(Google Colab Pro or AWS) for model training and testing  | 210hours      |
| Software and tools   | Python, TensorFlows/Pytorch, Hugging Face, OpenAI Gym                             |  Free         |
| Data Sources         | EirGrid Dashboard, ESb networks tarrif data, and apliances power comsuption       |  Free         |
| Prototype Hosting    | Optional cloud hosting of the MVP (Aws, Azure or Google Cloud)                    |  €100         |
