#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

int main ()
{
  int t, n, q, l, r, count = 0;
  cin >> t;	
  for (int i = 1; i <= t; ++i)
  {      
    cin >> n >> q;
    char vect[n+1];
    cin >> vect;

    count = 0;
    for (int j = 0; j < q; j++)
    {
     cin >> l >> r;

     unordered_map<char,int> mymap;

     for(int k=l-1; k<r; k++){
      if(mymap.find (vect[k])== mymap.end() ){
        mymap[vect[k]] = 1;
      } else{
       mymap[vect[k]] += 1;
     }
   }

   int flag1=0;

   for (pair<char,int> element : mymap)
   {
    if(element.second%2 == 1){
      flag1++;
    }
  }
  if(flag1<2) count++;
}
cout << "Case #" << i << ": " << count << endl;
}
return 0;
}