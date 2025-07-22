up:
	podman compose up -d --build --remove-orphans

down:
	podman compose down

shell:
	podman compose exec sandbox-py bash
