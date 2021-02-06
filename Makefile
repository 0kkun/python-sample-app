up:
		docker-compose up -d
stop:
		docker-compose stop
build:
		docker-compose build
build-up:
		docker-compose up -d --build
down:
		# コンテナ削除
		docker-compose down
work:
		docker-compose exec python3 bash
install:
		# 好きなライブラリをいれる
		docker-compose exec python3 python -m pip install numpy
		docker-compose exec python3 python -m pip install matplotlib
		docker-compose exec python3 python -m pip install networkx
		docker-compose exec python3 python -m pip install pyyaml
		docker-compose exec python3 python -m pip install xlsxwriter
		docker-compose exec python3 python -m pip install tornado
lib-list:
		# インストールされたライブラリのリスト表示 
		docker-compose exec python3 python -m pip list
restart:
		docker-compose restart