
# FIXMETL This is generating the protos with incorrect imports.  Figure out why or move protos to a separate project.
python -m grpc_tools.protoc -I.\
 --python_out=. \
 --grpc_python_out=. \
 cosim.proto