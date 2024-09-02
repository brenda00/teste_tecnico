# 🚀 Desafios Técnicos

Este repositório contém três desafios que cobrem Arquitetura, Consumo de Dados e Disponibilização de Dados. Vamos nessa?

## 🏗️ Desafio 1: Arquitetura

Os dispositivos com o **Globoplay** instalado (mobile, TV, computadores, etc.) enviarão eventos a cada ação do usuário na plataforma (assistir a um vídeo, pausar, adicionar aos favoritos, etc.). Seu desafio é pensar em uma solução escalável que suporte um grande volume de requisições por segundo. A solução deve receber e armazenar esses eventos para posterior análise pelas áreas de negócios.

### Requisitos
1. A arquitetura deve suportar ingestão de dados em tempo real e em lote.
2. Armazenamento centralizado que permita consultas rápidas e eficientes.
3. Uso de tecnologias adequadas para armazenamento e processamento de dados.
4. Explicação de como os dados serão consumidos e analisados.
5. Implementação de práticas de Governança de Dados para proteção de dados sensíveis (PII), garantindo que apenas pessoas autorizadas tenham acesso.

### Entregáveis
- 🖼️ Desenho da arquitetura em formato PDF ou imagem.
- 📄 Documento explicativo (máximo de 2 páginas) detalhando os componentes escolhidos e o fluxo de dados.

## 💾 Desafio 2: Consumo de Dados

Implemente um pipeline de dados simples que colete informações da API [SWAPI](https://swapi.dev/) e armazene esses dados em um banco de dados.

### Requisitos
- O desafio pode ser concluído na linguagem de programação de sua escolha.
- Utilize a biblioteca padrão da linguagem escolhida para coletar os dados.
- Lembre-se de que seu código será executado em um ambiente que você não controla, então, pense em implementações que facilitem essa execução.
- Testes unitários serão um diferencial!

### Entregáveis
- 🔗 O código deve ser entregue em um repositório Git (GitHub ou GitLab).
- 📜 O repositório deve conter um arquivo README com as instruções para configuração e execução do pipeline.

## 🌐 Desafio 3: Disponibilização de Dados

Os dados coletados no pipeline anterior devem ser disponibilizados através de uma API HTTP(S).

### Requisitos
- A API deve conter os seguintes endpoints:
  1. **/hottest_planet**: Retorna os 3 planetas mais quentes do universo Star Wars.
  2. **/appears_most**: Retorna os 5 personagens que mais aparecem nos filmes de Star Wars.
  3. **/fastest_ships**: Retorna as 3 naves mais rápidas do universo Star Wars.
