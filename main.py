from kivy.app import App
from functions import palavras
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.properties import ListProperty
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.animation import Animation


class Manager(ScreenManager):
    pass


class MainMenu(Screen):  # menu principal
    def on_pre_enter(self):
        Window.bind(on_request_close=self.confirmacao)

    def confirmacao(self, *args, **kwargs):
        box = BoxLayout(orientation='vertical', padding=10, spacing=10)
        botoes = BoxLayout(padding=10, spacing=10)

        pop = Popup(title='Deseja mesmo sair?', content=box, size_hint=(None, None), size=(150, 150))

        sim = Botao1(text='Sim', on_release=App.get_running_app().stop)
        nao = Botao1(text='Não', on_release=pop.dismiss)
        botoes.add_widget(sim)
        botoes.add_widget(nao)

        atencao = Image(source='atencao.png')
        box.add_widget(atencao)
        box.add_widget(botoes)


class Botao1(ButtonBehavior, Label):  # criação de botões em python
    cor = ListProperty([0.1, 0.5, 0.7, 1])
    cor2 = ListProperty([0.1, 0.1, 0.1, 1])

    def __init__(self, **kwargs):
        super(Botao1, self).__init__(**kwargs)
        self.atualizar()

    def on_pos(self, *args):
        self.atualizar()

    def on_size(self, *args):
        self.atualizar()

    def atualizar(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=self.cor)
            Ellipse(size=(self.height, self.height),
                    pos=self.pos)
            Ellipse(size=(self.height, self.height),
                    pos=(self.x + self.width - self.height, self.y))
            Rectangle(size=(self.width - self.height, self.height),
                      pos=(self.x + self.height / 2, self.y))


class PlayMenu(Screen):  # menu com as fases do jogo
    pass


class FaseUm(Screen):
    def on_enter(self, fase=palavras.fases[0], **kwargs):
        super().__init__(**kwargs)
        for v in fase.values():
            self.ids.box.add_widget(words(text=v))


class FaseUmCerto(Screen):
    def on_enter(self, fase=palavras.fases[0], **kwargs):
        super().__init__(**kwargs)
        for k, v in fase.items():
            self.ids.boxcerto.add_widget(WordsComplete(text=k))


class words(BoxLayout):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.ids.label1.text = text


class WordsComplete(BoxLayout):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text

# FASE 2


class FaseDois(Screen):
    def on_enter(self, fase=palavras.fases[2], **kwargs):
        super().__init__(**kwargs)
        for v in fase.values():
            self.ids.box2.add_widget(Words2(text=v))


class FaseDoisCerto(Screen):
    def on_enter(self, fase=palavras.fases[2], **kwargs):
        super().__init__(**kwargs)
        for k, v in fase.items():
            self.ids.boxcerto2.add_widget(WordsComplete2(text=k))


class Words2(BoxLayout):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.ids.label2.text = text


class WordsComplete2(BoxLayout):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.ids.labelc2.text = text


# FASE TRÊS

class FaseTres(Screen):
    def on_enter(self, fase=palavras.fases[4], **kwargs):
        super().__init__(**kwargs)
        for v in fase.values():
            self.ids.box3.add_widget(Words3(text=v))


class FaseTresCerto(Screen):
    def on_enter(self, fase=palavras.fases[4], **kwargs):
        super().__init__(**kwargs)
        for k, v in fase.items():
            self.ids.boxcerto3.add_widget(WordsComplete3(text=k))


class Words3(BoxLayout):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.ids.label3.text = text


class WordsComplete3(BoxLayout):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.ids.labelc3.text = text


# FASE QUATRO


class FaseQuatro(Screen):
    def on_enter(self, fase=palavras.fases[7], **kwargs):
        super().__init__(**kwargs)
        for v in fase.values():
            self.ids.box4.add_widget(Words4(text=v))


class FaseQuatroCerto(Screen):
    def on_enter(self, fase=palavras.fases[7], **kwargs):
        super().__init__(**kwargs)
        for k, v in fase.items():
            self.ids.boxcerto4.add_widget(WordsComplete4(text=k))


class Words4(BoxLayout):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.ids.label4.text = text


class WordsComplete4(BoxLayout):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.ids.labelc4.text = text


# FASE CINCO


class FaseCinco(Screen):
    def on_enter(self, fase=palavras.fases[10], **kwargs):
        super().__init__(**kwargs)
        for v in fase.values():
            self.ids.box5.add_widget(Words5(text=v))


