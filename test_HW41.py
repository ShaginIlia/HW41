import unittest
import HW41


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = HW41.Runner('Usain', 10)
        self.runner_2 = HW41.Runner('Andrey', 9)
        self.runner_3 = HW41.Runner('Nik', 3)

    @classmethod
    def tearDownClass(cls):
        print('Результаты: ')
        for key, value in cls.all_results.items():
            print(value)

    def test_Tournament1(self):
        tournament = HW41.Tournament(90, self.runner_1, self.runner_3)
        results = tournament.start()
        self.assertTrue(results[len(results)] == 'Nik')
        self.all_results['Usain and Nick'] = results

    def test_Tournament2(self):
        tournament = HW41.Tournament(90, self.runner_3, self.runner_2)
        results = tournament.start()
        self.assertTrue(results[len(results)] == 'Nik')
        self.all_results['Andrey and Nick'] = results

    def test_Tournament3(self):
        tournament = HW41.Tournament(90, self.runner_3, self.runner_2, self.runner_1)
        results = tournament.start()
        self.assertTrue(results[len(results)] == 'Nik')
        self.all_results['Usain, Andrey and Nick'] = results


if __name__ == '__main__':
    unittest.main()
