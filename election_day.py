import csv


class ElectionsManager:
    def __init__(self):
        self.precincts = []
        self.candidates = []
        self.results = {}
        self.final_results = {}
        self.total_votes = 0

    def process_results(self, results_file):
        with open(results_file, newline="\n") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            for index, line in enumerate(reader):
                if index == 1:
                    for candidate_name in line[1:]:
                        self.candidates.append(candidate_name)
                if index > 1:
                    self.precincts.append(line[1:])
        for precinct in self.precincts:
            for index, result in enumerate(precinct):
                if self.candidates[index] in self.results:
                    self.results[self.candidates[index]].append(int(result))
                else:
                    self.results[self.candidates[index]] = [int(result)]
        self.process_final_results()

    def print_raw_results(self):
        print(" " * 10, end="")
        for candidate in self.candidates:
            print("{:^18}".format("Candidate"), end="")
        print()
        print("Precinct  ", end="")
        for candidate in self.candidates:
            print(f"{candidate:^18}", end="")
        print()
        for index, result in enumerate(self.precincts):
            print(f"{(index + 1):^10}", end="")
            for i in range(len(self.candidates)):
                print(f"{str(result[i]):^18}", end="")
            print()

    def process_final_results(self):
        for name, result in self.results.items():
            self.final_results[name] = sum(result)
            self.total_votes += sum(result)

    def print_total_votes_by_candidate_name(self, name):
        if name in self.results:
            print(
                f"The total votes for {name}: {self.final_results[name]} out of {self.total_votes} votes"
            )
        else:
            print("Candidate name not found")

    def print_total_votes_for_all_candidates(self):
        print("\n")
        for candidate in self.candidates:
            self.print_total_votes_by_candidate_name(candidate)

    def get_winner(self):
        winner = ""
        for candidate, candidate_total in self.final_results.items():
            if candidate_total / self.total_votes > 0.49:
                winner = candidate
                break
        if winner == "":
            sorted_sores = sorted(self.final_results.values())
            runoff_a_value = sorted_sores[-1]
            runoff_b_value = sorted_sores[-2]
            runoff_a = ""
            runoff_b = ""
            for candidate in self.final_results.items():
                if candidate[1] == runoff_a_value:
                    runoff_a = candidate[0]
                if candidate[1] == runoff_b_value:
                    runoff_b = candidate[0]
            print(
                f"\nThe race will go to a runoff with candidates: {runoff_a} and {runoff_b}"
            )
        else:
            print(f"\nThe winner is {winner}")


# test code
em = ElectionsManager()
em.process_results("./candidates.csv")
em.print_raw_results()
em.print_total_votes_for_all_candidates()
em.get_winner()
