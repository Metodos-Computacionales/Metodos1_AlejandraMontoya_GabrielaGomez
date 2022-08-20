res=0
aux=5
#funcion

function factorial(){
    number=5
    for i in {1..4}
    do
        let number=$(($number*$i))
    done
    echo $number 
}

factorial
