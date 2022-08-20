echo "Escriba el nombre de la carpeta que desea buscar"
read name
if [ -e "$name" ]; then
  echo "La carpeta si existe"
else
    echo "La carpeta no existe"
fi
