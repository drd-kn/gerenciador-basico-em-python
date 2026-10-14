import PySimpleGUI as sg

# Função responsável por criar a janela inicial da aplicação
def criar_janela_inicial():

    # Define o tema visual da aplicação
    sg.theme('DarkBlue4')

    # Cria a primeira linha da lista de tarefas
    # Checkbox permite marcar uma tarefa como concluída
    # Input permite digitar o nome ou a descrição da tarefa
    linha = [
        [
            sg.Checkbox('', background_color='#1E293B'),
            sg.Input(
                '',
                background_color='#334155',  # Cor de fundo do campo de texto
                text_color='white'           # Cor do texto digitado
            )
        ]
    ]

    # Define a organização dos elementos que aparecerão na janela
    layout = [

        # Cria um contêiner chamado "Tarefas"
        # Nele serão adicionadas as linhas com as tarefas
        [
            sg.Frame(
                'Tarefas',
                layout=linha,
                key='container',              # Identificador do contêiner
                background_color='#1E293B',   # Cor de fundo do contêiner
                title_color='#38BDF8'         # Cor do título "Tarefas"
            )
        ],

        # Cria os botões que ficarão abaixo da lista
        [
            sg.Button(
                'Nova Tarefa',
                button_color=('white', '#16A34A')  # Texto branco e fundo verde
            ),
            sg.Button(
                'Resetar',
                button_color=('white', '#DC2626')  # Texto branco e fundo vermelho
            )
        ]
    ]

    # Cria e retorna a janela com o título "Tarefas"
    # finalize=True permite acessar e modificar os elementos
    # da janela logo após sua criação
    return sg.Window(
        'Tarefas',
        layout=layout,
        background_color='#0F172A',  # Cor de fundo da janela
        finalize=True
    )


# Cria a janela inicial chamando a função definida acima
janela = criar_janela_inicial()


# Loop principal: mantém a aplicação aberta
# até que o usuário solicite o fechamento da janela
while True:

    # Lê os eventos (cliques, fechamento etc.)
    # e os valores dos campos de entrada
    event, values = janela.read()

    # Verifica se o usuário clicou no botão de fechar
    if event == sg.WIN_CLOSED:
        break  # Encerra o loop principal

    # Verifica se o usuário clicou em "Nova Tarefa"
    elif event == 'Nova Tarefa':

        # Adiciona uma nova linha ao contêiner de tarefas
        # Cada linha contém uma caixa de seleção e um campo de texto
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

    # Verifica se o usuário clicou em "Resetar"
    elif event == 'Resetar':

        # Fecha a janela atual
        janela.close()

        # Cria uma nova janela, voltando à configuração inicial
        # Isso remove visualmente as tarefas que foram adicionadas
        janela = criar_janela_inicial()


# Fecha a janela ao terminar o loop
janela.close()