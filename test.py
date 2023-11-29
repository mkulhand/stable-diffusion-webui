import torch

def main():
    torch_version = torch.__version__
    cuda_version = torch.version.cuda

    print(f'Torch Version: {torch_version}')
    print(f'CUDA Version: {cuda_version}')

if __name__ == "__main__":
    main()
