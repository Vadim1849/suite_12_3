import unittest

from tournament import Runner

def freeze_check(func):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        return func(self, *args, **kwargs)

    return wrapper


class RunnerTest(unittest.TestCase):

    is_frozen = False

    @freeze_check
    def test_walk(self):
        runner = Runner("ArbitraryRunnerName")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @freeze_check
    def test_run(self):
        runner = Runner("ArbitraryRunnerName")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @freeze_check
    def test_challenge(self):
        # создаются 2 объекта класса Runner с произвольными именами.
        runner1 = Runner("ArbitraryRunnerName1")
        runner2 = Runner("ArbitraryRunnerName2")

        # Далее 10 раз у объектов вызываются методы run и walk соответственно.
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)
        self.assertEqual(runner1.distance, 100)
        self.assertEqual(runner2.distance, 50)


if __name__ == '__main__':
    unittest.main()