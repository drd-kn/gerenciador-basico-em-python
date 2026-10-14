import PySimpleGUI as sg

def criar_janela_inicial():
    sg.theme('DarkBlue4')

    linha = [
        [
            sg.Checkbox('', background_color='#1E293B'),
            sg.Input(
                '',
                background_color='#334155',
                text_color='white'
            )
        ]
    ]

    layout = [
        [
            sg.Frame(
                'Tarefas',
                layout=linha,
                key='container',
                background_color='#1E293B',
                title_color='#38BDF8'
            )
        ],
        [
            sg.Button(
                'Nova Tarefa',
                button_color=('white', '#16A34A')
            ),
            sg.Button(
                'Resetar',
                button_color=('white', '#DC2626')
            )
        ]
    ]

    return sg.Window(
        'Tarefas',
        layout=layout,
        background_color='#0F172A',
        finalize=True
    )

janela = criar_janela_inicial()

while True:
    event, values = janela.read()

    if event == sg.WIN_CLOSED:
        break

    elif event == 'Nova Tarefa':
        janela.extend_layout(
            janela['container'],
            [[
                sg.Checkbox('', background_color='#1E293B'),
                sg.Input(
                    '',
                    background_color='#334155',
                    text_color='white'
                )
            ]]
        )

    elif event == 'Resetar':
        janela.close()
        janela = criar_janela_inicial()

janela.close()