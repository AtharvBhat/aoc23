# flake8: noqa
from utils import Map, parse_input


def main():
    with open("input.txt", "r") as file:
        input_text = file.read()

    seeds, maps = parse_input(input_text)

    locations = []

    for seed in seeds:
        #print(f"Seed: {seed}")
        location = seed
        for location_map in maps:
            location = location_map.map_location(location)
            #print(f"    {location_map.name} : {location}")
        locations.append(location)

    print(f"Min Location: {min(locations)}")


if __name__ == "__main__":
    main()
