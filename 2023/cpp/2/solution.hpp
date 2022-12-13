#include <string>
#include <vector>

class Solution
{
public:
    std::string part1(const std::vector<std::string> &lines)
    {
        for (int i = 0; i < lines.size(); i++)
        {
            const std::string &line = lines[i];
            int id = i + 1;
            auto colon = line.find(':');
            std::string_view draws_str(&line[colon + 1], line.size() - colon - 1);
            std::size_t semicolon, start{0};
            std::vector<std::string_view> draws;
            while ((semicolon = draws_str.find(';', start)) != std::string_view::npos)
            {
                draws.emplace_back(&draws_str[start], semicolon - 1);
                start = semicolon + 1;
            }
            draws.emplace_back(&draws_str[start], draws_str.end());
        }
        return "";
    }

    std::string part2(const std::vector<std::string> &lines)
    {
    }
};