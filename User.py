class User:
        def __init__(self, name, email = None, drivers_licence = None, number = None):
            self.name = name
            self.email = email
            self.drivers_license = drivers_licence
            self.number = number 
        



def test_user_creation():
    user1 = User("Alice", "alice@example.com")
    assert user1.name == "Alice"
    assert user1.email == "alice@example.com"
    assert user1.drivers_license is None
    assert user1.number is None

    user2 = User("Bob", "bob@example.com", "XYZ123")
    assert user2.name == "Bob"
    assert user2.email == "bob@example.com"
    assert user2.drivers_license == "XYZ123"
    assert user2.number is None

 