
function help(){
    echo "debe incluir tres parametros posicion inicial, velocidad inicial y tiempo total "
}


if ! [ $# -eq 3]; then 
    echo $"Son tres"
    help
    exit l
fi
    echo $"corriendo programa"

