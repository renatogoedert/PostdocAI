# Executive Summary

This business case is part of continuous assessment for Foundations of Artificial Intelligence; it focuses on reducing the current problem of energy costs and carbon emissions in Ireland through an automated AI-driven load-balancing system, leveraging the Irish government initiatives like smart meters and time-of-use tariffs, while preserving users' comfort.

Following government statistics, the system aims to reduce on average 10% on household electricity bills, lower carbon footprint and Ireland's Climate Action Plan (2023). With lower development costs and following GDPR best practices, the system promotes itself as being a technically feasible, scalabe and ethical project.

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

## Search Based Optimisation

This approach can be formulated as a state-space search problem, where each state would represent a partial assignment of appliance start times within a 24-hour period. According to Russell & Norvig (2021), the search-based optimization shines in small to medium-sized problems with stable variable structures and following an explicit objective, in this case, a weighted combination of electricity consumption, carbon emissions, and user comfort penalties. 

Each node in the search tree corresponds to a scheduling decision (assigning a start time to one appliance), and each new step in the task has to respect some constraints, such as time windows, mutual exclusivity, and load limits. These cost constraints should be explicit and auditable, to improve the overall system explainability and transparency.

However, state-space architectures can grow combinatorially with the number of appliances, available time, and constraints in a household. Algorithms like the Uniform-Cost/A* offer optimal solutions but may require substantial memory and computational time as the system grows; of course, adding heuristics (lower bounds from cheapest remaining hours) and decomposition (per-device windows) may mitigate this. 

Another alternative is Greedy Best-First Search, which, because of its focus only on the immediate heuristic, offers faster decisions. Although it does not guarantee the optional schedule, which is particularly problematic for our domain, where the decision can be delayed, but efficiency is critical. Therefore, Greedy is less effective than USC or A*.(Russell & Norvig, 2021)

Following what Russell & Norvig (2021) declares, minimax and any other related game-tree algorithms are not applicable in this context, as the task doesn't involve adversarial decision-making. This is a single-point optimization task where the environment (tariffs and grid intensity) is dynamic but not oppositional; hence, classical search algorithm methods are more appropriate. 

Conversely, local search algorithms would offer an efficient and scalable solution by their iteration principle. Starting from an initial schedule and interacting with its neighbors, it would be able to reduce the objective function, which may include electricity cost, CO₂ emissions, and user penalties.Beyond that,  techniques such as hill climbing or simulated annealing can be applied to guide the process. Although local search is more suited to large search spaces with soft constraints, in addition, they do not guarantee optimality and may require random restarts or hybridization with rule-based filters to ensure feasibility. (Poole & Mackworth, 2017)

## Logic Based Reasoning

The foundation of logic-based reasoning systems, as described by Russell and Norvig (2021), is a series of explicit rules defining the relationships in a specific environment. With these rules the system can take actions, providing high levels of transparency and interpretability in decision-making, as every decision taken by the system can be traced back to its own rules. However, when dealing with quantitative trade-offs, such as the ones presented in this system, this model demonstrates substantive limitations. In addition, logic-based reasoning systems also struggle to adapt to dynamic and uncertain environments, as they work with a fixed set of rules that would demand a constant manual update to remain effective.

## Bayesian networks

A Bayesian network makes use of a graph structure that can capture causal/conditional relationships and do probabilistic calculations to predict high-cost or high-emission periods and supports scheduling decisions under uncertainty. Furthermore, it handles uncertainty naturally (missing and noisy data), and its architecture can learn and adapt to new parameters, though with a higher complexity. (Koller & Friedman, 2009)

A Bayesian network aims to predict conditions, and whereas a probabilistic approach like Bayesian would shine in a system where there is a need to forecast in uncertainty, like the probability of a high price or a change of CO₂ intervals, it does not directly optimize actions; there is no need for such probabilistic calculations.

## Deep Learning (Feed-Foward Neural Networks)

Deep learning was developed to solve complex relationships between the input and variables with the use of multiple layers of nodes. That approach offers a high capability of learning any nonlinear patterns from data, a fact that makes them suitable for prediction, like forecasting energy demand, electricity tariffs, or carbon intensity. (Goodfellow, Bengio and Courville, 2016)

