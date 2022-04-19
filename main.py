from calculadora_factories import make_display, make_root, make_buttons, make_label

from calculadora_class import Calculadora

def main():
    root = make_root()
    display = make_display(root)
    label = make_label(root)
    buttons = make_buttons(root)
    calculadora = Calculadora(root, label, display, buttons)
    calculadora.start()



if __name__ == '__main__':
    main()
