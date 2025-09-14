# Multiple & Multilevel Inheritance in Python

## Concepts

- **Multilevel Inheritance:** Child inherits from a parent, which inherits from another parent.
- **Multiple Inheritance:** Child inherits from more than one parent.

## Example Classes
- `Animal` → Base class
- `Prey` → inherits from `Animal`
- `Predator` → inherits from `Animal`
- `Rabbit` → inherits from `Prey`
- `Hawk` → inherits from `Predator`
- `Fish` → inherits from both `Prey` and `Predator`

## Output
Jessica is eating
Bald is eating
Wanda is eating

Jessica is sleeping
Bald is sleeping
Wanda is sleeping

Jessica can Flee
Bald can Hunt
Wanda can Flee
Wanda can Hunt
