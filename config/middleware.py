import time


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.perf_counter()

        response = self.get_response(request)

        end_time = time.perf_counter()

        duration = (end_time - start_time) * 1000

        print(
            f"{request.method} | "
            f"{request.path} | "
            f"{response.status_code} | "
            f"{duration:.2f} ms"
        )

        return response