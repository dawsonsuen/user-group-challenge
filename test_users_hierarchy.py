import unittest
from users_hierarchy import UsersHierarchy

# Unit test users_hierarchy
class TestUsersHierarchy(unittest.TestCase):
    def test_getSubOrdinates(self):
        
        users_hierarchy = UsersHierarchy(None)

        # Test cases from the examples
        print('Test: returns all subordinates of User Id 3:')
        self.assertEqual(users_hierarchy.getSubOrdinates(3), [{"Id": 2,"Name": "Emily Employee","Role": 4}, {"Id": 5, "Name": "Steve Trainer","Role": 5}])
        print('Test: returns all subordinates of User Id 1:')
        self.assertEqual(users_hierarchy.getSubOrdinates(1), [{"Id": 2,"Name": "Emily Employee","Role": 4}, {"Id": 3,"Name": "Sam Supervisor","Role": 3}, {"Id": 4,"Name": "Mary Manager","Role": 2}, {"Id": 5, "Name": "Steve Trainer","Role": 5}])
        
        # Test cases for User Id 2
        print('Test: returns all subordinates of User Id 2:')
        self.assertEqual(users_hierarchy.getSubOrdinates(2), [{"Id": 5,"Name": "Steve Trainer","Role": 5}])

def main():
    test = TestUsersHierarchy()
    test.test_getSubOrdinates()

if __name__ == '__main__':
    main()