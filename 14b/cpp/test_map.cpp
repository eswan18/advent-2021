#include <iostream>
#include <map>
#include <string>
#include <string_view>


void print_map(std::string_view comment, const std::map<std::string, char>& m)
{
    std::cout << comment;
    for (const auto& [key, value] : m) {
        std::cout << key << " = " << value << "; ";
    }
    std::cout << "\n";
}

int main() {
    std::map<std::string, char> test_rules = {
        {"CH", "B"},
        {"HH", "N"},
        {"CB", "H"},
        {"NH", "C"},
        {"HB", "C"},
        {"HC", "B"},
        {"HN", "C"},
        {"NN", "C"},
        {"BH", "H"},
        {"NC", "B"},
        {"NB", "B"},
        {"BN", "B"},
        {"BB", "N"},
        {"BC", "B"},
        {"CC", "N"},
        {"CN", "C"},
    };

    print_map("map: ", test_rules);
}
