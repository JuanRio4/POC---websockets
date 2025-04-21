A prova de conceito tem como objetivo demonstrar a viabilidade da implementação de um sistema simples de comunicação bidirecional em tempo real utilizando WebSockets, um protocolo que permite a comunicação persistente entre cliente e servidor. O foco da POC é explorar a troca de mensagens em tempo real em um ambiente controlado, onde o cliente e o servidor podem interagir de maneira eficiente e fluida.

A comunicação bidirecional possibilita que o servidor envie respostas para o cliente sempre que uma nova mensagem for recebida, proporcionando uma experiência de chat em tempo real. A escolha do WebSocket para a implementação se dá pela sua eficiência em ambientes de comunicação contínua, como em aplicações de chat, jogos online e sistemas de monitoramento.

5.1 Objetivos

●	Simular um ambiente distribuído com múltiplos sensores transmitindo dados em tempo real.

●	Avaliar o desempenho e a escalabilidade do protocolo MQTT como solução de comunicação para sistemas distribuídos.

●	Estabelecer uma arquitetura leve e eficiente baseada em pub/sub.

●	Monitorar e visualizar dados em tempo real, integrando ferramentas modernas de telemetria.

5.2 Implementação

Produtores (Sensores Simulados)

●	Três scripts Python simulam sensores de temperatura, umidade e pressão atmosférica.

●	Cada sensor publica dados em tópicos distintos no broker MQTT (ex.: iot/temperatura).

Broker MQTT (Mosquitto)

●	Instanciado em container Docker, configurado para aceitar múltiplas conexões simultâneas.

●	Controla o roteamento de mensagens de forma leve e eficiente.

Consumidores (Clientes MQTT)

●	Painel de monitoramento (via Grafana) conectado ao InfluxDB consome os dados.

●	Um consumidor alternativo (script Python) também registra os dados localmente e pode acionar alertas.

