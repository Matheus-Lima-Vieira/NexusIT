PROJETO 12 — NEXUS IT

Objetivo:
Criar um sistema interno de gerenciamento de chamados de TI, simulando um ambiente profissional de atendimento e suporte.

STACK:

Frontend: Angular + TypeScript + HTML/CSS + RxJS
Backend: Python + FastAPI
Banco: PostgreSQL + SQLAlchemy
Git/GitHub
API REST + Swagger/OpenAPI
Testes e deploy

PERFIS:

Solicitante: abre, consulta e comenta chamados.
Técnico: visualiza chamados do seu grupo, assume chamados, altera status/prioridade, comenta, adiciona anotações técnicas, resolve e cancela.
Administrador: possui as funcionalidades do técnico + gerenciamento de usuários, perfis, grupos e regras/configurações da ferramenta.

CHAMADO:

ID
Título
Descrição
Tipo/problema
Prioridade
Data de abertura
Última atualização
Status
Sala/local do solicitante
Solicitante
Técnico atribuído
Grupo resolutor

USUÁRIO:

Nome/dados básicos
Perfil (solicitante, técnico ou administrador)
Grupo(s) do técnico
VIP (sim/não)

STATUS:

Novo
Em atendimento
Pendente
Planejado
Resolvido
Cancelado

REGRAS DE NEGÓCIO:

VIP pertence ao usuário e serve apenas como indicação visual para o técnico.
O solicitante não define livremente a prioridade.
A prioridade inicial é determinada automaticamente pelo tipo/problema selecionado.
O técnico pode alterar a prioridade.
A prioridade inicial utiliza P1 (muito alta), P2 (alta), P3 (média) e P4 (baixa).
Solicitante não pode cancelar chamados.
Técnicos só podem atender chamados pertencentes ao seu grupo resolutor.
Um chamado possui apenas um técnico atribuído por vez.
Qualquer técnico do grupo pode assumir um chamado.
Para cancelar, o chamado deve estar atribuído ao técnico que realizará o cancelamento.
Cancelamento exige justificativa obrigatória.
Chamado cancelado continua listado para consulta e histórico.
Chamado cancelado não pode ser reaberto. Caso necessário, deve ser criado um novo chamado.
Chamado resolvido é considerado encerrado.
Um chamado resolvido pode ser reaberto por solicitante ou técnico, voltando para o status Novo.
Transições permitidas:
Novo → Em atendimento
Em atendimento → Pendente
Em atendimento → Planejado
Em atendimento → Resolvido
Pendente → Resolvido
Planejado → Em atendimento
Planejado → Resolvido
Não são permitidas transições como Novo → Resolvido, Cancelado → Em atendimento ou Resolvido → Pendente.
Para alterar o chamado para Resolvido, deve existir pelo menos um comentário.
Depois de Resolvido, solicitante não pode adicionar comentários.
Técnico e administrador podem adicionar comentários mesmo após Resolvido.
Comentários são visíveis para solicitante, técnicos e administrador.
Anotações técnicas são visíveis somente para técnicos e administrador.
Comentários e anotações podem ser editados, mas não excluídos fisicamente.
Edições devem gerar registro no histórico.
Alterações importantes do chamado devem gerar histórico.
O histórico registra usuário, data/hora, ação e, quando aplicável, valor anterior e novo valor.

HISTÓRICO:

Registrar pelo menos:

Chamado criado
Status alterado
Técnico atribuído/alterado
Prioridade alterada
Comentário adicionado/editado
Anotação adicionada/editada
Chamado cancelado
Chamado resolvido
Reabertura do chamado

COMENTÁRIOS:

Comentários são destinados à comunicação entre solicitante e equipe técnica.
Anotações técnicas são internas da equipe.
Registros não são apagados fisicamente para preservar o histórico.

TIPOS DE PROBLEMA / PRIORIDADE INICIAL:

Computador:

Não liga → P1
Travamento → P2
Lentidão → P3
Erro → P3
Outro → P4 + descrição

Usuário:

Criar usuário para novo funcionário → P4
Desativar usuário de funcionário demitido → P4

Sistema:

Erro → P3
Instalação → P3
Desinstalação → P4
Dúvida → P4
Não acessa → P3

Acesso:

Reset de senha → P3

Rede:

Sem internet → P2
Internet lenta → P4
Site específico não acessa → P3

TELAS:

Solicitante:

Login
Meus chamados
Abrir chamado
Detalhes do chamado
Comentários

Técnico:

Login
Lista de chamados do seu grupo
Filtros e busca
Detalhes do chamado
Assumir chamado
Alterar status/prioridade
Comentários
Anotações técnicas
Resolver/cancelar

Administrador:

Tudo do técnico
Gerenciamento de usuários
Perfis
Grupos resolutores
Técnicos × grupos
Regras/configurações da ferramenta

FILTROS:

Permitir filtros e combinações por:

Número do chamado
Status
Data de abertura
Solicitante
Técnico
Grupo resolutor
Chamados abertos/fechados
Chamados de determinado usuário
Chamados atribuídos/finalizados por determinado técnico

ESCOPO DO MVP:

Criar primeiro uma versão funcional e profissional do Nexus IT.

Ficam fora da primeira versão:

Fluxos complexos de aprovação
Integração real com Active Directory
Scripts/automação avançada
Outras áreas além de TI

LOGIN:

Sistema interno, sem cadastro público.
No desenvolvimento, utilizar usuários previamente cadastrados no banco para simular o ambiente corporativo/AD.
Cada usuário terá seu perfil e permissões correspondentes.

USO DE IA:

IA pode ser usada para boilerplate, código repetitivo, documentação, testes, CSS, configurações e resolução de bugs.
Nas partes importantes de arquitetura e regras de negócio, tentar primeiro e usar IA como orientação/revisão.
Nenhum código deve ser mantido sem entender o que ele faz.
O objetivo é conseguir explicar as decisões e o funcionamento do sistema em uma entrevista.