def get_status():
    return {
        "application": "lab-021-jenkins-demo",
        "status": "healthy"
    }

if __name__ == "__main__":
    print(get_status())
