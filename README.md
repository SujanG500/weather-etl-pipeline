<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Weather ETL Pipeline with Astronomer & Apache Airflow</title>
</head>
<body>

  <h1>Weather ETL Pipeline with Astronomer & Apache Airflow</h1>

  <h2>Project Overview</h2>
  <p>
    This project is built using Astronomer and Apache Airflow to automate the process of extracting, transforming, and loading weather data. It leverages Docker containers for local development and deployment, providing a scalable, reliable data pipeline framework.
  </p>

  <h2>What's Inside</h2>
  <ul>
    <li><strong>dags/</strong><br />
      Contains Python scripts defining your Airflow DAGs. This project includes a custom DAG to fetch and process weather data via APIs.
    </li>
    <li><strong>Dockerfile</strong><br />
      Defines the custom runtime environment based on Astronomer’s Airflow image, allowing you to customize dependencies and runtime behavior.
    </li>
    <li><strong>include/</strong><br />
      A folder to add any additional project files or scripts you want bundled with your deployment.
    </li>
    <li><strong>packages.txt</strong><br />
      Use this file to specify any operating system packages required by your project.
    </li>
    <li><strong>requirements.txt</strong><br />
      Lists Python dependencies for your Airflow DAGs and plugins.
    </li>
    <li><strong>plugins/</strong><br />
      Place custom Airflow plugins here to extend Airflow’s functionality.
    </li>
    <li><strong>airflow_settings.yaml</strong><br />
      Local-only config file to manage Airflow connections, variables, and pools without manual UI configuration.
    </li>
  </ul>

  <h2>Running the Project Locally</h2>
  <p>To start Airflow locally using Astronomer:</p>
  <pre><code>astro dev start</code></pre>
  <p>This will launch several Docker containers for:</p>
  <ul>
    <li><strong>Postgres:</strong> Airflow metadata database</li>
    <li><strong>Scheduler:</strong> Manages task scheduling</li>
    <li><strong>DAG Processor:</strong> Parses DAG files</li>
    <li><strong>API Server:</strong> Hosts Airflow UI and API</li>
    <li><strong>Triggerer:</strong> Handles deferred task triggers</li>
  </ul>
  <p>Once ready, open your browser to <a href="http://localhost:8080">http://localhost:8080</a> to access the Airflow UI.</p>
  <p>Postgres database connection details:<br />
    Host: <code>localhost</code><br />
    Port: <code>5432</code><br />
    User: <code>postgres</code><br />
    Password: <code>postgres</code>
  </p>
  <p><strong>Note:</strong> If these ports are already in use, please stop conflicting services or update port configurations. See <a href="https://www.astronomer.io/docs/astro/cli/troubleshoot-locally#ports-are-not-available-for-my-local-airflow-webserver" target="_blank" rel="noopener noreferrer">Astronomer troubleshooting guide</a>.</p>

  <h2>Deployment to Astronomer Cloud</h2>
  <p>If you have an Astronomer Cloud account, deploying your code is seamless:</p>
  <ul>
    <li>Commit and push your code to your connected GitHub repository</li>
    <li>Astronomer automatically builds and deploys your project</li>
  </ul>
  <p>For detailed deployment instructions, visit the <a href="https://www.astronomer.io/docs/astro/deploy-code/" target="_blank" rel="noopener noreferrer">Astronomer docs</a>.</p>

  <h2>Support and Contribution</h2>
  <p>This project is maintained with support from the Astronomer team. For bug reports, feature requests, or questions, please contact <a href="https://www.astronomer.io/support" target="_blank" rel="noopener noreferrer">Astronomer Support</a>.</p>

</body>
</html>
