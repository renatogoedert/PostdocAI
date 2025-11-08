# Background

## Problem

The growing pressure to integrate of smart meters and Time-of-Use(ToU) tariffs in Ireland, which have already begun transforming how residential buildings consume electricity. The ToU establishes that the electricity tariffs would vary according to the time of day, dividing into peak (17:00-19:00), day (08:00-23:00), and night (23:00-08:00), which reflects the variation in grid demand and generation costs (ESB Networks, 2024). Additionally, the Commission for Regulation of Utilities (CRU) mandates that all electricity suppliers working in Ireland offer ToU plans, enabling consumers to reduce their electricity costs while improving the grid's sustainability by avoiding the peak periods. (CRU, 2023)

Despite these initiatives, most households still use their high-consumption electrical appliances, like electric vehicle chargers, washing machines, and electric heaters, during peak hours, creating an elevated electricity bill and increasing grid congestion and usage of high-emission power sources during the peak demand (EirGrid, 2024). Whereas there is already a manual form of scheduling, this process demands the user to account for the tariffs times, as well as the personal comfort of multiple people in a household and and their need for an appliance, consequently, most people don't set the manual scheduling or even avoid the smart meters for the extra work needed.

Moreover, according to the EirGrid Smart Grid Dashboard (2024), CO₂ intensity varies by more than 50% between day and night, especially because during the peak hours, there is lower wind generation, making the provider rely on gas-fired plants; by contrast, during night hours, winds are stronger, creating a higher sustainable energy source. Thus, developing a strategy to transfer the load of electricity consumption could reduce residential carbon footprint without requiring a decrease in energy consumption.

## Oportunitty

Based on the previous section, proposing an intelligent scheduling system to balance the electricity load of a household would represent a significant opportunity for both the residential consumers and the electricity providers as for the Ireland carbon-reduction targets.

For the households, the system would enable automated management of smart high-consumption appliances to be shifted to lower-cost, lower-carbon periods without the need for user setup and management, therefore reducing the electricity consumption while keeping comfort and convenience. This reduction of monetary expenditure with the addition of a better use of natural resources could be a motivation point for the households to adopt the system.

For the grid operators and energy suppliers, a widespread adoption of such systems would make possible one of the key objectives for the Commission for Regulation of Utilities Smart Metering Programme, called the demand-side flexibility. This objective focuses on changing the current framework, where the suppliers need to produce as the demand increases, to a framework where households would adjust their electrical consumption accordingly with grid signals such as price, grid conditions, or renewable energy available (CRU, 2023). Furthermore, the adoption of demand-side flexibility would flatten the peak demand, which would also translate to reducing the strain on the infrastructure and reliance on carbon-intensive peaking plants. This would highly enhance grid stability, forecasting accuracy, and progress toward national decarbonization targets.

Overall the solution for this problem would bring economic gains to both households and companies, a possibility that would increase the range of commercial strategies for the product, as it also would have an ethical and social side in helping Ireland advance towards a more sustainable and data-driven energy network. 

# Solution

There are several Artificial Intelligence (AI) methods that can be applied to solve our problem and optimize household electricity consumption under the variables set, ToU, and grid carbon intensity. Each one of the approaches below offers advantages and challenges in interpretability, adaptability and computational power

## Search Based optimisation

This approach can be formulated as a state-space search problem, where each state would represent a partial assignment of appliance start times within a 24-hour period. According to Russell & Norvig (2021), the search-based optimization shines in small to medium-sized problems with stable variable structures and following an explicit objective, in this case, a weighted combination of electricity consumption, carbon emissions, and user comfort penalties. 

Each node in the search tree corresponds to a scheduling decision (assigning a start time to one appliance), and each new step in the task has to respect some constraints, such as time windows, mutual exclusivity, and load limits. These cost constraints should be explicit and auditable, to improve the overall system explainability and transparency.

However, state-space architectures can grow combinatorially with the number of appliances, available time, and constraints in a household. Algorithms like the Uniform-Cost/A* offer optimal solutions but may require substantial memory and computational time as the system grows; of course, adding heuristics (lower bounds from cheapest remaining hours) and decomposition (per-device windows) may mitigate this. 

Another alternative is Greedy Best-First Search, which, because of its focus only on the immediate heuristic, offers faster decisions. Although it does not guarantee the optional schedule, which is particularly problematic for our domain, where the decision can be delayed, but efficiency is critical. Therefore, Greedy is less effective than USC or A*.(Russell & Norvig, 2021)

Following what Russell & Norvig (2021) declares, minimax and any other related game-tree algorithms are not applicable in this context, as the task doesn't involve adversarial decision-making. This is a single-point optimization task where the environment (tariffs and grid intensity) is dynamic but not oppositional; hence, classical search algorithm methods are more appropriate. 

Conversely, local search algorithms would offer an efficient and scalable solution by their iteration principle. Starting from an initial schedule and interacting with its neighbors, it would be able to reduce the objective function, which may include electricity cost, CO₂ emissions, and user penalties.Beyond that,  techniques such as hill climbing or simulated annealing can be applied to guide the process. Although local search is more suited to large search spaces with soft constraints, in addition, they do not guarantee optimality and may require random restarts or hybridization with rule-based filters to ensure feasibility. (Poole & Mackworth, 2017)

## Bayesian networks

A Bayesian network makes use of a graph structure that can capture causal/conditional relationships and do probabilistic calculations to predict high-cost or high-emission periods and supports scheduling decisions under uncertainty. Furthermore, it handles uncertainty naturally (missing and noisy data), and its architecture can learn and adapt to new parameters, though with a higher complexity. (Koller & Friedman, 2009)

A Bayesian network aims to predict conditions, and whereas a probabilistic approach like Bayesian would shine in a system where there is a need to forecast in uncertainty, like the probability of a high price or a change of CO₂ intervals, it does not directly optimize actions; there is no need for such probabilistic calculations.

## Reinforcement Learning

The most adaptable of all approaches among the ones considered, it particularly shines within dynamic environments and changing variables, plus it is capable of learning trade-offs that are almost impossible to hand-code. However, the training of any RL model demands a large dataset and a considerate computational resource for hyperparameter tuning. Despite that, the resulting model is highly efficient on inference. 

Once trained, algorithms like Q-learning or a Deep Q-Network (DQN) can make decisions just with one lookup in a compact neural network. Moreover, these models learn how to maximise cumulative reward by reducing cost and emissions while satisfying user comfort constraints. (Sutton & Barto, 2018) 

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

# References

Commission for Regulation of Utilities (CRU). Smart Metering Programme: Time-of-Use Tariffs and Consumer Information. Dublin: CRU, 2023.

ESB Networks. Guide to Smart Meter Tariff Time Bands. Dublin: ESB Networks, 2024.

EirGrid. Smart Grid Dashboard: Carbon Intensity and System Demand. EirGrid plc, 2024.

Russell, S., & Norvig, P. Artificial Intelligence: A Modern Approach (4th ed.). Pearson, 2021.

Koller, D., & Friedman, N. Probabilistic Graphical Models: Principles and Techniques. MIT Press, 2009.

Goodfellow, I., Bengio, Y., & Courville, A. Deep Learning. MIT Press, 2016.

Sutton, R.S. and Barto, A.G., 2018. Reinforcement Learning: An Introduction. 2nd ed. Cambridge, MA: MIT Press.

Poole, D. & Mackworth, A., 2017. Artificial Intelligence: Foundations of Computational Agents. 2nd ed. Cambridge University Press.

Lapan, M., 2020. Deep Reinforcement Learning Hands-On. 2nd ed. Birmingham: Packt Publishing.