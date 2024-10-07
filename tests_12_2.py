import unittest
from tournament import Runner,Tournament

class TournamentTest(unittest.TestCase):
    all_results ={}

    @classmethod
    def setUpClass(cls): #создаём атрибут для хранения результатов теста
        cls.all_results = {}
    def setUp(self): #создаём бегунов
        self.runner1 = Runner('Усэйн',10)
        self.runner2 = Runner('Андрей',9)
        self.runner3 = Runner('Ник',3)
    @classmethod #вывод всех результатов тестов в столбик
    def tearDownClass(cls): #выводим результат
        print('\nРезультат всех тестов')
        for place,runner in sorted(cls.all_results.items()):
            print(f'Место {place}: {runner}')


#имитируем забеги
    def test1(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(1 in results)
        self.assertTrue(results[1].name == 'Усэйн') #первое место у Усэйн

    def test2(self):
        tournament = Tournament(90,  self.runner2, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(1 in results)
        self.assertTrue(results[1].name == 'Андрей') #Андрей должен занять первое место

    def test3(self):
        tournament = Tournament(90, self.runner1,self.runner2,self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(1 in results)
        self.assertTrue(results[1].name == 'Усэйн')
        self.assertTrue(results[2].name == 'Андрей')
        self.assertTrue(results[3].name == 'Ник') #проверила, что Ник последний
if __name__ == '__main__':
    unittest.main()
