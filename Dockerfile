FROM python:3.11

COPY . .
RUN pip install -r requirements.txt
WORKDIR professor_cheat_sheet
RUN python pull_data.py

ENTRYPOINT ["solara", "run", "solara.py", "--host=0.0.0.0", "--port=80"]
