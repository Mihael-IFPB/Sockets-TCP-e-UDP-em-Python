# Projeto Cliente/Servidor com Sockets TCP e UDP

## Descrição do Projeto
Este projeto consiste na implementação de uma aplicação Cliente/Servidor utilizando os protocolos TCP e UDP em Python. Foi desenvolvido como parte da disciplina de **Tecnologias de Roteamento**, com o objetivo de explorar as diferenças entre esses dois protocolos de transporte e sua aplicação em uma rede de comunicação. 

A aplicação é composta por um servidor que responde a mensagens enviadas pelos clientes, utilizando as portas 5000 para TCP e 5001 para UDP. O cliente pode escolher o protocolo que deseja usar para enviar uma mensagem ao servidor e, em seguida, recebe uma resposta prefixada pelo identificador do protocolo ("TCP:" ou "UDP:").

## Objetivo
O principal objetivo deste projeto é compreender as diferenças práticas entre TCP e UDP, abordando questões como confiabilidade, conexão e estado, além de entender como cada protocolo é implementado em Python com o módulo `socket`.

## Estrutura do Projeto
O projeto contém os seguintes arquivos:

1. **servidor_tcp.py**: Código do servidor que escuta conexões TCP na porta 5000.
2. **servidor_udp.py**: Código do servidor que escuta mensagens UDP na porta 5001.
3. **servidor.py**: Versão avançada do servidor que lida com ambos os protocolos (TCP e UDP) simultaneamente em um único arquivo, utilizando threads para atender múltiplos clientes TCP.
4. **cliente.py**: Código do cliente, que permite ao usuário escolher o protocolo (TCP ou UDP), enviar uma mensagem ao servidor e exibir a resposta recebida.
5. **README.md**: Arquivo de documentação com instruções de uso e detalhes técnicos.

## Detalhes Técnicos
### Protocolos
- **TCP (Transmission Control Protocol)**: Protocolo orientado à conexão que garante entrega confiável e em ordem dos pacotes de dados. No projeto, cada cliente TCP que se conecta ao servidor é atendido em uma nova thread.
- **UDP (User Datagram Protocol)**: Protocolo sem conexão, que permite envio de mensagens (datagramas) sem garantir a entrega ou a ordem dos pacotes. O servidor UDP está sempre disponível para responder a múltiplas mensagens sem a necessidade de threads adicionais.

### Bibliotecas Utilizadas
- **socket**: Módulo padrão do Python para comunicação em rede, utilizado para criar sockets TCP e UDP.
- **threading**: Módulo para criar threads que possibilitam o atendimento simultâneo de múltiplos clientes TCP no servidor.

### Funcionamento Geral
1. O servidor escuta conexões TCP na porta 5000 e mensagens UDP na porta 5001.
2. O cliente permite ao usuário selecionar o protocolo desejado e enviar uma mensagem.
3. O servidor responde ao cliente com o prefixo do protocolo utilizado ("TCP:" ou "UDP:").
4. A comunicação entre cliente e servidor ocorre localmente (localhost), simulando uma rede de comunicação.

## Requisitos para Execução
- Python 3.x

## Como Executar o Projeto

### 1. Executando os Servidores Separadamente
Para executar os servidores TCP e UDP de forma independente:

1. Abra um terminal e execute o servidor TCP:
   ```bash
   python servidor_tcp.py
   ```
   O servidor TCP estará escutando na porta 5000.

2. Em outro terminal, execute o servidor UDP:
   ```bash
   python servidor_udp.py
   ```
   O servidor UDP estará escutando na porta 5001.

### 2. Executando o Servidor Unificado com Threads
Caso deseje executar um único servidor que escute e responda a ambos os protocolos (TCP e UDP) simultaneamente:

1. Execute o seguinte comando em um terminal:
   ```bash
   python servidor.py
   ```
   Este servidor estará escutando na porta 5000 para conexões TCP e na porta 5001 para mensagens UDP.

### 3. Executando o Cliente
Para enviar mensagens ao servidor, siga os passos abaixo:

1. Abra um novo terminal e execute o cliente:
   ```bash
   python cliente.py
   ```
   
2. O cliente solicitará que você escolha o protocolo e insira a mensagem a ser enviada:
   - Digite `TCP` ou `UDP` para selecionar o protocolo.
   - Em seguida, insira a mensagem que deseja enviar.

3. O cliente exibirá a resposta do servidor no seguinte formato:
   - Se enviado via TCP: `Resposta do servidor: TCP: [sua mensagem]`
   - Se enviado via UDP: `Resposta do servidor: UDP: [sua mensagem]`

### Exemplo de Funcionamento
**Exemplo 1 (TCP)**:
- Entrada do Cliente:
  - Protocolo: `TCP`
  - Mensagem: `Olá servidor!`
- Resposta Esperada: `Resposta do servidor: TCP: Olá servidor!`

**Exemplo 2 (UDP)**:
- Entrada do Cliente:
  - Protocolo: `UDP`
  - Mensagem: `Ping`
- Resposta Esperada: `Resposta do servidor: UDP: Ping`

## Considerações
- **Confiabilidade**: O TCP fornece entrega confiável e em ordem, enquanto o UDP não garante entrega nem ordem.
- **Performance**: O UDP é mais leve e rápido, pois não requer o estabelecimento de conexão.
- **Aplicações Práticas**: Este projeto demonstra uma aplicação básica que pode ser estendida para serviços que precisam de comunicação confiável (TCP) ou comunicação rápida e leve (UDP).

## Conclusão
Este projeto permite observar as diferenças fundamentais entre TCP e UDP no contexto de uma aplicação Cliente/Servidor. Além disso, a implementação de threads para atender a múltiplos clientes TCP simultâneos demonstra como lidar com paralelismo em Python. 

Para mais detalhes ou dúvidas, consulte a documentação do módulo `socket` em [https://docs.python.org/3/library/socket.html](https://docs.python.org/3/library/socket.html).
