"""
Modules
Independent units that can be used to construct complex structure

Modularization
Process of dividing software into multiple independent modules

Coupling
- measure of the degree of interdependence between modules
- degree to which one class knows about another class
- how strongly a software element is connected to other elements

If information is only exposed thourgh interfaces like data hiding - loosely coupled

If information is exposed via data members directly - tightly coupled

Thight coupling makes it more likely that code will stop working after the chagne

5 types of coupling - from best to worst
Data coupling
Control coupling
External coupling
Common coupling
Content coupling

Cohesion
- the degree to which the elements of a module belong together
- measures the strength of relationship between pieces of functionality within a given module
- high cohesion
    - reduces complexity
    - increases maintainability
    - increases reusability

7 types of cohesion - from high to low
Functional cohesion
Sequential cohesion
Communicational cohesion
Procedural cohesion
Temporal cohesion
Logical cohesion
Coincidental cohesion

Cohesion vs Coupling

| Coupling                            | Cohesion                           |
|-------------------------------------|------------------------------------|
| Concept of inter module             | Concept of intra module            |
| Relationships between modules       | Relationship within module         |
| Increasing in coupling is avoided   | Increasing in cohesion             |
| Independence among modules          | Functional strength of modules     |
| Low coupling is good for software   | High cohesion is good for software |
| Modules are connected to each other | Module focuses on the single thing |
"""

