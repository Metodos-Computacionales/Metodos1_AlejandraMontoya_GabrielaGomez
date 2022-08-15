
function help(){
    echo $"debe incluir tres parametros posicion inicial, velocidad inicial y tiempo total "
}
if ! [ $# -eq 3 ]; then
	echo ""
	help
	exit 1
else
	echo "Corriendo programa"
fi
