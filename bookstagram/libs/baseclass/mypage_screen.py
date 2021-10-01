from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.bottomsheet import MDCustomBottomSheet

class BookstagramMypageScreen(MDScreen):
    
    def show_bottom_sheet(self):
        self.bottom_sheet = MDCustomBottomSheet(screen=ContentCustomSheet())
        self.bottom_sheet.open()

class ContentCustomSheet(MDBoxLayout):
    pass