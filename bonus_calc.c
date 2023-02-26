#include<stdio.h>
int main()
{
    char gender;
    printf("\nEnter the employee gender(m/f): ");
    scanf("%c",&gender);
    float salary,bonus,final_salary;
    printf("\nEnter your current salary:");
    scanf("%f",&salary);
    if(gender=='m')
    {
       if(salary<10000)
        {
            bonus=0.12*salary;
        }
        else
        {
            bonus=0.10*salary;
        }
    }
    else
    {
        if(salary<10000)
        {
            bonus=0.07*salary;
        }
        else
            {
                bonus=0.05*salary;
            }
    }
    final_salary=bonus+salary;
    printf("\nFinal salary of the employee is: %.2f rupees",final_salary);
    printf("\nBonus received:%.2f",bonus);
    return 0;
}
