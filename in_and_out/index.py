#!/usr/bin/python3.7

import MySQLdb
import cgi


print ("Content-Type: text/htmlr\n\r\n\r;charset=utf-8")
print ("<html><head>")
print ("<title>Pruebas</title>")
print()
print ("""<script type="text/javascript" src="https://www.google.com/jsapi?autoload={'modules':[{'name':'visualization', 'version':'1', 'packages':['corechart']}]}></script>""")
#Inicia el script que dibujará la gráfica
print ("<script type=text/javascript>")
print ("google.setOnLoadCallback(drawChart);")
#Hace las consultas en la base de datos.
db = MySQLdb.connect("localhost","root","password","RB")
curs = db.cursor()
curs.execute("SELECT * FROM RB order By date DESC limit 0,100")
print ("function drawChart() {var data = google.visualization.arrayToDataTable([['Fecha', 'Voltaje', 'Potencia'])
#Hace la consulta en la base de datos y por ende, extrae todos los datos en tiempo real
for data in curs.fetchall():
    print (",['"+str(data[1])+"',"+str(data[2])+","+str(data[3])+"]")
print ("]);")
db.close() 
print("""   var options = {
                title: 'Raspberry',
                curveType: 'function',
                legend: { position: 'bottom' }
            };""")
print ("""  var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));
            chart.draw(data, options);
        }</script>""")
print ("""</head>
<body>
<h1>Mediciones en tiempo real</h1>
<div id="curve_chart"></div>
</body></html>""")