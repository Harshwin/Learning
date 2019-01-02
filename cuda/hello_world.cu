    #include <stdio.h>

    #if defined(__CUDA_ARCH__) && (__CUDA_ARCH__ < 200)
    #error printf is only supported on devices of compute capability 2.0 and higher, please compile with -arch=sm_20 or higher
    #endif

    __global__ void device_greetings()
    {
      printf("Fuck you\n");
    }

    int main(void)
    {
      // greet from the host
      printf("Hello, world from the host!\n");

      // launch a kernel with a single thread to greet from the device
      device_greetings<<<1,10>>>();

      cudaDeviceSynchronize();

      return 0;
    }
