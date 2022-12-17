# Part 2 Implementation from https://github.com/Samathingamajig

import argparse
import math
import pprint
import itertools
import re
import os
import tqdm
from multiprocessing import Pool
import numpy as np
import concurrent.futures
air = '.'

def main(args):
    # Example input:
    # Sensor at x=2, y=18: closest beacon is at x=-2, y=15 

    # with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as input_file:
    #     input = input_file.read().rstrip()
    #     solution(input, search_space=4_000_000)


    elf_file = open(args.input, 'r')
    elf_lines = elf_file.readlines()
    sensors = []
    grid = dict()

    max_x, max_y = 0, 0
    min_x, min_y = 999999, 999999
    search_space = 4_000_000

    # Get Sensors and Beacons
    for line in elf_lines:
        line = line.strip()
        line = line.split('=')
        sensor_x = int(line[1].split(',')[0])
        sensor_y = int(line[2].split(':')[0])
        beacon_x = int(line[3].split(',')[0])
        beacon_y = int(line[4])
     


        sensors.append((sensor_x, sensor_y, beacon_x, beacon_y))
    print("Sensors & Beacons loaded")

    sensor_distance = {
        a + b * 1j: distance(a, b, c, d) for a, b, c, d in sensors
    }

    min_x = int((min(sensor.real - dist for sensor, dist in sensor_distance.items())))
    max_x = int((max(sensor.real + dist for sensor, dist in sensor_distance.items())))
 

    positive_lines = []
    negative_lines = []
    edges: set[complex] = set()
    intersections: set[complex] = set()

    for sensor, dist in sensor_distance.items():
        top, bottom = sensor - dist * 1j, sensor + dist * 1j
        left, right = sensor - dist, sensor + dist

        positive_lines += [(left, top), (right, bottom)]
        negative_lines += [(left, bottom), (right, top)] 

    for pos, neg in itertools.product(positive_lines, negative_lines):
        isect = get_line_intersection(pos, neg)
        if (
            -1 <= isect.real <= search_space + 1
            and -1 <= isect.imag <= search_space + 1
            and int(isect.real) == isect.real
            and int(isect.imag) == isect.imag

        ):
            intersections.add(isect)
        pass

    whole_points: set[complex] = set()

    for isect in intersections:
        whole_points.add(isect + 1)
        whole_points.add(isect - 1)
        whole_points.add(isect + 1j)
        whole_points.add(isect - 1j)

    answer = None 
    for point in whole_points:
        if 0 <= point.real <= search_space and- 1 <= point.imag <= search_space + 1:
            for sensor, dist in sensor_distance.items():
                if distance(point.real, point.imag, sensor.real, sensor.imag) <= dist:
                    break
            else:
                answer = point
                break
    print(answer)
    print("Decoded: ", int(4_000_000 * answer.real + answer.imag))



def distance(x1, y1, x2, y2) -> tuple[int, int]:
    return abs(x2 - x1) + abs(y2 - y1)


def get_det(a, b):
    if isinstance(a, complex):
        return get_det((a.real, a.imag), b)
    if isinstance(b, complex):
        return get_det(a, (b.real, b.imag))
    return a[0]*b[1] - a[1]*b[0]


def get_line_intersection(
    line1: tuple[complex, complex], line2: tuple[complex, complex]
) -> complex:
    x_diff = (line1[0].real - line1[1].real, line2[0].real - line2[1].real)
    y_diff = (line1[0].imag - line1[1].imag, line2[0].imag - line2[1].imag)

    div = get_det(x_diff, y_diff)
    if div == 0:
        raise Exception("Lines do not intersect")
    
    d = (get_det(*line1), get_det(*line2))
    x = get_det(d, x_diff) / div
    y = get_det(d, y_diff) / div
    return x + y * 1j






if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = "Day 4 Advent of Code 2022",
                                    description = "Solve the first day of Advent of Code 2022"
                                     )

    parser.add_argument('-i', '--input', help = 'Input file', required = True)
    args = parser.parse_args()
    main(args)

   






