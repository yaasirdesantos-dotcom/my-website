import time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.core.window import Window

# Rangi ya muonekano wa ndani (Cyberpunk Deep Dark)
Window.clearcolor = (0.05, 0.09, 0.15, 1)

# ================= 1. SPLASH SCREEN (JINA LAKO KUBWA) =================
class SplashScreen(Screen):
    def __init__(self, **kwargs):
        super(SplashScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=25, spacing=15)
        
        self.logo = Label(
            text="🚨\nDaladala Navigator", 
            font_size='36sp', 
            bold=True, 
            color=(0, 1, 0.8, 1), # Cyan Neon
            halign='center'
        )
        
        # NEMBO NA JINA LAKO LA USHINDI
        self.dev_name = Label(
            text="Designed by Senior Developer Yaasir", 
            font_size='20sp', 
            bold=True, 
            color=(1, 0.8, 0, 1), # Rangi ya Dhahabu inayong'aa
            halign='center'
        )
        
        self.loading_label = Label(
            text="Inapakia Mfumo wa Ruti na Nauli za LATRA...", 
            font_size='13sp', 
            color=(0.5, 0.6, 0.7, 1)
        )
        
        layout.add_widget(Label(text="")) # Balance ya juu
        layout.add_widget(self.logo)
        layout.add_widget(self.dev_name)
        layout.add_widget(self.loading_label)
        layout.add_widget(Label(text="© 2026 | Android Native Application", font_size='11sp', color=(0.3, 0.4, 0.5, 1)))
        
        self.add_widget(layout)

