#include<iostream>
#include<algorithm>
#include<cstdio>

using namespace std;

double step,*XY,*t,t_initial,t_final,XY_initial;

int main(){
	cin>>step>>t_initial>>t_final>>XY_initial;
	//cout<<step<<" "<<t_initial<<" "<<t_final<<" "<<XY_initial<<"\n\n";
	fflush(stdout);
	int N = (int)((t_final-t_initial)/step) + 1;
	XY = new double [N];
	t = new double [N];
	int i=0;
	XY[0]=XY_initial;
	t[0]=t_initial;
	float t_cur=t_initial;
	//cout<<"1"<<endl;
	while(t_cur < t_final){
		XY[i+1] = XY[i] + step*(XY[i] - XY[i]*XY[i]*XY[i]);
		//cout<<t_cur<<" "<<step<<"  ";
		t_cur = t_cur + step;
		//cout<<t_cur<<"      ";
		t[i+1]=t_cur;
		cout<<t[i]<<","<<XY[i]<<endl;
		i++;
		
	}
}