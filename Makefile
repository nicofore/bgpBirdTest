clear:
	docker stack rm scapp
	

build:
	docker build ./BIRD -t nfore/bird

start:
	docker stack deploy -c scapp.yml scapp

s:
	docker service create --network n --name target nfore/bird tail -f /dev/null
	docker service create --network n --name neighbor nfore/bird tail -f /dev/null
