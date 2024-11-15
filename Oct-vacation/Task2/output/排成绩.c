#include <stdio.h>
#include <stdlib.h>

void print(int a[], int n, int i) {
    printf("���Ϊ�� ", i + 1);
    for (int j = 0; j < n; j++) {
        printf("%d  ", a[j]);
    }
    printf("\n");
}

void selectSort(int a[],int len) {
        int i,j,min,max,tmp;  
        for(i=0; i<len/2; i++){  // ��������n/2��ѡ������ 
            min = max = i;  
            for(j=i+1; j<=len-1-i; j++){  
				//�ֱ��¼������С�ؼ��ּ�¼λ��
                if(a[j] > a[max]){  
                    max = j;  
                    continue;  
                }  
                if(a[j] < a[min]){  
                    min = j;  
                }  
            }  
			//�ý����������ɷ�������������Ч��
            if(min != i){//����һ��Ϊminֵ�����ý���  
                tmp=a[min];  a[min]=a[i];  a[i]=tmp;  
            }  
            if(max == len-1-i && min == i)//����һ��Ϊmaxֵ��ͬʱ���һ��Ϊminֵ��������Ҫ�������  
                continue;  
            if(max == i)//����һ��Ϊmaxֵ���򽻻���min��λ��Ϊmaxֵ  
                max = min;  
            if(max != len-1-i){//�����һ��Ϊmaxֵ�����ý���  
                tmp=a[max];  a[max]=a[len-1-i];  a[len-1-i]=tmp;  
            }		
        }  
 }

int main() 
{
    int size;
    printf("�༶����Ϊ?\n");
    scanf("%d",&size);
    int *grade = (int *)malloc(size * sizeof(int)); // ��̬�����ڴ����

    if (grade == NULL) {
        printf("Memory allocation failed.\n");
        return 1;
    }

    for (int i = 0; i < size; i++) {
        printf("��%dλͬѧ�ķ�����?\n",i+1);
        scanf("%d", &grade[i]);
    }

    printf("��ȷ�����ݣ�");
    for (int i = 0; i < size; i++) {
        printf("%d ", grade[i]);
    }
    printf("\n\n");
    selectSort(grade, size);
    print(grade, size, size);
    return 0;
}