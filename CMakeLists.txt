cmake_minimum_required(VERSION 3.16)

project(openscad-newsfeed-lint VERSION 0.0.1 LANGUAGES)

find_package(Python3 COMPONENTS Interpreter)

set(NEWS_SCRIPT ${CMAKE_CURRENT_SOURCE_DIR}/scripts/news.py)
set(NEWS_SOURCE ${CMAKE_CURRENT_SOURCE_DIR}/data/news.yaml)
set(NEWS_OUTPUT news.jsonp)

set(GALLERY_SCRIPT ${CMAKE_CURRENT_SOURCE_DIR}/scripts/gallery.py)
set(GALLERY_SOURCE ${CMAKE_CURRENT_SOURCE_DIR}/data/gallery.yaml)
set(GALLERY_OUTPUT gallery.jsonp)

add_custom_target(news ALL COMMAND ${Python3_EXECUTABLE} ${NEWS_SCRIPT} ${NEWS_SOURCE} -o ${NEWS_OUTPUT} DEPENDS ${NEWS_SOURCE})
add_custom_target(gallery ALL COMMAND ${Python3_EXECUTABLE} ${GALLERY_SCRIPT} ${GALLERY_SOURCE} -o ${GALLERY_OUTPUT} DEPENDS ${GALLERY_SOURCE})
