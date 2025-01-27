from datetime import datetime

class SalaryMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            user = request.user
            experience = user.experience_years

            if experience >= 1 and experience <= 3:
                salary = 1000
            elif experience > 3 and experience <= 7:
                salary = 2000
            elif experience > 7 and experience <= 10:
                salary = 5000
            else:
                salary = 0

            request.user.salary = salary
        response = self.get_response(request)
        return response