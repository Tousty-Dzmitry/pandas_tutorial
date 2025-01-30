

# Переменные
PYTHON := python
PIP := pip
VENV := venv
REQ := requirements.txt

# Создание виртуального окружения
.PHONY: venv
venv:
	$(PYTHON) -m venv $(VENV)
	$(VENV)/bin/$(PIP) install --upgrade pip
	$(VENV)/bin/$(PIP) install -r $(REQ)

# Установка зависимостей
.PHONY: install
install: venv
	$(VENV)/bin/$(PIP) install -r $(REQ)

# Запуск основного скрипта
.PHONY: run
run:
	$(VENV)/bin/$(PYTHON) script.py

# Проверка кода линтером
.PHONY: lint
lint:
	$(VENV)/bin/$(PIP) install flake8
	$(VENV)/bin/flake8 .

# Удаление виртуального окружения
.PHONY: clean
clean:
	rm -rf $(VENV)
