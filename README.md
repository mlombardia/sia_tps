# sia_tps

## TP1: 

### Instrucciones de instalación y ejecución

1. Descargar e instalar Python 3. 
2. Descargar e instalar pip para Python, ya que se requiere el uso de las librerias pygame y PyYAML.
3. Correr dentro de la carpeta del repositorio:
```
  pip install -r requirements.txt
```
4. Para correr el trabajo ejecutar:
```
  python main.py
```

### Manual de uso

1. Para correr un nivel, se debe elegir un mapa y un algoritmo. Para IDDFS y para los metodos informados tambien se debe aclarar un parametro extra (profundidad, heurística). Todos estos parámetros se pasan en el archivo config.yaml
2. Para manejar el visualizador:
```
→ : Pasa al siguiente estado
← : Vuelve al estado anterior
p : Activa o desactiva el autoplay, es decir el avance automático de estados
r : Reinicia el nivel al estado inicial
```
Tip: Recomendamos jugar los mapas con el autoplay activado, ya que contiene una animación especial al final.
