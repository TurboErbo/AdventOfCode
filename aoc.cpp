#include <solution.hpp>

#include <fstream>
#include <iostream>
#include <filesystem>

namespace
{
    std::vector<std::string> readFileLines(std::filesystem::path path)
    {
        std::ifstream f(path);
        std::string buf;
        std::vector<std::string> result;
        while (std::getline(f, buf))
        {
            result.push_back(std::move(buf));
        }
        return result;
    }
}

int main(int argc, char *argv[])
{
    if (argc != 3)
    {
        std::cout << "Usage: aoc.cpp YEAR DAY\n";
        std::exit(1);
    }

    const std::string year = argv[1];
    const std::string day = argv[2];

    const auto part1_example_data(readFileLines(std::filesystem::path(year) / "data" / (day + ".example.txt")));
    const auto data(readFileLines(std::filesystem::path(year) / "data" / (day + ".txt")));

    std::vector<std::string> part2_example_data;
    const std::filesystem::path part2_example_path(std::filesystem::path(year) / "data" / (day + ".example2.txt"));
    if (std::filesystem::exists(part2_example_path))
    {
        part2_example_data = readFileLines(part2_example_path);
    }
    else
    {
        part2_example_data = std::move(part1_example_data);
    }

    const auto solutions = readFileLines(std::filesystem::path(year) / "data" / (day + ".solution.txt"));

    Solution s;
    const auto part1_example_result = s.part1(part1_example_data);
    if (part1_example_result != solutions[0])
    {
        std::cout << "Part 1 example failed, expected: " << solutions[0] << ", got: " << part1_example_result << std::endl;
        std::exit(1);
    }
    std::cout << "Part 1 example passed!" << std::endl;

    const auto part1_result = s.part1(data);
    std::cout << "Part 1 result: " << part1_result << std::endl;

    if (solutions.size() == 1)
    {
        std::cout << "Part 2 example solution not provided. Exiting." << std::endl;
        std::exit(0);
    }

    const auto part2_example_result = s.part2(part2_example_data);
    if (part2_example_result != solutions[1])
    {
        std::cout << "Part 2 example failed, expected: " << solutions[1] << ", got: " << part2_example_result << std::endl;
        std::exit(1);
    }
    std::cout << "Part 2 example passed!" << std::endl;

    const auto part2_result = s.part2(data);
    std::cout << "Part 2 result: " << part2_result << std::endl;
}