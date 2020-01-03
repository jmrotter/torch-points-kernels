from setuptools import setup, find_packages
from torch.utils.cpp_extension import BuildExtension, CUDAExtension, CUDA_HOME
import glob
import torch_points

ext_src_root = "cuda"
ext_sources = glob.glob("{}/src/*.cpp".format(ext_src_root)) + glob.glob(
    "{}/src/*.cu".format(ext_src_root)
)

ext_modules = []
if CUDA_HOME:
    ext_modules.append(
        CUDAExtension(
            name="torch_points.points_cuda",
            sources=ext_sources,
            extra_compile_args={
                "cxx": ["-O2", "-I{}".format("{}/include".format(ext_src_root))],
                "nvcc": ["-O2", "-I{}".format("{}/include".format(ext_src_root))],
            },
        )
    )

setup(
    name="torch_points",
    version="0.1.1",
    author="Nicolas Chaulet",
    packages=find_packages(),
    install_requires=[],
    ext_modules=ext_modules,
    cmdclass={"build_ext": BuildExtension},
)