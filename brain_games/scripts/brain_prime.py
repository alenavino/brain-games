#!/usr/bin/env python3


from brain_games.scripts.brain_games import greet
from brain_games.engine import engine
from brain_games.games.prime import prime


def main():
    greet()
    engine(prime)


if __name__ == '__main__':
    main()
