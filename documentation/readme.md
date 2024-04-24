# Documentação da Clínica Vision

## Tipografia
- Título: Raleway font-size: 30px
- Subtítulo font-size: 20px
- Conteúdo: Montserrat font-size: 18px
- Descrições font-size: 16px
- Inputs heigth: 40px

``` html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Raleway:wght@400;500;600;700&display=swap" rel="stylesheet">
```

``` css
font-family: 'Montserrat', sans-serif;
font-family: 'Raleway', sans-serif;
```

#### MOBILE
- Header font-size 14
- Título Font-size 16
- Subtítulo Font-size 14
- Descrição font-size 12

## Paleta de cores
``` css
#44403F
#031D38
#031D38
#160041
#337F98
#3F95A9
#66B5C4
#A2D3E1
#C8E2DF
#F1F1F1
#EDD604
#1FC625
#FF0000
#D9D9D9
```

## Imagens
Para acessar as imagens no Trello [Clique aqui](https://trello.com/c/Ff6wbnJp).

## Login
A faixa azul superior está apenas com o telefone. Na faixa branca: o logo fica à esquerda, no meio a mensagem [Olá! “Nome-do-usuário“] e à direita dois links (em formato de botão) [VOLTAR] [LOGOUT].

- Selecionar o tipo de acesso ADM, usuário ou funcionário.
- Criar cadastro.
- Recuperar Senha.
- Login + botões para acessar com Google, Facebook e Apple.
- Inputs: e-mail, senha.
- Texto e link
- Botão Login

## Administrador
O administrador vai ter acesso ao Banco de dados e agendamentos em formato de tabelas.

Tendo opções para acrescentar, alterar ou excluir.

Quando clicar no nome, será direcionado a dados mais completos.

BANCO DE DADOS
- Criar acesso de usuários
- Funcionários (Lista com nome, CPF)

Nome, cargo, CRM, data de nascimento, RG, CPF, telefone, e-mail, endereço
- Pacientes (Lista com nome, CPF)

Nome, RG, CPF, Data de Nascimento, Telefone, e-mail, endereço, convênio, número da carteirinha, histórico de agendamento.

- Dados da clínica

CNPJ, Razão Social, Nome fantasia, Endereço, horário de funcionamento.

### ACESSAR AGENDAMENTOS

Lista com todas as consultas e exames agendados.

Terá um botão para alterar agendamento ou cancelar.

## Acesso Funcionários
Vamos ter 2 opções de perfil (médico e atendente)

### Perfil Médico
- Visualização das consultas agendadas.

Data, hora e paciente.

- Prontuário.

Descrição das consultas e exames realizados, histórico médico de doenças de cada paciente.

### Perfil Atendente

- Banco de dados dos pacientes.

Nome, gênero, telefone, endereço, e-mail, convênio e CPF.

- Consultas e exames agendados - Permissão para agendar e cancelar (em caso de cancelamento descrição do motivo e quem solicitou).

Nome do paciente, médico, especialidade, convênio, data e hora.

## Convênios
Lista de convênios que serão atendidos na clinica.

- Unimed
- Notre Dame
- Green Line
- Amil
- Bradesco
- Porto Seguro