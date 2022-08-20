echo "Escriba un numero"
read num 
fact=1
while [ $num -gt 1 ]
do
  fact=$((fact * num))  
  num=$((num - 1))     
done
echo fact
#Calcular primeros 20 factoriales

echo "Los primeros 20 numeros factoriales son:"
for i in {1..19}
    do
    num_2=$i
    fact_2=1
    while [ $num_2 -gt 1 ]
    do
    fact_2=$((fact_2 * num_2))  
    num_2=$((num_2 - 1))     
    done
    echo $fact_2
    done