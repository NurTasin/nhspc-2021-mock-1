#include <iostream>
#include <string>

#define minimum(x,y) ((x<y)?x:y)
int main(){
    int n;
    std::cin>>n;
    std::string blob;
    std::cin>>blob;
    int c=0,o=0,d=0,e=0;
    for(int i=0;i<blob.size();i++){
        if(blob[i]=='c'){
            c++;
        }
        else if(blob[i]=='o'){
            o++;
        }
        else if(blob[i]=='d'){
            d++;
        }
        else if(blob[i]=='e'){
            e++;
        }
    }
    int ans=minimum(minimum(c,o),minimum(d,e));
    std::cout << ans << std::endl;
    return 0;
}