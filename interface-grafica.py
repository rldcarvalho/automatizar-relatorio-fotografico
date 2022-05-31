import PySimpleGUI as sg


def criar_janela(manutencao, poda, limpeza):
    # definição do Layout
    sg.theme('Dark Grey 13')
    layout_inicial = [
        [sg.Text('Qual o tipo de Croqui?')],
        [sg.Radio('Manutenção', "Radio1", default=False, key='manutencao'),
         sg.Radio('Poda', "Radio1", default=False, key='poda'),
         sg.Radio('Limpeza de Faixa', "Radio1", default=False, key='limpeza')],
        [sg.Button('OK')]
    ]

    layout_manutencao = [
        [sg.Text('Croqui de Manutenção')],
        [sg.Text('Foto 1')],
        [sg.Input(key='foto1'), sg.FileBrowse()],
        [sg.Text('Foto 2')],
        [sg.Input(key='foto2'), sg.FileBrowse()],
        [sg.Text('Gemini')],
        [sg.Input(key='gemini'), sg.FileBrowse()],
        [sg.Button('Gerar Relatório')]
    ]

    layout_poda = [
        [sg.Text('Croqui de Poda')],
        [sg.Text('Foto 1')],
        [sg.Input(key='foto1'), sg.FileBrowse()],
        [sg.Text('Gemini')],
        [sg.Input(key='gemini'), sg.FileBrowse()],
        [sg.Text('Coord 1:'), sg.Input(key='coord1')],
        [sg.Text('Coord 2:'), sg.Input(key='coord2')],
        [sg.Button('Gerar Relatório')]
    ]

    layout_limpeza = [
        [sg.Text('Croqui de Limpeza de Faixa')],
        [sg.Text('Foto 1')],
        [sg.Input(key='foto1'), sg.FileBrowse()],
        [sg.Text('Foto 2')],
        [sg.Input(key='foto2'), sg.FileBrowse()],
        [sg.Text('Gemini')],
        [sg.Input(key='gemini'), sg.FileBrowse()],
        [sg.Text('Coord 1:'), sg.Input(key='coord1')],
        [sg.Text('Coord 2:'), sg.Input(key='coord2')],
        [sg.Text('Coord 3:'), sg.Input(key='coord3')],
        [sg.Button('Gerar Relatório')]
    ]
    # criação da Janela
    if manutencao == True:
        return sg.Window("Croqui de Manutenção").layout(layout_manutencao)
    elif poda == True:
        return sg.Window("Croqui de Poda").layout(layout_poda)
    elif limpeza == True:
        return sg.Window("Croqui de Limpeza de Faixa").layout(layout_limpeza)
    else:
        return sg.Window("Tipo de Croqui").layout(layout_inicial)


def principal():
    janela = criar_janela(False, False, False)

    while True:
        event, values = janela.Read()
        print(event, values)
        if event == sg.WIN_CLOSED:
            break
        if event == "Gerar Relatório":
            return values
        if event == "OK":
            manutencao = values['manutencao']
            poda = values['poda']
            limpeza = values['limpeza']
            janela.close()
            janela = criar_janela(manutencao, poda, limpeza)
        # fotos = [self.values['foto1'], self.values['foto2']]
        # gemini = self.values['gemini']
        # coords = [self.values['coord1'], self.values['coord2'], self.values['coord3']]
        # print(fotos)
        # print(gemini)
        # print(coords)
    janela.close()


if __name__ == '__main__':
    principal()
