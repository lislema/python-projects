import os


def clean_docker():
    # Stop and remove all containers
    os.system("docker stop $(docker ps -a -q)")
    os.system("docker rm $(docker ps -a -q)")

    # Remove all dangling images
    os.system("docker rmi $(docker images -f 'dangling=true' -q)")

    # Remove unused volumes
    os.system("docker volume prune -f")

    print("Docker cleanup completed.")


if __name__ == "__main__":
    clean_docker()
