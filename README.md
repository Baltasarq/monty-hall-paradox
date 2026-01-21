# The Monty Hall Paradox

A simulation illustrating the [Monty Hall paradox](https://en.wikipedia.org/wiki/Monty_Hall_problem).

![Simulation results](docs/paradox_result.png)

The simulation counterintuitively demonstrates that you get an extra third of probabilities of getting the prize by changing your initial choice.

## Installing

You need **Python** tu run the simulation.

You can install the dependencies with the `requirements.txt` file:

```bash
$ pip install -r requirements.txt
```

Or, you cand do it manyally by installing **pandas** and **matplotlib**, as in:

```bash
$ pip install --upgrade pandas matplotlib
```

## Execution

Just execute the *py* program:

```bash
$ python monty_hall.py
```

This will show all the available options:
- help: will show the same information as invoked without arguments.
- verbose: will show a textual table with 10 maximum elements.
- enoc, or evaluate-no-change: shows a graph with data evaluated over 100000 elements.
- ec, or evaluate-change: shows a graph with data evaluated over 100000 elements, the initial choice is changed.

The last two can be given at the same time, and in that case their results are compared.
