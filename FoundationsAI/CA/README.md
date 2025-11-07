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

This approach can be formulated as a state-space search problem, where each state would represent a partial assignment of appliance start times within a 24-hour period. According to Tussell & Norvig (2021), the search-based optimization shines in small to medium-sized problems with stable variable structures and following an explicit objective, in this case, a weighted combination of electricity consumption, carbon emissions, and user comfort penalties. 

Each node in the search tree corresponds to a scheduling decision (assigning a start time to one appliance), and each new step in the task has to respect some constraints, such as time windows, mutual exclusivity, and load limits. These cost constraints should be explicit and auditable, to improve the overall system explainability and transparency.

However, state-space architectures can grow combinatorially with the number of appliances, available time, and constraints in a household. Algorithms like the Uniform-Cost/A* offer optimal solutions but may require substantial memory and computational time as the system grows; of course, adding heuristics (lower bounds from cheapest remaining hours) and decomposition (per-device windows) may mitigate this. 

Another alternative is Greedy Best-First Search, which, because of its focus only on the immediate heuristic, offers faster decisions. Although it does not guarantee the optional schedule, which is particularly problematic for our domain, where the decision can be delayed, but efficiency is critical. Therefore, Greedy is less effective than USC or A*.

Minimax and any other related game-tree algorithms are not applicable in this context, as the task doesn't involve adversarial decision-making. This is a single-point optimization task where the environment (tariffs and grid intensity) is dynamic but not oppositional; hence, classical search algorithm methods are more appropriate. 

Conversely, local search algorithms would offer an efficient and scalable solution by their iteration principle. Starting from an initial schedule and interacting with its neighbors, it would be able to reduce the objective function, which may include electricity cost, CO₂ emissions, and user penalties.Beyond that,  techniques such as hill climbing or simulated annealing can be applied to guide the process. Although local search is more suited to large search spaces with soft constraints, in addition, they do not guarantee optimality and may require random restarts or hybridization with rule-based filters to ensure feasibility.

## Bayesian networks

A Bayesian network make uses of a graph structure that can capture casual/contional relationships, and do a probabilistc calculation to predict high-cost or hiugh-emmisions periods and suports scheduling decisions under uncertanty. Furthermore it handles uncertainty naturally (missing and noisy data) and its archtecture can learn and adapt to new parameters, thought a higher complexity. (Koller & Friedman, 2009)

A Bayesian Network aims to predict conditions and whereas a probabilistic approach like Bayesian would shine in a system where there is a need to forecast in uncertainty, like Probality of high price or change of CO2 intervals, it does not directly optimise actions, there is no need for such probabilistic calculations.

## Logic-based

Logic based approachs offer near-perfect audataibility, with human-readable contrains thta allow easy inspect/approve rules, on the other hand, 


# References

Commission for Regulation of Utilities (CRU). Smart Metering Programme: Time-of-Use Tariffs and Consumer Information. Dublin: CRU, 2023.

EirGrid. Smart Grid Dashboard: Carbon Intensity and System Demand. EirGrid plc, 2024.

Russell, S., & Norvig, P. Artificial Intelligence: A Modern Approach (4th ed.). Pearson, 2021.

Koller, D., & Friedman, N. Probabilistic Graphical Models: Principles and Techniques. MIT Press, 2009.

Goodfellow, I., Bengio, Y., & Courville, A. Deep Learning. MIT Press, 2016.

Sutton, R. S., & Barto, A. G. Reinforcement Learning: An Introduction (2nd ed.). MIT Pres