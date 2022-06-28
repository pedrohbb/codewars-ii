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
  <li><a href="https://github.com/pedrohbb" target="_blank"></a>Pedro Henrique Birindiba Batista</li>
  <li><a href="https://github.com/renatalobo" target="_blank"></a>Renata Lobo Alves</li>
  <li><a href="https://github.com/thaifurforo" target="_blank">Thainara Lessa Furforo</a></li>
</ul>
<br>

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
      *Obs.: os holerites gerados são salvos automaticamente no banco de dados, exceto caso já tenha sido salvo anteriormente um holerite para a mesma matrícula e mesmo mês.
     </ul>
     <li>Tratamento de exceptions</li>
     <li>Extras:</li>
     <ul>
       <li>Modelo de holerite gráfico é gerado nas funções de holerite</li>
       <li>Arquivo connection com as configurações de conexão, para evitar repetição em todos os módulos</li>
       <li>Arquivo .env oculto no repositório, no qual cada utilizador deverá registrar suas variáveis de acesso ao MySQL, garantindo maior segurança</a>
      </ul>
</ul>
       
<b>:x:	Pendentes:</b>
<ul>
   <li>Do enunciado:</li>
   <ul>
     <li>Testes unitários</li>
   </ul>
   <li>Extras:</li>
   <ul>
     <li>Revisão do diagrama UML de classes</li>
     <li>Retirar o hardcoding do script</li>
     <li>Criar banco de dados de funcionários inativos para arquivamento dos funcionários cujos contratos tenham sido rescindidos, incluindo "data rescisão"</li>
     <li>Holerite: permitida a geração de holerite de funcionários inativos se o mês refência for entre a admissão e a rescisão</li>
     <li>Adicionar função: alterar dados do holerite (caso tenham sido inseridos dados errados na geração inicial do holerite)</li>
   </ul>
</ul>
