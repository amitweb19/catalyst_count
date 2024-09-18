from datetime import date

class ValidationError(Exception):
      pass


def validate_workgroup_dates(today: date, work_start_date: date, work_end_date: date):
      # Start date cannot be in the past
      if work_start_date < today:
            raise ValidationError("Start date cannot be in the past")
      
      # End date cannot be in the past
      if work_end_date < today:
            raise ValidationError("End date cannot be in the past")
      
      # Workgroup Start date <= Workgroup End date
      if work_start_date > work_end_date:
            raise ValidationError("End date cannot be before the start date")
      
      # Workgroup Start date != Workgroup End date
      if work_start_date == work_end_date:
            raise ValidationError("Start date and end date cannot be the same")


def validate_with_position_dates(work_start_date: date, work_end_date: date, pos_start_date: date, pos_end_date: date):
      # Start date cannot be before the position's start date
      if work_start_date < pos_start_date:
            raise ValidationError("Start date cannot be before the position's start date")
      
      # End date cannot be beyond the position's end date
      if work_end_date > pos_end_date:
            raise ValidationError("End date cannot be beyond the position's end date")


def validate_valid_date(work_start_date, work_end_date):
      try:
            # If dates are invalid, this would raise an error during date construction
            date.fromisoformat(str(work_start_date))
            date.fromisoformat(str(work_end_date))
      except ValueError:
            raise ValidationError("Start date and End date must be valid dates")


# Example scenarios

def run_scenarios():
      today = date.today()

      scenarios = [
      # 1. Workgroup start date = position start date and workgroup end date = position end date
            {
                  'work_start_date': date(2024, 9, 1),
                  'work_end_date': date(2034, 9, 1),
                  'pos_start_date': date(2024, 9, 1),
                  'pos_end_date': date(2034, 9, 1),
                  'expected': 'success'
            },
     # 2. Workgroup start date = position start date and workgroup end date = position end date-1 year
            {
                  'work_start_date': date(2024, 9, 1),
                  'work_end_date': date(2033, 9, 1),
                  'pos_start_date': date(2024, 9, 1),
                  'pos_end_date': date(2034, 9, 1),
                  'expected': 'success'
            },

     # 3. Workgroup start date = position start date + 1 year and workgroup end date = position end date
            {
                  'work_start_date': date(2025, 9, 1),
                  'work_end_date': date(2034, 9, 1),
                  'pos_start_date': date(2024, 9, 1),
                  'pos_end_date': date(2034, 9, 1),
                  'expected': 'success'
            },
     # 4. Workgroup start date > position start date and workgroup end date = position end date
            {
                  'work_start_date': date(2024, 9, 1),
                  'work_end_date': date(2034, 1, 1),
                  'pos_start_date': date(2024, 1, 1),
                  'pos_end_date': date(2034, 1, 1),
                  'expected': 'success'
            },
     # 5. Workgroup start date in past
            {
                  'work_start_date': date(2024, 1, 1),
                  'work_end_date': date(2034, 1, 1),
                  'pos_start_date': date(2024, 1, 1),
                  'pos_end_date': date(2034, 1, 1),
                  'expected': 'fail',
                  'error': 'Start date cannot be in the past'
            },




     # 6. Workgroup start date = end date
            {
                  'work_start_date': date(2024, 9, 1),
                  'work_end_date': date(2024, 9, 1),
                  'pos_start_date': date(2024, 1, 1),
                  'pos_end_date': date(2034, 1, 1),
                  'expected': 'fail',
                  'error': 'Start date and end date cannot be the same'
            },
     # 7. Workgroup start date > end date
            {
                  'work_start_date': date(2024, 10, 2),
                  'work_end_date': date(2024, 10, 1),
                  'pos_start_date': date(2024, 1, 1),
                  'pos_end_date': date(2034, 1, 1),
                  'expected': 'fail',
                  'error': 'End date cannot be before the start date'
            },
     # 8. Workgroup start date is future and workgroup end date < workgroup start date and today's date
            {
                  'work_start_date': date(2024, 10, 2),
                  'work_end_date': date(2024, 9, 2),
                  'pos_start_date': date(2024, 1, 1),
                  'pos_end_date': date(2034, 1, 1),
                  'expected': 'fail',
                  'error': 'End date cannot be in the past'
            },
     # 9. Workgroup end date > position's end date
            {
                  'work_start_date': date(2024, 10, 2),
                  'work_end_date': date(2034, 8, 2),
                  'pos_start_date': date(2024, 1, 1),
                  'pos_end_date': date(2034, 1, 1),
                  'expected': 'fail',
                  'error': 'End date cannot be beyond the position\'s end date'
            },


     # 10. Workgroup start and end dates in the past
            {
                  'work_start_date': date(2024, 1, 1),
                  'work_end_date': date(2024, 1, 1),
                  'pos_start_date': date(2024, 1, 1),
                  'pos_end_date': date(2034, 1, 1),
                  'expected': 'fail',
                  'error': 'Start date and end date cannot be the same'
            },
     # 11. Invalid date for start date
            {
                  'work_start_date': '2024-99-01',  # Invalid date
                  'work_end_date': '2034-09-01',
                  'pos_start_date': '2024-09-01',
                  'pos_end_date': '2034-09-01',
                  'expected': 'fail',
                  'error': 'Start date must be a valid date'
            },
      ]




      for i, scenario in enumerate(scenarios, 1):
         try:
            if isinstance(scenario['work_start_date'], str):
               validate_valid_date(scenario['work_start_date'], scenario['work_end_date'])
            else:
               # Validate workgroup dates
               validate_workgroup_dates(today, scenario['work_start_date'],                                              scenario['work_end_date'])
                        
               # Validate with position dates
               validate_with_position_dates(scenario['work_start_date'], scenario['work_end_date'], scenario['pos_start_date'], scenario['pos_end_date'])

               result = 'success'
        except ValidationError as e:
               result = 'fail'
               error_message = str(e)
            
        expected_result = scenario.get('expected')
        if expected_result == 'success':
           assert result == 'success', f"Scenario {i} failed. Expected: success, Got: {result}"
        else:
           assert result == 'fail' and error_message == scenario['error'], f"Scenario {i} failed. Expected: {scenario['error']}, Got: {error_message}"

     print("All test scenarios passed!")



# Run the scenarios
run_scenarios()
