res=0
aux=5
#funcion

function factorial(){
    local number=4
    for i in {1..3}
    do
        let number=$(($number*$i))
    done
    echo $number 
}

factorial
