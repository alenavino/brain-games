#!/usr/bin/env python3


from brain_games.scripts.brain_games import greet
from brain_games.engine import engine
from brain_games.games.even import even


def main():
    greet()
    engine(even)


if __name__ == '__main__':
    main()
