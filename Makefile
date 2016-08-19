deps:
	@pip install -r requirements.txt

clean:
	@find . -name '*.pyc' -delete

run: deps
	@python src/courses.py
	@python src/courses_language.py
	@python src/question_language.py
	@python src/user_profile_courses.py
	@python src/users.py 
	@python src/indicate_course.py clean