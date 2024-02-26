#!/usr/bin/env python3


from brain_games.scripts.brain_games import greet
from brain_games.engine import engine
from brain_games.games.calc import calc


def main():
    greet()
    engine(calc)


if __name__ == '__main__':
    main()
