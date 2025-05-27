#include <vector>

class Flag {
    std::vector<char> *flag;
public:
    Flag() {
        flag = new std::vector<char>({102,108,97,103,123,81,85,69,83,84,65,95,70,76,65,71,95,69,39,95,83,73,67,85,82,65,77,69,78,84,69,95,85,78,65,95,70,76,65,71,95,86,69,82,65,125});
    }
};

// da mandare da qua
#include <unistd.h>
int main(){
    Flag flag;
    std::vector<char> *prova = *(std::vector<char> **)&flag;
    for(char &i: *prova){
        write(1, &i, 1);
    }
    return 0;
}
// EOF
