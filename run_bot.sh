if [ "$(pwd -PW 2> /dev/null)" ]; then _pwd="pwd -PW"; else _pwd="pwd -P"; fi

self_dir="$(cd "$(dirname "$0")"; ${_pwd})"

image_name="skomorokh"



docker build -t ${image_name} ${self_dir}/docker

docker run -it --rm -v ${self_dir}:/skomorokh ${image_name}
