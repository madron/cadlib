# cadlib

### Activate environment
conda activate cadquery

### Add module to path
ln -s `realpath cl` ~/.conda/envs/cadquery/lib/python3.10/site-packages/cl

### CadQuery server
docker run --rm -d -p 5000:5000 -v ${PWD}/cl:/opt/conda/envs/cq/lib/python3.8/site-packages/cl:ro --name cqs cadquery/cadquery-server
docker logs -f cqs
docker stop cqs
