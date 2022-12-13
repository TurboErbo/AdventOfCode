#include "utilities.hpp"

#include <string>
#include <vector>
#include <numeric>

class Solution
{
public:
    std::string part1(const std::vector<std::string> &lines)
    {
        auto [numbers, symbols] = Utilities::parse_input(lines);
        auto part_numbers = Utilities::extract_part_numbers(numbers, symbols);
        return std::to_string(std::reduce(part_numbers.begin(), part_numbers.end()));
    }

    std::string part2(const std::vector<std::string> &lines)
    {
        return "";
    }
};