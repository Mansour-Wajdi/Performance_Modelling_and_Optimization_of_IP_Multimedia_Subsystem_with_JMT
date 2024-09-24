# Performance Modelling and Optimization of IMS

## Introduction

This project involves the study and reproduction of the performance model presented in the IEEE-published paper titled **["Performance Modelling and Optimization of IP Multimedia Subsystem (IMS)"](https://ieeexplore.ieee.org/document/6779915).** The IMS provides multimedia and telephony services in Next-Generation Networks (NGNs), but it faces significant challenges in maintaining Quality of Service (QoS) under increased signaling loads.

The primary focus of this project was to reproduce the model proposed in the paper using **[Java Modeling Tools (JMT)](https://jmt.sourceforge.net/)**, conduct experiments with different configurations, and analyze the impact of these configurations on the overall system performance.

## Repository Structure

This repository is organized as follows:

- **JMT Models**: Contains Java Modeling Tool (JMT) simulation models for different load conditions:
  - `IMS Normal Load.jsimg`: Simulation model for IMS under normal load conditions.
  - `IMS Overload with finite capacity.jsimg`: Simulation model for IMS under overload conditions with finite system capacity.
  - `IMS Overload with infinite capacity.jsimg`: Simulation model for IMS under overload conditions with infinite system capacity.
- **Optimization Solver**:
  - `gurobi.py`: Python script that uses **[Gurobi Optimizer](https://www.gurobi.com/)** for calculating optimal routing probabilities and handling nonlinear system constraints.
  - `values.py`: Python script for calculating simulation values and parameters.
- `README.md`: Provides a comprehensive overview of the project, its objectives, methodologies, and key findings.

## IMS Architecture

IMS architecture is composed of several key elements responsible for the processing and routing of signals, including:
- **Call Session Control Function (CSCF)**, which consists of:
  - **I-CSCF (Interrogating-CSCF)**
  - **P-CSCF (Proxy-CSCF)**
  - **S-CSCF (Serving-CSCF)**

The project focuses on modeling the behavior of these components, particularly the **S-CSCF**, which is often considered the bottleneck in IMS networks.

### SIP (Session Initiation Protocol)

The **Session Initiation Protocol (SIP)** is a key signaling protocol in IMS, facilitating the establishment, modification, and termination of multimedia sessions. This project explores how SIP messages are prioritized and routed through the IMS under varying traffic loads.

## Objective

The objective of this project is to reproduce the IMS traffic model proposed in the IEEE paper and evaluate its performance under different signaling loads. This was achieved by:
- **Reproducing the model** using **Java Modeling Tools (JMT)**.
- **Experimenting with different parameters**, such as message arrival rates, routing policies, and system capacity.
- **Simulating normal and overload conditions** to evaluate the prioritization of SIP messages, routing efficiency, and system bottlenecks.

## SIP Message Classification

The SIP messages are classified into three priority levels:
- **Class 1 (High Priority):** Messages that terminate sessions (e.g., BYE, CANCEL).
- **Class 2 (Medium Priority):** Lightweight messages (e.g., REGISTER, MESSAGE, PUBLISH) and retransmissions.
- **Class 3 (Low Priority):** Messages that initiate sessions (e.g., INVITE).

## Model Assumptions

In order to simplify the model, several key assumptions were made:
- The model considers four main signaling procedures:
  1. Registration
  2. Basic session establishment/termination
  3. Instant messaging
  4. Presence information publication
- Only one instance of each **CSCF** is modeled.
- **S-CSCF** is assumed to be the main bottleneck in the network.

These assumptions simplify the model's complexity while still providing meaningful insights into IMS behavior under different load conditions.

## Experimental Setup and Parameters

The model was simulated using **Java Modeling Tools (JMT)** under different traffic conditions. The following parameters were experimented with:
- **Message arrival rates** for different classes of SIP messages.
- **Routing probabilities** between IMS components.
- **System capacity** constraints under both normal and overload traffic conditions.

## Problems Encountered

During the implementation and experimentation phases, several issues were encountered:
1. **Lack of satisfactory solutions** during routing probability calculations.
2. **Nonlinear system incompatibility** with the **Gurobi optimizer** .
3. **Inaccurate approximations** of certain values in the paper, leading to deviations in results.

### Solutions Implemented

1. A tolerance was introduced in the model's equations to allow for greater flexibility.
2. Constraints were added to ensure that probabilities remained within the [0, 1] range.
3. The Gurobi optimizer's objective function was modified to minimize errors resulting from these approximations.

## Simulations 

The model was evaluated under the following traffic conditions:
1. **Normal load conditions**, where the system operates within capacity.
2. **Overload conditions with infinite capacity**, simulating an ideal, unconstrained environment.
3. **Overload conditions with finite capacity**, where the system's limitations are modeled more realistically.

## Results
**Normal Load**

| CSCF Type | Utilization | Queue Time | Number of Customers |
|-----------|-------------|------------|---------------------|
| P-CSCF    | 0.4784      | 0.4503     | 0.9035              |
| I-CSCF    | 0.1947      | 0.2385     | 0.242               |
| S-CSCF    | 0.7645      | 4.1508     | 3.358               |

**Overload with infinite capacity**

| CSCF Type      | Number of Customers | Queue Time | Response Time | Residence Time | Utilization | Throughput |
|----------------|---------------------|------------|---------------|----------------|-------------|------------|
| P-CSCF         | 4.1601              | 2.0781     | 2.5393        | 5.0335         | 0.7971      | 1.5959     |
| I-CSCF         | 0.5819              | 0.5853     | 1.5844        | 0.7161         | 0.3659      | 0.3647     |
| S-CSCF (FCR)   | 1.07E+05            | 0          | 0             | 5.80E+04       | -           | 1.9257     |
| S-CSCF (queue) | 1.05E+05            | 8.24E+04   | 8.24E+04      | 1.26E+05       | 1           | 0.8018     |
| S-CSCF (fifo)  | -                   | -          | -             | -              | -           | -          |
| S-CSCF (pq)    | 269.4105            | 494.1404   | 373.9351      | 372.8225       | 0.9976      | 0.7981     |


**Overload with finite capacity**

| CSCF Type      | Number of Customers | Queue Time | Response Time | Residence Time | Utilization | Throughput | Drop  |
|----------------|---------------------|------------|---------------|----------------|-------------|------------|-------|
| P-CSCF         | 5.4669              | 2.7359     | 3.2666        | 6.4352         | 0.8482      | 1.6934     |       |
| I-CSCF         | 0.4891              | 0.491      | 1.4921        | 0.5714         | 0.3272      | 0.3288     |       |
| S-CSCF (FCR)   | 107.4896            | 0          | 90.1853       | 125.0375       | -           | 1.1898     |       |
| S-CSCF (queue) | 97.9117             | 120.7711   | 122.0172      | 113.9626       | 1           | 0.802      | 0.3819|
| S-CSCF (fifo)  | 9.2285              | 12.1807    | 12.8506       | 10.6179        | 0.8918      | 0.7101     |       |
| S-CSCF (pq)    | 0.1643              | 0.5637     | 1.7925        | 0.1923         | 0.115       | 0.0922     |       |


The results revealed key insights into IMS performance:
- **Message prioritization** was effective in managing signaling loads during normal traffic.
- Under **overload conditions**, **S-CSCF** was identified as the primary bottleneck, impacting overall system performance.


## Conclusion

This project successfully reproduced the IMS performance model proposed in the IEEE paper using **Java Modeling Tools (JMT)**. By simulating different traffic conditions and experimenting with various parameters, the project provided insights into the behavior of IMS under both normal and overload traffic conditions. Further research is needed to refine the model and address its limitations.

## References
- [IEEE - Performance Modelling and Optimization of IP Multimedia Subsystem](https://ieeexplore.ieee.org/document/6779915)
- [Java Modelling Tools - JMT](https://jmt.sourceforge.net/)
- [Gurobi Optimizer](https://www.gurobi.com/)
