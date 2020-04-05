#!/usr/bin/env python

import filecmp
import inspect
import shutil
import os

import utils

dir_name = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))


def main():
    include_dir = os.path.join(dir_name, "../Includes/AlphaTFT")

    file_names = utils.get_all_files(include_dir, ["*.hpp"])
    file_names.sort()

    header = os.path.join(dir_name, "../Includes/AlphaTFT/AlphaTFT.hpp")
    header_tmp = header + ".tmp"
    with open(header_tmp, "w") as header_file:
        header_file.write("""// Copyright (c) 2020 Chris Ohk, Chanho Park, Eddie Lee, Gyojun Youn

// We are making my contributions/submissions to this project solely in our
// personal capacity and are not conveying any rights to any intellectual
// property of any third parties.\n
""")
        header_file.write("#ifndef ALPHATFT_ALPHATFT_HPP\n")
        header_file.write("#define ALPHATFT_ALPHATFT_HPP\n\n")
        for filename in file_names:
            line = "#include <AlphaTFT/%s>\n" % filename
            header_file.write(line)
        header_file.write("\n#endif  // ALPHATFT_ALPHATFT_HPP\n")

    if not filecmp.cmp(header, header_tmp):
        shutil.move(header_tmp, header)
    else:
        os.remove(header_tmp)


if __name__ == "__main__":
    main()
