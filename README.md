
This repository contains the source code of a Django application called API-project, which consists of two services:

1. **depth_service**: A service that takes an image as input and returns its estimated depth.
2. **llm_service**: A service that utilizes a Language Model (LLM) to answer questions based on a PDF document provided by the user.

## Requirements

Make sure you have Docker and Docker Compose installed on your machine before starting the services.

## Installation and Usage

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your-user/api-project.git
    ```

2. Navigate to the cloned directory:

    ```bash
    cd api-project
    ```

3. Run Docker Compose to build and start the services:

    ```bash
    docker-compose up --build
    ```

    This will start the `depth_service` and `llm_service` in separate Docker containers.

4. Access the services at the following URL:

    - http://localhost:8001

## How to Use

- **depth_service**: Send an image to `/depth/` using a POST request and receive the estimated depth of the image as a response.
- **llm_service**: Send a PDF document and a question to `/llm/` using a POST request and receive a response based on the document content.

## Contribution

Contributions are welcome! Feel free to open issues or submit pull requests with improvements.

## License

This project is licensed under the [MIT License](LICENSE).
