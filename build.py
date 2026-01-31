import subprocess

cmake_generate_command = [
    "cmake",
    "-S .",
    "-B build",
    "-G Ninja",
    "-D CMAKE_CXX_COMPILER=clang++",
    "-D CMAKE_BUILD_TYPE=None",
    "-D CMAKE_EXPORT_COMPILE_COMMANDS=ON",
]

cmake_build_command = ["cmake", "--build", "build"]

subprocess.run(cmake_generate_command)
subprocess.run(cmake_build_command)
