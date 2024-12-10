import unittest
import runner



class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        """
        Test_walk - метод, в котором создается объект класса Runner с произвольным именем.
        Далее вызовите метод walk у этого объекта 10 раз.
        После чего методом assertEqual сравните distance этого объекта со значением 50.
        """
        rn = runner.Runner(name='Faster')
        for _ in range(10):
            rn.walk()
        self.assertEqual(rn.distance, 50 )

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        """
        Test_run - метод, в котором создается объект класса Runner с произвольным именем.
        Далее вызовите метод run у этого объекта 10 раз.
        После чего методом assertEqual сравните distance этого объекта со значением 100.
        """
        rn = runner.Runner(name='Faster')
        for _ in range(10):
            rn.run()
        self.assertEqual(rn.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        """
        Test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами.
        Далее 10 раз у объектов вызываются методы run и walk соответственно.
        Т.к. Дистанции должны быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.
        """
        rna = runner.Runner(name='RNA')
        rnb = runner.Runner(name='RNB')
        for _ in range(10):
            rna.run()
            rnb.walk()
            self.assertNotEqual(rna.distance, rnb.distance)

if __name__ == '__main__':
    unittest.main()













