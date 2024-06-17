from rest_framework import serializers

class CompanyFilterSerializer(serializers.Serializer):
    country = serializers.IntegerField(required=False)
    state = serializers.IntegerField(required=False)
    city = serializers.IntegerField(required=False)
    current_employee_estimate_from = serializers.IntegerField(required=False)
    current_employee_estimate_to = serializers.IntegerField(required=False)

    def validate(self, data):
        # Validate that if 'current_employee_estimate_from' is provided, 'current_employee_estimate_to' must also be provided
        if 'current_employee_estimate_from' in data and 'current_employee_estimate_to' not in data:
            raise serializers.ValidationError("Both 'current_employee_estimate_from' and 'current_employee_estimate_to' are required.")
        if 'current_employee_estimate_to' in data and 'current_employee_estimate_from' not in data:
            raise serializers.ValidationError("Both 'current_employee_estimate_from' and 'current_employee_estimate_to' are required.")
        return data