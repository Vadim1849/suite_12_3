import unittest
import runner_test
import tournament_test


def load_tests(loader, tests, pattern):
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(runner_test.RunnerTest))
    suite.addTests(loader.loadTestsFromTestCase(tournament_test.TournamentTest))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(load_tests(unittest.TestLoader(), None, None))
