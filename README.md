# Code Wars II | Projeto: Holerite :receipt:	

Bootcamp Python /código[s]<br>
Stone e How Bootcamps :green_heart: :purple_heart:	
<br>

#

### Nome do Projeto: "Sistema de folha de pagamento da XPTO Alimentos" 

<b>:rocket:	Grupo 9:</b>
<ul>
  <li><a href="https://github.com/barbaramir" target="_blank">Bárbara Mirelli de Oliveira Pinto</a></li>
  <li><a href="https://github.com/LorianeMartins" target="_blank">Loriane Moreira Martins</a></li>
  <li><a href="https://github.com/pedrohbb" target="_blank">Pedro Henrique Birindiba Batista</a></li>
  <li><a href="https://github.com/renatalobo" target="_blank">Renata Lobo Alves</a></li>
  <li><a href="https://github.com/thaifurforo" target="_blank">Thainara Lessa Furforo</a></li>
</ul>

## :bookmark_tabs:	Etapas

<b>:heavy_check_mark:	Cumpridas:</b>
<ul>
   <li>Diagrama do banco de dados</li>
   <li>Script para geração do banco de dados</li>
   <ul>
     <li>Bancos: funcionários, cargos e holerites</li>
     <li>Inserção automática: cargos base</li>
     <li>Inserção automática: funcionários exemplo</li>
    </ul>
    <li>Funções:</li>
    <ul>
      <li>Inclusão de funcionários</li>
      <li>Exclusão de funcionários</li>
      <li>Consulta de dados de funcionários</li>
      <li>Alteração de dados de funcionários</li>
      <li>Listagem de todos os funcionários registrados</li>
      <li>Geração de holerite de funcionário específico</li>
      <li>Geração de holerite de todos os funcionários em um mês específico</li>
      *Obs.: os holerites gerados são salvos automaticamente no banco de dados, exceto caso já tenha sido salvo anteriormente um holerite para a mesma matrícula e mesmo mês
     </ul>
     <li>Tratamento de exceções:</li>
     <ul>
       <li>Não permitir a inclusão de dois funcionários com o mesmo CPF</li>
       <li>Não permitir a inclusão de dados brancos ou nulos (validação de cada campo dentro de critérios específicos) na inserção e na alteração de dados de funcionários</li>
       <li>Emitir mensagem de erro caso a chave buscada (matrícula ou CPF) não seja encontrada, nas funções exclusão, consulta e alteração</li>
       <li>Emitir mensagem de erro na função de listagem, caso não haja funcionários cadastrados</li>
     <li>Extras:</li>
     <ul>
       <li>Geração automática de número de matrícula de 6 dígitos na inclusão de funcionários, por auto incremento no banco de dados, iniciando em 100001 e mantendo o padrão de sequência</li>
       <li>Modelo de holerite gráfico é gerado nas funções de holerite</li>
       <li>Arquivo connection com as configurações de conexão, para evitar repetição em todos os módulos</li>
       <li>Arquivo .env oculto no repositório, no qual cada utilizador deverá registrar suas variáveis de acesso ao MySQL, garantindo maior segurança</a>
      </ul>
</ul>
</ul>
<b>:x: Pendentes:</b>
<ul>
   <li>Do enunciado:</li>
   <ul>
     <li>Testes unitários</li>
   </ul>
   <li>Extras:</li>
   <ul>
     <li>Revisão do diagrama UML de classes</li>
     <li>Retirar o hardcoding do script nas consultas ao banco de dados</li>
     <li>Criar banco de dados de funcionários inativos para arquivamento dos funcionários cujos contratos tenham sido rescindidos, incluindo "data rescisão"</li>
     <li>Adicionar função: alterar dados do holerite (caso tenham sido inseridos dados errados na geração inicial do holerite)</li>
     <li>Fazer tratamento de exceções para que só possa ser emitido holerite de um mês que esteja entre a admissão e a rescisão do funcionário (caso inativo) ou entre a admissão e a data atual (caso inativo)</li>
   </ul>
</ul>
