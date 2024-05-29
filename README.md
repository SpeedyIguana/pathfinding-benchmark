# Benchmarking different pathfinding algorithms

This repository will handle different path finding algorithms and benchmark them.

The types of algorithms are as follows:
- [x] from Point A to Point B
- [ ] from Point A to Region R
- [ ] from Point A to leave Region R

# Concept

To benchmark different path-finding algorithms, we must have an agent that is able to move and an environment for the agent to move.

## Map

For this project we will be working in a 2D space with a map over a discrete number space, i.e. a grid. Each grid block is of unit size.

To encode a map by humans, we can try using existing visualization tools and formats. This project will use `Portable Network Graphics` to encode a map. Simply put a `x` by `y` map can be encoded in a `x` pixels by `y` pixels `.png` image.

A map can consist of the following block-types:
- Grass [Green] [#00ff00]
- Water [Blue] [#0000ff]
- Lava [Red] [#ff0000]

Additionally, a map encoding must have at least one of the following each:
- Suggested agent start position(s) [White] [#ffffff]
- Suggested agent goal position(s) [Black] [#000000]

## Agent

An agent can move one block in 4 directions, relative to its current position:
- North
- East
- South
- West

# Local Development

*Note: this package is using python version 3.12.3*

It is recommended to use a virtual environment like [venv](https://docs.python.org/3/library/venv.html).

## Dependancies

```sh
pip install -r ./requirements.txt
```

## Running the benchmark

```sh
python ./src/benchmark.py
```
