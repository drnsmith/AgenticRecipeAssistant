## Agentic Recipe Assistant

### Scenario: Where Data Science Meets Software Engineering
You're part of a team at a cutting-edge culinary tech company, tasked with developing an AI-driven recipe assistant. The goal is simple. It also transformative: empower users to create and customise recipes based on their unique preferences, available ingredients, and dietary needs—all without endless web searches or scrolling through blogs.

This project represents the perfect intersection of data science and software engineering:

 - As a **data scientist**, you focus on leveraging cutting-edge Large Language Models (LLMs) to generate personalised recipes. Using a rich dataset of culinary knowledge, you design algorithms that can adapt to user input, refine recipes dynamically, and offer insightful suggestions.
 - As a **software engineer**, you build the infrastructure to bring this vision to life. You create APIs, develop an interactive frontend, and ensure the system runs efficiently, scalably, and seamlessly across devices.

Together, your work enables the assistant to:
 - Suggest recipes based on the user’s available ingredients.
 - Offer real-time adjustments (e.g., "Make it spicier" or "Add a vegetarian option").
 - Provide step-by-step instructions for preparing dishes.
 - Learn and adapt to user preferences over time, creating a truly personalised culinary experience.

### Overview
The **Agentic Recipe Assistant** is an AI-powered solution designed to transform the way users create and customise cooking recipes. Using cutting-edge technologies, including Large Language Models (LLMs), this system generates personalised recipes based on user inputs, such as available ingredients, dietary preferences, and cooking styles. 

The assistant adapts to user feedback, refines its suggestions, and learns over time, offering a seamless and interactive recipe-generation experience.
So, this project is about creating a robust pipeline where data science powers the intelligence, and software engineering ensures the delivery—offering users an assistant that truly feels like their own personal chef.

---

### Features
- **Ingredient-based recipe generation:** Provide a list of ingredients, and the assistant generates tailored recipes.
- **Customisable recipes:** Adjust recipes based on preferences like dietary restrictions, cuisine, or cooking methods.
- **Real-time adaptation:** Modify recipes dynamically (e.g., "Make it spicier" or "Add a vegetarian option").
- **Recipe variations:** Generate multiple versions of a recipe, from quick and simple to gourmet.
- **Proactive suggestions:** Offers complementary ingredient ideas and side dishes.
- **Learning capability:** Learns user preferences over time for personalised recommendations.

---

### Technologies used
- **Frontend:** React.js for the user interface.
- **Backend:** FastAPI for API endpoints.
- **LLM integration:** OpenAI's GPT or Hugging Face models for recipe generation.
- **Data storage:** Azure Data Lake for storing recipe and user data.
- **Data processing:** PySpark for data pre-processing.
- **Deployment:** Docker and Kubernetes for scalable deployments.
- **Orchestration:** Apache Airflow for pipeline automation.

---

### Installation and setup

#### Prerequisites
1. **Python 3.8+**
2. **Node.js and npm** (for frontend development)
3. **Docker** (for containerisation)
4. API keys for:
   - OpenAI GPT-3 or Hugging Face models
   - Azure services (or alternative cloud providers for data storage)

#### Clone the repository
```bash
$ git clone https://github.com/drnsmith/AgenticRecipeAssistant.git
$ cd AgenticRecipeAssistant
```
#### Backend Setup
1. Create a virtual environment:
   ```bash
   $ python -m venv env
   $ source env/bin/activate   # On Windows: env\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   $ pip install -r requirements.txt
   ```
3. Set up environment variables in `.env`:
   ```env
   OPENAI_API_KEY=your_openai_key
   AZURE_STORAGE_KEY=your_azure_storage_key
   DATABASE_URL=your_database_url
   ```
4. Run the backend:
   ```bash
   $ uvicorn app.main:app --reload
   ```

#### Frontend Setup
1. Navigate to the `frontend` folder:
   ```bash
   $ cd frontend
   ```
2. Install dependencies:
   ```bash
   $ npm install
   ```
3. Start the development server:
   ```bash
   $ npm start
   ```

#### Docker Setup (Optional)
1. Build and run Docker containers:
   ```bash
   $ docker-compose up --build
   ```

---

#### Usage
1. Access the app via your browser at `http://localhost:3000`.
2. Enter your ingredients and preferences.
3. Receive personalised recipes and interact with the assistant for adjustments or variations.

---

#### Project Structure
```
agentic-recipe-assistant/
├── app/
│   ├── main.py         # FastAPI app
│   ├── models/         # Data models
│   │   └── __init__.py
│   ├── services/       # Business logic
│   │   ├── __init__.py
│   │   └── recipe_service.py
│   ├── utils/          # Helper functions
│   │   └── __init__.py
│   └── .env            # Environment variables
├── frontend/           # Frontend application (React.js)
├── data/               # Data processing scripts and datasets
├── tests/              # Unit and integration tests
├── Dockerfile          # Docker configuration for backend
├── docker-compose.yml  # Multi-container setup
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation

```

---

#### Roadmap
- [ ] Integrate recipe variation generation.
- [ ] Add IoT integration for smart fridges.
- [ ] Implement nutritional analysis for recipes.
- [ ] Expand multi-agent collaboration features.

---

### Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add feature-name'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

---

### License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

