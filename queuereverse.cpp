#include<bits/stdc++.h>
using namespace std;
void print(queue<int> &q)
{
	while(!q.empty())
	{
		int r= q.front();
		cout<<  r;
    }
}

int reverse(queue<int>&q)
{

   stack<int> Stack;
   while(!q.empty())
   {

   	Stack.push(q.front());

   }

  while(!Stack.empty())
  {

   q.push(Stack.top());
   Stack.pop();

   }
   return q;
   

}




int main()
{
	queue<int> q1;
	q1.push(1);
	q1.push(2);
	q1.push(3);
	q1.push(4);
	q1.push(5);
	q1.push(6);
     cout<<"the initial queue that you have provided is"<<endl;
     print(q1);
     reverse(q1);
     cout<<"the reversed queue is"<<endl;
     print(q1);
     
  
}