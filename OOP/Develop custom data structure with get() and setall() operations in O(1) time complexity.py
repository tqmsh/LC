from datetime import datetime 
import unittest 
from time import sleep

class O1setAll:
    def __init__(self):
        self.mp = {}
        self.k_lst = {}
        self.all_lst = 0
        self.all_val = None 

    def set(self, k, v):
        self.mp[k] = v
        self.k_lst[k] = datetime.now().timestamp()

    def get(self, k):
        if k in self.k_lst and self.all_lst < self.k_lst[k]:
            return self.mp[k]
        return self.all_val

    def setAll(self, val):
        self.all_lst = datetime.now().timestamp()
        self.all_val = val



class TestO1setAll(unittest.TestCase):
    def test_set_and_get(self):
        obj = O1setAll()
        
        # Test setting and getting a single value
        obj.set('a', 10)
        self.assertEqual(obj.get('a'), 10)
        
        # Test updating a value
        obj.set('a', 20)
        self.assertEqual(obj.get('a'), 20)
        
        # Test setting and getting multiple values
        obj.set('b', 30)
        self.assertEqual(obj.get('a'), 20)
        self.assertEqual(obj.get('b'), 30)
        
    def test_setAll(self):
        obj = O1setAll()
        
        # Test setAll with no previous values
        obj.setAll(100)
        self.assertEqual(obj.get('a'), 100)
        self.assertEqual(obj.get('b'), 100)
        
        # Test setAll with previous values
        obj.set('a', 10)
        obj.set('b', 20)
        sleep(0.01)  # Ensure a time difference
        obj.setAll(50)
        self.assertEqual(obj.get('a'), 50)
        self.assertEqual(obj.get('b'), 50)
        
    def test_set_after_setAll(self):
        obj = O1setAll()
        
        # Test set after setAll
        obj.setAll(100)
        obj.set('a', 10)
        self.assertEqual(obj.get('a'), 10)
        self.assertEqual(obj.get('b'), 100)
        
        # Test setAll after set
        sleep(0.01)  # Ensure a time difference
        obj.setAll(200) 
        self.assertEqual(obj.get('a'), 200)
        self.assertEqual(obj.get('b'), 200)
        
if __name__ == '__main__':
    unittest.main()
