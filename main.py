# main.py
# Fabien Couthouis
import os
import re
from functools import partial
from pygame import mixer

from kivy.app import App
from kivy.core.window import Window
from kivy.config import Config

from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import DragBehavior

from GenerateVoice import generate_voice


# VOICES_PATH = "sounds/voices/"
# INTRO_PATH = "sounds/intro/"
PATH = "sounds/"


class VoicePlay(App):

    def build(self):
        self.title = 'VoicePlay'
        self.sm = ScreenManager()

        self.layout_names = [name for name in os.listdir(PATH)]

        self.build_play_screen()
        self.build_add_screens()

        return self.sm

    def build_add_screens(self):
        screens = [Screen(name=name) for name in self.layout_names]
        for screen in screens:
            self.sm.add_widget(screen)
        return

    def build_play_screen(self):
        play_screen = Screen(name='play')
        self.sm.add_widget(play_screen)

        tab_names = self.layout_names
        self.layouts = {}

        tb_panel = TabbedPanel(do_default_tab=False,
                               tab_width=Window.width / len(tab_names))
        play_screen.add_widget(tb_panel)

        for layout_name in self.layout_names:
            layout = BoxLayout(orientation='vertical')
            self.layouts[layout_name] = layout
            self.add_audio_to_layout(layout_name)

            tabitem = TabbedPanelItem(text=layout_name)
            tabitem.add_widget(layout)
            tb_panel.add_widget(tabitem)

        return

    def get_path(self, layout_name):
        return "{}{}".format(PATH, layout_name)

    def add_audio_to_layout(self, layout_name):
        main_layout = self.layouts[layout_name]
        main_layout.clear_widgets()
        path = self.get_path(layout_name)

        filenames = os.listdir(path)

        i = 0
        subgrids = []
        subgrids.append(GridLayout(rows=1, cols=6))

        # Create subgrids and place btn according to his name : "n-xxx"
        for filename in filenames:
            if filename[0] != str(i+1):
                i += 1
                subgrids.append(GridLayout(rows=1, cols=6))

            btn = Button(text=self.format_filename(filename))
            btn.bind(on_release=partial(
                self.play_audio, filename, layout_name))
            subgrids[i].add_widget(btn)

        # Add created grids on main layout
        for subgrid in subgrids:
            main_layout.add_widget(subgrid)

        add_btn = Button(text="Ajouter", background_color=[
            0.7, 0.7, 1, 1])
        add_btn.bind(on_release=partial(self.add_file, layout_name))
        main_layout.add_widget(add_btn)

    def format_filename(self, filename):
        return re.sub("(.{15})", r"\1\n", filename, 0, re.DOTALL)

    def add_file(self, instruction, instance):
        screen = self.sm.get_screen(instruction)
        screen.clear_widgets()
        self.sm.current = instruction

        bl = BoxLayout(orientation='vertical')
        screen.add_widget(bl)

        label = TextInput(size_hint_y=None,
                          height=50, hint_text="Nom du fichier", multiline=False)
        bl.add_widget(label)

        ti = TextInput(hint_text="Entrer le texte à dire")
        bl.add_widget(ti)

        grid_btn = GridLayout(rows=1, cols=2, size_hint_y=None)
        bl.add_widget(grid_btn)

        cancel_btn = Button(text="Annuler", size_hint_y=None,
                            height=100)
        cancel_btn.bind(on_release=partial(self.return_to_main_screen))
        grid_btn.add_widget(cancel_btn)

        add_btn = Button(text="Ajouter", size_hint_y=None,
                         height=100)
        add_btn.bind(on_release=partial(
            self.generate_file, ti, label, instruction))
        grid_btn.add_widget(add_btn)

        return

    def generate_file(self, ti, label, layout_name, instance):
        path = self.get_path(layout_name)
        text = ti.text
        fname = label.text
        try:
            if text != "" and fname != "":
                generate_voice(text, os.path.join(
                    path, fname.replace('\t', '').replace('\n', '') + '.mp3'))
                self.add_audio_to_layout(layout_name)
                self.return_to_main_screen()
            else:
                raise ValueError("Champs manquants")
        except Exception as e:
            print(str(e))
            popup = Popup(title=str(e), content=Label(text="Erreur lors de l'ajout du fichier.\n\rVeillez à ce que que tous les champs soient remplis\net ne contiennent pas de caractères spéciaux."),
                          size_hint=(None, None), size=(400, 400))
            popup.open()

        return

    def return_to_main_screen(self, instance=None):
        self.sm.current = 'play'
        return

    def play_audio(self, fname, layout_name, instance):
        mixer.init()
        path = self.get_path(layout_name)
        mixer.music.load(os.path.join(path, fname))
        mixer.music.play()
        return


Config.set('kivy', 'window_icon', 'icon.ico')
Config.set('graphics', 'width', str(800))
Config.set('graphics', 'height', str(400))
VoicePlay().run()
