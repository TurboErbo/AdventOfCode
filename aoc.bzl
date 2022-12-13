def aoc(year, day):
    native.cc_binary(
        name = "{}_{}".format(year, day),
        srcs = ["aoc.cpp"],
        deps = ["{}_{}_solution".format(year, day)],
        args = [str(year), str(day)],
        data = native.glob(["{}/data/{}*.txt".format(year, day)]),
    )

    native.cc_library(
        name = "{}_{}_solution".format(year, day),
        hdrs = ["{}/cpp/{}/solution.hpp".format(year, day)],
        deps = [":{}_{}_utilities".format(year, day)],
        strip_include_prefix = "{}/cpp/{}".format(year, day),
    )

    native.cc_library(
        name = "{}_{}_utilities".format(year, day),
        hdrs = ["{}/cpp/{}/utilities.hpp".format(year, day)],
        strip_include_prefix = "{}/cpp/{}".format(year, day),
    )

    native.cc_test(
        name = "{}_{}_test".format(year, day),
        srcs = ["{}/cpp/{}/test.cpp".format(year, day)],
        deps = [
            ":{}_{}_utilities".format(year, day),
            "@googletest//:gtest_main"
        ],
    )

def aoc_binaries(year):
    for day in range(1, 26):
        aoc(year, day)