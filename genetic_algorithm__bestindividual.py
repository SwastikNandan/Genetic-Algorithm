import numpy as ny
import random
import math
from matplotlib import pyplot as plt
from random import randint

def fitness(gs):
    s=gs[0]
    a=gs[1]
    b=gs[2]
    c=gs[3]
    d=gs[4]
    if s==['+']:
        x = float(a) + float(b/10) + float(c/100) + float(d/1000)
    else:
        x = (-1)*( float(a) + float(b/10) + float(c/100) + float(d/1000) )
    f=float(x*(math.sin( 10*3.14*x))+1)
    return f
    
def generator():            # generates string of base 10 random numbers
    sign_list=['+','-']
    sign=random.sample(sign_list,1)
    a=randint(0,9)
    b=randint(0,9)
    c=randint(0,9)
    d=randint(0,9)
    gs=[sign,a,b,c,d]            # gs stands for gene-string
    #print(gs)
    return gs

def batch_generator(ps):
    string_elements=[None]*ps
    elem=0
    while(elem != ps ):
        g=generator()
        if g[0]==['+']:
            number= float(g[1]) + float(g[2]/10) + float(g[3]/100) + float(g[4]/1000)
        else :
            number= (-1)*(float(g[1]) + float(g[2]/10) + float(g[3]/100) + float(g[4]/1000))
        if (number<= 1 and number >= -.5) :
            string_elements[elem]=g        # string_elements is a list of list
            elem=elem+1                         # elem a variable that keeps track of the number of elements that goes in the string_elements list
    return string_elements
        


def selection(sz,p) :
    ordered_tuple = ()
    ordered_tuple_list=[None]*sz
    content=()
    for i in range(sz):
        fitness_index=fitness(p[i])
        ordered_tuple = (fitness_index,p[i])
        ordered_tuple_list[i]=ordered_tuple
    ordered_tuple_list1=sorted(ordered_tuple_list,key = lambda x: x[0],reverse=True)
    sorted_strings = [None]*sz
    partition_string_tuple=()
    cumulative_partition=0
    total= ((sz)*(sz))-((sz-1)*(sz-2)/2)
    partition_tuple_list= [None]*sz
    for count in range(sz):
        content=ordered_tuple_list1[count]
        sorted_strings[count]=content[1]
        partition= (sz - count)
        cumulative_partition = cumulative_partition + partition
        partition_string_tuple=(cumulative_partition,content[1])
        partition_tuple_list[count]=partition_string_tuple
    selected_string_list=[None]*350
    num1=0
    while num1<350:
        e=randint(0,total)
        for num2 in range(sz-1):
            tuple0 = partition_tuple_list[num2]
            if tuple0[1]==None:
                print(tuple0[1],'--------------------------------------------------------------------')
            tuple1 = partition_tuple_list[num2+1]
            if tuple1[1]==None:
                print(tuple1[1],'--------------------------------------------------------------------')
            if e<tuple1[0] and e>tuple0[0]:
                selected_string_list[num1]= tuple0[1]
                print(tuple0[1])
                num1 = num1 +1 
    print('I am in selection')
    print(selected_string_list)
    return selected_string_list
    
def mutation(child_elements):
    num1=0
    while(num1!=1650):
        elem=child_elements[num1]
        for num2 in range(1,4):
            a=elem[num2]
            pm=.5                   #mutation probability
            k=random.uniform(0,1)
            if k<pm:
                d= int((1650-num1)/1650)
                random_number= randint(a-d,a+d)
                if random_number>=10 and random_number<12:
                    random_number=1
                elif random_number>=12 and random_number<14:
                    random_number=3
                elif random_number>=14 and random_number<16:
                    random_number=5
                elif random_number>=16 and random_number<18:
                    random_number=7
                elif random_number>=18 and random_number<20:
                    random_number=9
                elem[num2]=random_number
        g=elem
        if g[0]==['+']:
            number= float(g[1]) + float(g[2]/10) + float(g[3]/100) + float(g[4]/1000)
        else :
            number= (-1)*(float(g[1]) + float(g[2]/10) + float(g[3]/100) + float(g[4]/1000))
        if number>-.5 and number<1:
            child_elements[num1]=g
            num1=num1+1
    return child_elements
                #perform mutation

