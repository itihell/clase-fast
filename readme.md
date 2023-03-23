Renombrar el archivo .env.example a .env y configurar los valores que este trae de ejemplo por los del servidor de configuración

### Creando el entorno de python
````
python3 -m virtualenv venv

ó

python -m virtualenv venv
````



### Instalando dependencias
```
pip install -r  requirement.txt
```

### Activando el entorno
```
source venv/bin/activate
```

### Ejecuntando el servidor
```
uvicorn main:app --reload
```

##### Si no esta instaldo pip en ubuntu
```
sudo apt install python3-pip
```

##### Si no esta instalado virtualenv
```
pip install virtualenv
```




