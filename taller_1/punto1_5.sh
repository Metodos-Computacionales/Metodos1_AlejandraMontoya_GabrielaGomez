num=6
num_2=3
num_2=$((num-num_2))
fact=1
while [ $num -gt 1 ]
do
  fact=$((fact * num))  
  num=$((num - 1))     
done
fact_2=1
while [ $num_2 -gt 1 ]
do
  fact_2=$((fact_2 * num_2))   
  num_2=$((num_2 - 1))     
done

echo $(($fact/$fact_2))