def crossover(selected_string,ps):
    print('I am here')
    elem=0
    child_elements=[None]*1650
    while(elem != 1650 ):
        random_index= random.sample(range(0, 350), 2)             # randomly generated indices
        parent1 = selected_string[random_index[0]]    # parent1 is a string of genes
        parent2 = selected_string[random_index[1]]    # parent2 is a string of genes
        child=[parent1[0],parent2[1],parent1[2],parent2[3],parent1[4]]
        if child[0]==['+']:
            number= float(child[1]) + float(child[2])/10 + float(child[3])/100 + float(child[4])/1000
        else:
            number= (-1)*(float(child[1]) + float(child[2])/10 + float(child[3])/100 + float(child[4])/1000)
        if (number <= 1 and number >= -.5):
            child_elements[elem]=child        # child_elements is a list of list
            elem=elem+1
    return child_elements

    
# The body of the main program
population_size=2000
gene_population=batch_generator(population_size)     # gene_population is a list of list
diff=1                                               # initializing diff
max_list=[None]*30
min_list=[None]*30
average=[None]*30
cnt=0
while (cnt<30):
    selected_strings= selection(population_size,gene_population)
    children1=crossover(selected_strings,population_size)
    children=mutation(children1)
    gene_population=selected_strings+children
    tally1=[None]*2000
    tally2=[None]*2000
    tally_tuple=[None]*2000
    avg=0
    for i in range(2000):
        e1=gene_population[i]
        eval_1=fitness(e1)
        if e1[0]==['+']:
            number1= float(e1[1]) + float(e1[2]/10) + float(e1[3]/100) + float(e1[4]/1000)
        else:
            number1=(-1)*(float(e1[1]) + float(e1[2]/10) + float(e1[3]/100) + float(e1[4]/1000))
        tally1[i]=eval_1
        tally2[i]=number1
        tup=(eval_1,number1)
        tally_tuple[i]=tup
    ordered_tuple=sorted(tally_tuple,key = lambda x: x[0],reverse=True)
        #avg=avg+eval_1
    min_list[cnt]=ordered_tuple[1999][1]
    max_list[cnt]=ordered_tuple[0][1]
    #average[cnt]= avg/population_size
    cnt=cnt+1
iteration_list=range(0,30)
#print(max_list)
#print(min_list)
#print(average)
plt.plot(iteration_list, max_list,'r',label='Best individual for each successive generation of the GA')
plt.plot(iteration_list, min_list, 'b', label='Worst individual for each successive generation of the GA')
#plt.plot(iteration_list, average, 'g', label='Average')
plt.xlabel('Iteration')
plt.ylabel('X Values')
plt.legend(loc='best')
plt.show()
#tally1=[None]*2000
#tally2=[None]*2000
#for i in range(2000):
#    e1=gene_population[i]
    #e2=gene_population[1000]
#    eval_1=fitness(e1)
    #eval_2=fitness(e2)
#    if e1[0]==['+']:
#        number1= float(e1[1]) + float(e1[2]/10) + float(e1[3]/100) + float(e1[4]/1000)
#    else:
#        number1=(-1)*(float(e1[1]) + float(e1[2]/10) + float(e1[3]/100) + float(e1[4]/1000))
    #if e2[0]==['+']:
    #    number2=float(e2[1]) + float(e2[2]/10) + float(e2[3]/100) + float(e2[4]/1000)
    #else:
    #    number2=(-1)*(float(e2[1]) + float(e2[2]/10) + float(e2[3]/100) + float(e2[4]/1000))
    #diff=abs(number1-number2)
#    tally1[i]=eval_1
#    tally2[i]=number1
    
    #result=(number1+number2)/2
    #print(number1)
    #print(number2)
#maximum1=max(tally1)
#minimum1=min(tally1)
#maximum2=max(tally2)
#minimum2=min(tally2)
#print('The minimum y value is:',minimum1)
#print('The maximum y value is:',maximum1)
#print('The minimum x value is',minimum2)
#print('The maximum x value is', maximum2)
    #diff=(eval_1-eval_2)/(number1-number2)             # Rolle's theorem to evaluate the derivative
    #print(diff)

#print(gene_population[10])
    #    number1= float(e1[1]) + float(e1[2]/10) + float(e1[3]/100) + float(e1[4]/1000)
    #else:
    #    number1=(-1)*(float(e1[1]) + float(e1[2]/10) + float(e1[3]/100) + float(e1[4]/1000))