Nevertheless, while the feedforward networks excel at discovering data correlations, they require large amounts of labeled data, increasing their development costs, and don't possess a focus on decision-making or dynamic feedback. For this solution, deep learning, as Bayesian networks, could be used to forecast the external variable but not for optimization tasks. Hence, deep learning should be left as a possible complement, but not as a main algorithm for adaptive control and decision-making.

## Reinforcement Learning

The most adaptable of all approaches among the ones considered, it particularly shines within dynamic environments and changing variables, plus it is capable of learning trade-offs that are almost impossible to hand-code. However, the training of any RL model demands a large dataset and a considerate computational resource for hyperparameter tuning. Despite that, the resulting model is highly efficient on inference. 

Once trained, algorithms like Q-learning can make decisions just with one lookup in a compact neural network. Moreover, these models learn how to maximise cumulative reward by reducing cost and emissions while satisfying user comfort constraints. (Sutton & Barto, 2018) 

# Selected solution

After thorough consideration of all algorithms stated before, the two most applicable to the problem were Search (A*) and Reinforcement Learning. As the system aims to be applied in multiple houses, the computation resource needed to train a model would be divided by multiple users, making it more viable, and, combined with the probability of an expansion with energy suppliers and grid providers to create a data-driven system, reinforcement learning was chosen as the most suitable one, as its adaptive paradigm would make it perfect to receive and adapt to the data of the grid in an eventual demand-side flexibility system.

## Archtecture

The system would be designed as a Markov Decision Process (MDP). Sutton and Barto (2018) explain this system as a mathematical framework for sequential decision-making problems in environments where outcomes are partly under control and partly random. They are divided into:

S – a finite set of states, representing all possible configurations the environment can be in.

A – a finite set of actions available to the agent in each state.

P(s′|s, a) – a transition probability function, which defines the probability of moving to state s′ given that the agent took action a in state s.

R(s, a) – a reward function, specifying the immediate numerical reward received after taking action a in state s.

γ – a discount factor, 0 ≤ 𝛾 ≤ 1, which determines how much the agent values future rewards compared to immediate ones.

On this, the agent would learn a policy π(a∣s) that maximizes the expected cumulative reward over time; the state would include time, appliance status, tariff band, and carbon intensity; the actions would be selecting an appliance start time,; finally the reward would penalize/reward costs, emissions, and comfort violations.

However, Lapan (2020) brings to attention that the rewarding and penalizing should be well designed, as if the AI gets a sequence of punishments, it could get stuck, as it would learn that no matter what it does, it would get punished. So techniques like giving rewards per progress and offering relative rewards would be beneficial to a proper learning phase. With that in mind, the proposed reward function is

Reward = −α x Cost −β x Emissions −γ x Penaltycomfort ​+δ x ApplianceBonus

The reward weights (α, β, γ, and δ) should be predefined for training but also may be adjusted during iterations of the training phase to allow improvement of the policy.

## Algorithms

One of the main expectations for this system would be a fast inference capability, even when applied to computationally constrained hardware. Therefore, among the algorithms researched, the ones that use the Q-value or Q-learning , were selected due to their efficiency and simplicity.

The foundation of these algorithms is the Q-value function, which calculates the expected cumulative reward of an agent, considering starting in a state s, taking an action a, and following one particular policy afterwards. (Sutton and Barto, 2018)

- Q-learning: This algorithm creates a Q-table that stores the values of each pair (state and action). During inference the model performs a simple lookup to find, in the table, the highest Q value and select the related actions. This is a lightweight and effective solution for low-dimensional states problems

## Data Sources

As this own report arises, RL AI systems demand a substantial amount of data for training. Fortunately, much of the data sources were already collected and publicly available for training. Not just that, but companies like energy suppliers, grid operators, and appliance builders usually offer high-structured, high-precision data, removing from the solution development: a heavy data wrangling process. The data source for the system would be

- Tariff data: ESB Networks and Electric Ireland documentation on Time-of-Use tariffs
- Carbon intensity: EirGrid Smart Grid Dashboard and published CO₂ emission datasets.
- Appliance usage patterns: Derived from demand-side management literature and residential energy surveys

# Implementation

The report would consist of only the implementation of the AI system; all extra hardware is not going to be taken into consideration. The development of the MVP for the smart scheduling system based on the Q-learning algorithm would require minimal technical infrastructure, as all experiments can be conducted using a standard laptop and open-source tools. Therefore, the resources for this solution are human only and time.