class FaseCincoCerto(Screen):
    def on_enter(self, fase=palavras.fases[10], **kwargs):
        super().__init__(**kwargs)
        for k, v in fase.items():
            self.ids.boxcerto5.add_widget(WordsComplete5(text=k))


class Words5(BoxLayout):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.ids.label5.text = text


class WordsComplete5(BoxLayout):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.ids.labelc5.text = text


# FASE SEIS


class FaseSeis(Screen):
    def on_enter(self, fase=palavras.fases[1], **kwargs):
        super().__init__(**kwargs)
        for v in fase.values():
            self.ids.box6.add_widget(Words6(text=v))


class FaseSeisCerto(Screen):
    def on_enter(self, fase=palavras.fases[1], **kwargs):
        super().__init__(**kwargs)
        for k, v in fase.items():
            self.ids.boxcerto6.add_widget(WordsComplete6(text=k))


class Words6(BoxLayout):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.ids.label6.text = text


class WordsComplete6(BoxLayout):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.ids.labelc6.text = text

# FASE SETE


class FaseSete(Screen):
    def on_enter(self, fase=palavras.fases[6], **kwargs):
        super().__init__(**kwargs)
        for v in fase.values():
            self.ids.box7.add_widget(Words7(text=v))


class FaseSeteCerto(Screen):
    def on_enter(self, fase=palavras.fases[6], **kwargs):
        super().__init__(**kwargs)
        for k, v in fase.items():
            self.ids.boxcerto7.add_widget(WordsComplete7(text=k))


class Words7(BoxLayout):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.ids.label7.text = text


class WordsComplete7(BoxLayout):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.ids.labelc7.text = text


# FASE OITO


class FaseOito(Screen):
    def on_enter(self, fase=palavras.fases[9], **kwargs):
        super().__init__(**kwargs)
        for v in fase.values():
            self.ids.box8.add_widget(Words8(text=v))


class FaseOitoCerto(Screen):
    def on_enter(self, fase=palavras.fases[9], **kwargs):
        super().__init__(**kwargs)
        for k, v in fase.items():
            self.ids.boxcerto8.add_widget(WordsComplete8(text=k))


class Words8(BoxLayout):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.ids.label8.text = text


class WordsComplete8(BoxLayout):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.ids.labelc8.text = text

# FASE NOVE


class FaseNove(Screen):
    def on_enter(self, fase=palavras.fases[5], **kwargs):
        super().__init__(**kwargs)
        for v in fase.values():
            self.ids.box9.add_widget(Words9(text=v))


class FaseNoveCerto(Screen):
    def on_enter(self, fase=palavras.fases[5], **kwargs):
        super().__init__(**kwargs)
        for k, v in fase.items():
            self.ids.boxcerto9.add_widget(WordsComplete9(text=k))


class Words9(BoxLayout):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.ids.label9.text = text


class WordsComplete9(BoxLayout):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.ids.labelc9.text = text


# FASE DEZ


class FaseDez(Screen):
    def on_enter(self, fase=palavras.fases[8], **kwargs):
        super().__init__(**kwargs)
        for v in fase.values():
            self.ids.box10.add_widget(Words10(text=v))


class FaseDezCerto(Screen):
    def on_enter(self, fase=palavras.fases[8], **kwargs):
        super().__init__(**kwargs)
        for k, v in fase.items():
            self.ids.boxcerto10.add_widget(WordsComplete10(text=k))


class Words10(BoxLayout):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.ids.label10.text = text


class WordsComplete10(BoxLayout):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.ids.labelc10.text = text


# FASE ONZE


class FaseOnze(Screen):
    def on_enter(self, fase=palavras.fases[3], **kwargs):
        super().__init__(**kwargs)
        for v in fase.values():
            self.ids.box11.add_widget(Words11(text=v))


class FaseOnzeCerto(Screen):
    def on_enter(self, fase=palavras.fases[3], **kwargs):
        super().__init__(**kwargs)
        for k, v in fase.items():
            self.ids.boxcerto11.add_widget(WordsComplete11(text=k))


class Words11(BoxLayout):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.ids.label11.text = text


class WordsComplete11(BoxLayout):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.ids.labelc11.text = text


class Literacy(App):
    def build(self):
        self.icon = 'menuButton.png'


Literacy().run()
