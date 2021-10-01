from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard


class BookstagramHomeScreen(MDScreen):
    
    def refresh_callback(self, *args):
        print("Hello Refresh")
        

class MainCard(MDCard):
    pass
