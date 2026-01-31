cmake_minimum_required(VERSION 3.31)

project(simple-log-viewer
    VERSION 1.0
    DESCRIPTION "A simple log viewer application"
    LANGUAGES CXX
)

add_executable(test
    src/main.cpp
)

target_sources(test PRIVATE
    FILE_SET HEADERS FILES
)

set_target_properties(test PROPERTIES
    CXX_STANDARD 23
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/bin"
)
