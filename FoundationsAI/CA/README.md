# Background

## Problem

Recently there is a growing pressure to create an integration of smart meters and Time-of-Use(ToU) tariffs in Ireland, which have already begun transforming how residential buildings consume electricity. The ToU establishes that the electricity tariffs would vary according to the time of day, dividing into peak (17:00-19:00), day (08:00-23:00), and night (23:00-08:00), which reflects the variation in grid demand and generation costs (ESB Networks, 2024). Additionally, the Commission for Regulation of Utilities (CRU) mandates that all electricity suppliers working in Ireland offer ToU plans, enabling consumers to reduce their electricity costs while improving the grid's sustainability by avoiding the peak periods. (CRU, 2023)

Despite these initiatives, most households still use their high-consumption electrical appliances, like electric vehicle chargers, washing machines, and electric heaters, during peak hours, creating an elevated electricity bill and increasing grid congestion and usage of high-emission power sources during the peak demand (EirGrid, 2024). Whereas there is already a manual form of scheduling, this process demands the user to account for the tariffs times, as well as the personal comfort of multiple people in a household and and their need for an appliance, consequently, most people don't set the manual scheduling or even avoid the smart meters for the extra work needed.

Moreover, according to the EirGrid Smart Grid Dashboard (2024), CO₂ intensity varies by more than 50% between day and night, especially because during the peak hours, there is lower wind generation, making the provider rely on gas-fired plants; by contrast, during night hours, winds are stronger, creating a higher sustainable energy source. Thus, developing a strategy to transfer the load of electricity consumption could reduce residential carbon footprint without requiring a decrease in energy consumption.


## Oportunitty

Based on the previous section, proposing an intelligent scheduling system to balance the electricity load of a household would represent a significant opportunity for both the residential consumers and the electricity providers as for the Ireland carbon-reduction targets.

For the households, the system would enable automated management of smart high-consumption appliances to be shifted to lower-cost, lower-carbon periods without the need for user setup and management, therefore reducing the electricity consumption while keeping comfort and convenience. This reduction of monetary expenditure with the addition of a better use of natural resources could be a motivation point for the households to adopt the system. Furthermore, this system could be integrated with live-time data from energy suppliers, making the scheduling able to respond to seasonal demands and register user preferences.

For grid operators and suppliers, a widespread adoption of such systems would support one of the key objectives for the Commission for Regulation of Utilities Smart Metering Programme, the demand-side flexibility, which refers to the ability of electricity consumers to adjust to when and how much electricity they use in response to grid signals such as price, grid conditions, or renewable energy available (CRU, 2023). Furthermore, the adoption of demand-side flexibility could flatten the peak demand, reducing the strain on the infrastructure and reliance on carbon-intensive peaking plants. This would highly enhance grid stability, forecasting accuracy, and progress toward national decarbonization targets.

Overall, the solution aligns with the economic, social, and ethical interests of consumers, grid operators, and electricity suppliers, broadening the range of commercial strategies for the final production and also advancing Ireland's transition toward a more sustainable, data-driven energy.

# Solution

The proposed solution consists of an Inteligent Appliance Scheduling System (IASS), this system would focus on the setermination of optimal start timers for the eletrical devices to minimise eletricity costs and environmental impact while maintaining user confort. The optimisation models is a decison-making framework that can be approached using diverses of the curent inteligence paradgms, each one providing advanatges and challenges on interpretability, adaptability and computational performance.

Initially, the scheduling problem will be formulated as a state-space searcxh task, where each state represents a partial assigment of appliance operations. Classical search algorithms, including Uniform-Cost, Greedy Best-First and A*, will be applied to explore 


# References

Commission for Regulation of Utilities (CRU). Smart Metering Programme: Time-of-Use Tariffs and Consumer Information. Dublin: CRU, 2023.

EirGrid. Smart Grid Dashboard: Carbon Intensity and System Demand. EirGrid plc, accessed 2024.

ESB Networks. Guide to Smart Meter Tariff Time Bands. Dublin: ESB Networks, 2024.

Russell, S., & Norvig, P. Artificial Intelligence: A Modern Approach (4th ed.). Pearson, 2021.