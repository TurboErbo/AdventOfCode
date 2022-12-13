#include "utilities.hpp"

#include <string>
#include <vector>

class Solution
{
public:
    std::string part1(const std::vector<std::string> &lines)
    {
        int sum{0};
        for (const auto &line : lines)
        {
            sum += Utility::parse_line(line);
        }

        return std::to_string(sum);
    }

    std::string part2(const std::vector<std::string> &lines)
    {
        const std::vector<std::string> digit_strings{"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        int sum{0};
        for (const auto &line : lines)
        {
            int firstdigit, lastdigit;
            std::size_t firstdigitindex{std::numeric_limits<std::size_t>::max()}, lastdigitindex{0};
            for (int i = 1; i <= 9; i++)
            {
                auto idx = line.find(digit_strings[i - 1]);
                if (idx != std::string::npos && idx < firstdigitindex)
                {
                    firstdigitindex = idx;
                    firstdigit = i;
                }
                idx = line.find('0' + i);
                if (idx != std::string::npos && idx < firstdigitindex)
                {
                    firstdigitindex = idx;
                    firstdigit = i;
                }
                idx = line.rfind(digit_strings[i - 1]);
                if (idx != std::string::npos && idx >= lastdigitindex)
                {
                    lastdigitindex = idx;
                    lastdigit = i;
                }
                idx = line.rfind('0' + i);
                if (idx != std::string::npos && idx >= lastdigitindex)
                {
                    lastdigitindex = idx;
                    lastdigit = i;
                }
            }
            sum += firstdigit * 10 + lastdigit;
        }
        return std::to_string(sum);
    }
};