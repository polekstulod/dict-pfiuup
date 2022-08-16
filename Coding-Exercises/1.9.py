class ClubMembers:

    def __init__(self, name, birthday, age, favorite_food, goal):
        self.name = name
        self.birthday = birthday
        self.age = age
        self.favorite_food = favorite_food
        self.goal = goal

    def display_1(self):
        print(f'Name: {self.name}')
        print(f'Birthday: {self.birthday}')
        print(f'Age: {self.age}')
        print(f'Favorite Food: {self.favorite_food}')
        print(f'Goal: {self.goal}')


class ClubOfficers(ClubMembers):

    def __init__(self, name, birthday, age, favorite_food, goal, position):
        super().__init__(name, birthday, age, favorite_food, goal)
        self.position = position

    def display_2(self):
        print(f'Name: {self.name}')
        print(f'Birthday: {self.birthday}')
        print(f'Age: {self.age}')
        print(f'Favorite Food: {self.favorite_food}')
        print(f'Goal: {self.goal}')
        print(f'Position: {self.position}')


m_1 = ClubMembers('Tom', 'January 16', '14', 'Ice Cream', 'To be happy')
o_4 = ClubOfficers('Vera', 'June 22', '16', 'Beef stroganoff', "To be the world's greatest chef", 'Treasurer')

m_1.display_1()
o_4.display_2()