# ================= 2. MAIN INTERFACE (INJINI YA RUTI NA LATRA) =================
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        
        main_layout = BoxLayout(orientation='vertical', padding=15, spacing=12)
        
        # Kichwa cha App ya Ndani
        header = Label(
            text="Daladala Navigator 🚌", 
            font_size='24sp', 
            bold=True, 
            size_hint_y=None, 
            height=45,
            color=(0, 1, 0.8, 1)
        )
        main_layout.add_widget(header)
        
        sub_header = Label(
            text="Mifumo Rasmi ya Usafiri na Viwango vya LATRA Dar es Salaam",
            font_size='12sp',
            size_hint_y=None,
            height=25,
            color=(0.6, 0.7, 0.8, 1)
        )
        main_layout.add_widget(sub_header)
        
        # SPINNER YENYE RUTI NYINGI ZAIDI (ZILIZOONGEZWA)
        self.ruti_spinner = Spinner(
            text='-- Gusa Hapa Kuchagua Ruti --',
            values=(
                'Kimara kwenda Posta (BRT)',
                'Gongo la Mboto kwenda Kariakoo',
                'Mbagala Kuu kwenda Posta',
                'Tegeta Nyuki kwenda Mwenge',
                'Tabata Bima kwenda Kariakoo',
                'Temeke kwenda Muhimbili',
                'Ubungo kwenda Chalinze (Mikoani)',
                'Kigamboni (Ferry) kwenda Mwenge'
            ),
            size_hint_y=None,
            height=55,
            background_color=(0.09, 0.14, 0.23, 1),
            color=(1, 1, 1, 1)
        )
        main_layout.add_widget(self.ruti_spinner)
        
        # KITUFE CHA KUTAFUTA
        btn_tafuta = Button(
            text="Tafuta Usafiri na Nauli ⚡", 
            size_hint_y=None, 
            height=55,
            background_color=(0, 0.5, 1, 1), # Premium Blue
            font_size='16sp',
            bold=True
        )
        btn_tafuta.bind(on_press=self.tafuta_usafiri)
        main_layout.add_widget(btn_tafuta)
        
        # MAJIBU YENYE PANEL YA KIJASUSI
        self.lbl_safari = Label(text="", font_size='15sp', halign='center', color=(1, 1, 1, 1))
        self.lbl_gari = Label(text="", font_size='15sp', halign='center', color=(0.7, 0.9, 1, 1))
        self.lbl_kituo = Label(text="", font_size='14sp', halign='center', color=(0.8, 0.8, 0.8, 1))
        self.lbl_nauli = Label(text="", font_size='16sp', bold=True, halign='center', color=(0, 1, 0.8, 1))
        
        main_layout.add_widget(self.lbl_safari)
        main_layout.add_widget(self.lbl_gari)
        main_layout.add_widget(self.lbl_kituo)
        main_layout.add_widget(self.lbl_nauli)
        
        # Hakiri ya Senior Developer chini kabisa
        main_layout.add_widget(Label(
            text="App Core Engine by Developer Yaasir", 
            font_size='12sp', 
            color=(0.3, 0.4, 0.5, 1), 
            size_hint_y=None, 
            height=20
        ))
        
        self.add_widget(main_layout)

    # LOGIC YA RUTI, VITUO, MAGARI NA VIWANGO VYA LATRA
    def tafuta_usafiri(self, instance):
        mchaguo = self.ruti_spinner.text
        
        if mchaguo == '-- Gusa Hapa Kuchagua Ruti --':
            self.lbl_nauli.text = "Tafadhali chagua ruti kuona mifumo!"
            self.lbl_safari.text = ""
            self.lbl_gari.text = ""
            self.lbl_kituo.text = ""
            return
            
        if mchaguo == 'Kimara kwenda Posta (BRT)':
            self.lbl_safari.text = "📍 Safari: Kimara Mwisho ➔ Posta Mpya"
            self.lbl_gari.text = "🚌 Usafiri: Mwendokasi BRT (Express & Kawaida)"
            self.lbl_kituo.text = "🏢 Kituo Kikuu: Terminal ya Kimara"
            self.lbl_nauli.text = "💰 Nauli ya LATRA: 750 TZS (Wanafunzi: 300 TZS)"
            
        elif mchaguo == 'Gongo la Mboto kwenda Kariakoo':
            self.lbl_safari.text = "📍 Safari: Gongo la Mboto ➔ Kariakoo (Mnazi Mmoja)"
            self.lbl_gari.text = "🚌 Usafiri: Daladala Kubwa (Coaster / Eicher)"
            self.lbl_kituo.text = "🏢 Kituo Kikuu: Stendi ya Gongo la Mboto"
            self.lbl_nauli.text = "💰 Nauli ya LATRA: 700 TZS (Wanafunzi: 200 TZS)"
            
        elif mchaguo == 'Mbagala Kuu kwenda Posta':
            self.lbl_safari.text = "📍 Safari: Mbagala Rangi Tatu ➔ Posta"
            self.lbl_gari.text = "🚌 Usafiri: Daladala za Kawaida / Mwendokasi (BRT)"
            self.lbl_kituo.text = "🏢 Kituo Kikuu: Terminal ya Mbagala"
            self.lbl_nauli.text = "💰 Nauli ya LATRA: 600 TZS (Wanafunzi: 200 TZS)"
            
        elif mchaguo == 'Tegeta Nyuki kwenda Mwenge':
            self.lbl_safari.text = "📍 Safari: Tegeta Nyuki ➔ Mwenge Terminal"
            self.lbl_gari.text = "🚌 Usafiri: Daladala (Scania / Coaster / Hiace)"
            self.lbl_kituo.text = "🏢 Kituo Kikuu: Kituo cha Tegeta Nyuki"
            self.lbl_nauli.text = "💰 Nauli ya LATRA: 600 TZS (Wanafunzi: 200 TZS)"
            
        elif mchaguo == 'Tabata Bima kwenda Kariakoo':
            self.lbl_safari.text = "📍 Safari: Tabata Bima ➔ Kariakoo (Stendi)"
            self.lbl_gari.text = "🚌 Usafiri: Daladala Ndogo na Kubwa (Eicher/Hiace)"
            self.lbl_kituo.text = "🏢 Kituo Kikuu: Njia Panda ya Bima"
            self.lbl_nauli.text = "💰 Nauli ya LATRA: 500 TZS (Wanafunzi: 200 TZS)"
            
        elif mchaguo == 'Temeke kwenda Muhimbili':
            self.lbl_safari.text = "📍 Safari: Temeke Hospitali ➔ Hospitali ya Muhimbili"
            self.lbl_gari.text = "🚌 Usafiri: Daladala Maalum za Hospitali"
            self.lbl_kituo.text = "🏢 Kituo Kikuu: Stendi ya Temeke Mwisho"
            self.lbl_nauli.text = "💰 Nauli ya LATRA: 600 TZS (Wanafunzi: 200 TZS)"
            
        elif mchaguo == 'Ubungo kwenda Chalinze (Mikoani)':
            self.lbl_safari.text = "📍 Safari: Ubungo Shekilango ➔ Chalinze Stendi"
            self.lbl_gari.text = "🚌 Usafiri: Coaster za Mikoani / Mabasi ya SGR"
            self.lbl_kituo.text = "🏢 Kituo Kikuu: Kituo cha Ubungo"
            self.lbl_nauli.text = "💰 Nauli ya LATRA: 3,000 TZS (Mabasi ya Kati)"
            
        elif mchaguo == 'Kigamboni (Ferry) kwenda Mwenge':
            self.lbl_safari.text = "📍 Safari: Kigamboni Ferry ➔ Mwenge kupitia Daraja"
            self.lbl_gari.text = "🚌 Usafiri: Daladala Kubwa (Ruta za Darajani)"
            self.lbl_kituo.text = "🏢 Kituo Kikuu: Geti la Kigamboni Ferry"
            self.lbl_nauli.text = "💰 Nauli ya LATRA: 700 TZS (Wanafunzi: 200 TZS)"

# ================= 3. MWONGOZO WA APP NA TIMER =================
class DaladalaApp(App):
    def build(self):
        self.title = "Daladala Navigator"
        sm = ScreenManager()
        
        sm.add_widget(SplashScreen(name='splash'))
        sm.add_widget(MainScreen(name='main'))
        
        # Splash screen ikae sekunde 3 kukuza jina lako halafu iingie kwenye App
        Clock.schedule_once(lambda dt: setattr(sm, 'current', 'main'), 3)
        
        return sm

if __name__ == '__main__':
    DaladalaApp().run()