Human Resources:

| Role           | Description                                                                             | Estimated Time|  Estimated Cost  |
|----------------|-----------------------------------------------------------------------------------------|---------------|------------------|
| AI Engineer    | Design and implement the Q-learning algorithm, define the state, actions and rewards    | 160 hours     | €30/hour = €4800 |
| Data Analist   | Curates and validates training datasets from public sources                             |  40 hours     | €25/hour = €1000 |
| Project Lead   | Oversees progress, documentation and ethical compliance                                 |  60 hours     | €30/hour = €1800 |


| Phase                          | Activity                                                                        | Duration|
|--------------------------------|---------------------------------------------------------------------------------|---------|
| Research and Design            | Review leterature, define variables, states, and weights for the reward function|  1 week |
| Environment Setup              | Simulate environment with tariff and carbon data, define appliance models       |  1 week |
| Q-Learning Agent Development   | IMplement Algorithm, integrate environment, tune the reward weights             |  2 weeks|
| Testing and Evaluation         | Run multiple times, measure convergence, cost reduction, and emission savings   |  1 week |
| Reporting and Documentation    | Analyze results, write a technical report                                       |  1 week |

## Financial benefits

Proceeding to calculate the Return on Investment (ROI), the data provided by both EirGrid (2024) and ESB Network (2024) states that smart scheduling can save from 8-15% on energy costs. Regarding that, and combining a conservative 10% saving with the average Irish household's electrical bill of €1,800 per year (CRU, 2024) results in an expected savings of €180 per year per household. 

As the total development costs rest around €7600, and considering the system would be sold with a value that offers a profit of half a year of expected savings (€90), a total of approximately 86 households would be needed to recover the initial investments (€90 x 86 = 7740), offering a very feasible break-even point for any small company to invest and innovate. The potential of financial gain increases exponentially due to its lower initial cost; for example, ESB states that over 2 million smart meters are installed all over Ireland. if just 1% of these (20,000) adopt the system, the expected gross revenue would be €1,800,000.00 (€90 * 20,000). calculating ROI of this, ((*€1,800,000 – €7,600) / 7,600) * 100, a staggering 23,585% Of profit over investment.

Beyond the direct revenue, companies like grid operators and energy suppliers would benefit from this energy load-balancing system, which could foster a subsidy or partnership model to strengthen the economic benefits

## Non-Financial benefits

Beyond the financial domain, this solution would contribute to the carbon emission reduction by load-shifting the energy consumption to high renewable generation periods, supporting the Ireland 2030 Climate Action Plan and the UN Sustainable Development Goals. Additionally, this system has the ability to foster a much-delayed technological innovation in both the smart home and energy management sectors, advancing the implementation of the demand-side flexibility objective. Utterly, these aspects align with national sustainability targets and European digitalization policies.

# Risk and Ethics

## Privacy and Data Protection

The main data to feed the solution would consist of Time-of-Use data and appliance energy consumption, which are public and do not imply any risk to personal data. However, while this data is not directly sensitive, the user preferences and detailed consumption data could be used to reveal user routines and behavior patterns. In view of that, the system would be designed taking into consideration a privacy-by-design architecture, where all personal and household data are stored and processed locally on the user's smart HUD or device. Only anonymized or aggregated summaries are shared externally for analytics or system updates.

Retaining the data locally would allow the users to have full data ownership; this, allied with transparent access and an easy opt-out choice, would increase users' assurance that no data would be used without their consent. Furthermore, all data could possibly go through another layer of encryption and protection within device-level security, furthering General Data Protection Regulation (GDPR) principles of data minimization and user control.

## Transparency and Explainability

Since Q-learning algorithms operate via explicit reward functions, the system could employ a high level of transparency and explainability through a simple interface that communicates and explains why a specific scheduling decision was made; for example, "The washing machine was scheduled for 23:00 to minimize cost and emissions where the sleep time is set to 00:00." The meaning of this step is to enhance the user's understanding and trust, while it facilitates the user's understanding and changing of comfort rules to adjust to users' routines. Thus, this simple step fully aligns the system with the EU Intelligence Act (2024) transparency and traceability for AI systems mandate.

## Fairness and Accessibility

