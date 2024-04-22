#include <iostream>

class Singleton {
    protected:
        Singleton() {};
    public:
        static Singleton* Instancia();
    private:
        static Singleton* _instancia;

};

Singleton* Singleton::_instancia = 0;

Singleton* Singleton::Instancia(){
    if(_instancia==0){
        _instancia = new Singleton;
    }
    return _instancia;
}

int main(){

    auto *s1 = Singleton::Instancia();
    auto *s2 = Singleton::Instancia();

    if (s1 == s2) {
        std::cout << "Son iguales instancias " << std::endl;
    } else {
        std::cout << "Son distintas " << std::endl;
    }

    return 0;
}
