from datetime import datetime
class WeeklyMenu:
    def __init__(self):
        self.menu = {
            'Monday': [],
            'Tuesday': [],
            'Wednesday': [],
            'Thursday': [],
            'Friday': [],
            'Saturday': [],
            'Sunday': []
        }
    def add_item_to_day(self, day, item):
        if day in self.menu: self.menu[day].append(item)
        else: print(f"{day} is not a valid")
    def upd_item_from_day(self, day, old, new):
        if day in self.menu:
            if old in self.menu[day]: self.menu[day][self.menu[day].index(old)] = new
            else: print(f"{old} not found in menu for {day}")
        else: print(f"{day} is not a valid")
    def display_todays_menu(self):  
        day = datetime.now().strftime('%A')
        menu = self.menu.get(day, 'Menu not available')
        if menu == 'Menu not available': print('Menu not available')
        else:
            print(f"{day}'s Menu")
            for item in menu: print(f"- {item}")
menu = WeeklyMenu()
menu.add_item_to_day('Saturday', '1')
menu.display_todays_menu()