Even tought the algorith offers close to minimal risk of bias on its decision-making, still remains the possiblity of favouing one manufacturers device over another. Nevertheless, the simplicity and transparency of Q-learning, which rely manly on the reward function and the Q-table rather than the hidden layers of neural networkd, significantly reduce the likehood of bias. Additionally, the inclusion of the confort rules further contrains the model behaviour, minimiszing any decision based on AI bias.

One of the main pillars of the system would be an accessible design for the overall system. Although it doesn't affect the AI method in itself, making it easier to use in lower-literacy households is essential to widespread adoption of the model by a higher number of households across all social groups, hence maximizing its financial, social and environmental benefits. As mentioned before, a subsidised partnership could be realized with governments/companies to offer an affordable price and spread equitably to all social groups.

## Risk Assesment

| **Risk**                   | **Description**                                                                     | **Likelihood** | **Impact** | **Mitigation Strategy**                                                                             |
| -------------------------- | ----------------------------------------------------------------------------------- | -------------- | ---------- | --------------------------------------------------------------------------------------------------- |
| **Data breach**            | Unauthorized access to consumption data revealing private behavior                  | Low         | High       | Use local storage, strong encryption, anonymization, and GDPR compliance                           |
| **Algorithmic bias**       | The model may optimize unfairly for certain user patterns or appliance types        | Low         | Low     | Regularly review training data and test for representativeness across demographics                  |
| **Model misbehavior**      | Inaccurate or unsafe scheduling (e.g., running high-load appliances simultaneously) | Low            | Medium     | Introduce rule-based constraints (e.g., load limits, user safety overrides)                         |
| **Transparency failure**   | Users may not understand or trust AI decisions                                      | Medium         | Medium     | Implement explainability dashboard and clear user communication                                     |
| **Technology exclusion**   | Non-smart homes or elderly users unable to participate                              | Medium         | Medium     | Design lightweight, user-friendly interfaces; offer manual scheduling options                       |
| **Environmental backfire** | Shifting load at scale could create new mini-peaks                                  | Low            | High     | Coordinate with grid operators; use adaptive reinforcement updates to prevent synchronized behavior |

## Regulatory Alignment

As stated during this report, the proposed system not just fully aligns but also helps with the development of major European and national regulations like

- Ireland’s Climate Action Plan (2023–2030): Plan to reduce carbon emissions and incentivize sustainable energy usage.

- EU Artificial Intelligence Act (2024): Act to provide transparency, explainability, and accountability for AI systems users.

- General Data Protection Regulation (GDPR, 2016): EU regulation to provide to indicidual users data privacy.

# References

Commission for Regulation of Utilities (CRU) (2023) Smart Metering Programme: Time-of-Use Tariffs and Consumer Information. Dublin: CRU.

EirGrid (2024) Smart Grid Dashboard: Carbon Intensity and System Demand. Dublin: EirGrid plc.

ESB Networks (2024) Guide to Smart Meter Tariff Time Bands. Dublin: ESB Networks.

ESB Networks (n.d.) About Smart Meters. Available at: https://www.esbnetworks.ie/services/manage-my-meter/about-smart-meters (Accessed: 14 November 2025).

European Parliament and Council of the European Union (2016) Regulation (EU) 2016/679: General Data Protection Regulation (GDPR). Official Journal of the European Union, L 119, 4 May.

European Parliament and Council of the European Union (2024) Regulation (EU) 2024/1689 on Artificial Intelligence. Official Journal of the European Union, L 1689, 12 July.

Goodfellow, I., Bengio, Y. and Courville, A. (2016) Deep Learning. MIT Press.

Government of Ireland (2023) Climate Action Plan 2023–2025. Dublin: Department of the Environment, Climate and Communications.

Koller, D. and Friedman, N. (2009) Probabilistic Graphical Models: Principles and Techniques. MIT Press.

Lapan, M. (2020) Deep Reinforcement Learning Hands-On. 2nd ed. Packt Publishing.

Poole, D. and Mackworth, A. (2017) Artificial Intelligence: Foundations of Computational Agents. 2nd ed. Cambridge University Press.

Russell, S. and Norvig, P. (2021) Artificial Intelligence: A Modern Approach. 4th ed. Pearson.

Sutton, R.S. and Barto, A.G. (2018) Reinforcement Learning: An Introduction. 2nd ed. MIT Press.
