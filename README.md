# **Cone of Possibility**
*A geometric simulation framework for visualizing constraint‑bounded probabilistic behavior.*

This project explores how probabilistic systems evolve under different types of constraints.  
It provides a set of experiments that show how **reachable regions** emerge from the interaction between:

- random drift  
- geometric boundaries  
- projection rules  
- time‑varying constraints  

The result is a visual and intuitive model of the **Cone of Possibility** — a way to understand how systems tighten, expand, or reshape their allowable behavior over time.

---

## **Conceptual Ladder**
The framework builds up through five increasingly expressive boundary types:

1. **Circle** — symmetric constraint  
2. **Polygon** — asymmetric, convex constraint  
3. **Star** — multi‑metric constraint (direction‑dependent)  
4. **Arbitrary Function** — real‑world, irregular, concave, or jagged constraints  
5. **Cone (Time‑Varying)** — constraints that tighten or expand over time  

Each experiment shows how a simple Gaussian drift behaves when constrained by these shapes.

---

## **Repository Structure**
```
src/
    state.py
    drift.py
    simulate.py
    constraints.py
    project.py
    visualize.py

experiments/
    circle_experiment.py
    polygon_experiment.py
    star_experiment.py
    arbitrary_experiment.py
    cone_circle_experiment.py
    shrinking_star_cone_experiment.py
```

---

## **Running Experiments**
Each experiment is self‑contained:

```bash
python experiments/circle_experiment.py
python experiments/polygon_experiment.py
python experiments/star_experiment.py
python experiments/arbitrary_experiment.py
python experiments/cone_circle_experiment.py
python experiments/shrinking_star_cone_experiment.py
```

Plots will open in a window showing the trajectory (blue) and the constraint boundary (red).

---

## **Why This Matters**
This framework provides a geometric lens for understanding:

- bounded exploration  
- safety constraints  
- guardrails  
- error budgets  
- multi‑metric limits  
- time‑dependent capability envelopes  

It is intentionally simple, visual, and extensible — a foundation for deeper work on reliability, agent behavior, and probabilistic systems.

---

## **License**
Apache License 2.0

---

## **Future Work**
- Soft boundaries (penalty‑based instead of hard projection)  
- Attractors and stable regions  
- Time‑varying star boundaries  
- 3D cone visualization  
- Multi‑agent cones  


---

