class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed*2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants[:]: #скопировала список для безопасного удаления
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers
    #создали бегунов
runner1 = Runner('Усэйн',10)
runner2 =Runner('Андрей',9)
runner3 =Runner('Ник',3)
#создали турнир
tournament = Tournament(90,runner1,runner2,runner3)
#запускаем турнир
results = tournament.start()
for place, runner in sorted(results.items()):
    print(f'Место {place}: {runner}')