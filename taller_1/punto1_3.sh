
function checkvalue(){
    echo -n "Enter a number: "
    read VAR

    if [[ $VAR -gt 1 ]]
    then
    echo "Intente nuevamente"
    else
        echo "El numero fue correcto"
        pass=1
    fi
}

pass=0
while [ $pass -lt 1 ]
do
    checkvalue
done
