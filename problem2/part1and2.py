# noqa
max_cubes = {"red": 12, "green": 13, "blue": 14}


class Game:
    def __init__(self, game_id: int, games: list[str]):
        self.is_valid = True
        self.game_id = game_id
        self.games = self.parse_games(games)
        self.check_is_valid()

    def parse_games(self, games):
        games_list = []
        for game in games:
            cubes_list = game.split(",")
            cubes_list = self.parse_cubes(cubes_list)
            games_list.append(cubes_list)

        return games_list

    def parse_cubes(self, cubes_list):
        cubes = {}
        for cube in cubes_list:
            cube_count, cube_colour = int(cube.split(" ")[1]), cube.split(" ")[2]
            cubes[cube_colour] = cube_count

        return cubes

    def check_is_valid(self):
        for game in self.games:
            for colour in game.keys():
                if game[colour] > max_cubes[colour]:
                    self.is_valid = False
                    break
            if not self.is_valid:
                break

    def min_game_power(self):
        min_cubes = {}
        for game in self.games:
            for colour in game.keys():
                if colour in min_cubes:
                    min_cubes[colour] = max(game[colour], min_cubes[colour])
                else:
                    min_cubes[colour] = game[colour]
        power = 1
        for value in min_cubes.values():
            power *= value

        return power


def parse_input(input_str) -> dict:
    game_id = int(input_str.split(":")[0].split(" ")[-1])
    games = input_str.split(":")[1].split(";")
    game = Game(game_id, games)

    return game


def main() -> None:
    with open("input.txt", "r") as file:
        input_text = file.read()

    input_text = input_text.split("\n")

    idx_sum = 0
    power = 0
    for input_str in input_text:
        game = parse_input(input_str)
        if game.is_valid:
            idx_sum += game.game_id
        power += game.min_game_power()

    # part1
    print(f"valid game sum : {idx_sum}")

    # part2
    print(f"min game power sum : {power}")


if __name__ == "__main__":
    main()
