from kivy.lang import Builder
from kivymd.app import MDApp


class Cards500(MDApp):

    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(
            '''
MDScreen:

    MDBottomNavigation:
        #panel_color: "#ffffff"
        selected_color_background: "#f6eeee"
        text_color_active: "#222325"
        
        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'профиль'
            icon: 'cat'
            
            MDBoxLayout:
                orientation: "horizontal"
                #md_bg_color:  "#999999"
                pos_hint: {"top": .97, "center_x": .5}
                spacing: "10dp"
                size_hint: .92, .2
                        
                MDBoxLayout:
                    orientation: "vertical"
                    size_hint: .6, 1
                    #md_bg_color: "#55f55f"
                    spacing: "1dp"
                    padding: "16dp", "35dp"
                   
                    MDLabel:
                        text: "Имя профиля"
                        font_style: "H5"
                        bold: True
                        pos_hint: {"top": .9, "left": .5}
                        adaptive_height: True
                        
                    MDLabel:
                        text: "Статус cтатус статус"
                        theme_text_color: "Hint"
                        adaptive_height: True
                    
                MDBoxLayout:
                    #md_bg_color:  "#88ff88"
                    size_hint: .3, 1
                    height: self.width
                    
                    FitImage:
                        source: "avatar_pic.jpg"
                        radius: [16, 16, 16, 16 ]
                        
                        
                    
            MDCard:
                orientation: "vertical"
                adaptive_size: True
                spacing: "56dp"
                size_hint: .92, .2
                pos_hint: {"top": .735, "center_x": .5}
                shadow_softness: 2
                md_bg_color: "#f6eeee"
                ripple_behavior: True
                ripple_color: "#ffffff"#
                
            MDCard:
                orientation: "vertical"
                adaptive_size: True
                spacing: "56dp"
                size_hint: .92, .2
                pos_hint: {"top": .485, "center_x": .5}
                shadow_softness: 2
                md_bg_color: "#f6eeee"
                ripple_behavior: True
                ripple_color: "#ffffff"
            
            MDCard:
                orientation: "vertical"
                adaptive_size: True
                spacing: "56dp"
                size_hint: .92, .2
                pos_hint: {"top": .235, "center_x": .5}
                shadow_softness: 2
                ripple_behavior: True
                md_bg_color: "#f6eeee"
                ripple_color: "#ffffff"


        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'открытые'
            icon: 'bird'

            MDLabel:
                text: 'Открытые игры'
                font_style:"Subtitle1" ##['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'Subtitle1', 'Subtitle2', 'Body1', 'Body2', 'Button', 'Caption', 'Overline', 'Icon']

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'создать игру'
            icon: 'plus'

            MDLabel:
                text: 'Меню'
                halign: 'center'
'''
        )


Cards500().run()