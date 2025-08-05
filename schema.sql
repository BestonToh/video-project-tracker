CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT,
    company TEXT
);

CREATE TABLE projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER,
    title TEXT NOT NULL,
    start_date TEXT,
    status TEXT CHECK (status IN ('In Progress', 'Completed', 'On Hold')),
    phase TEXT CHECK (phase IN ('Assembly', 'Offline Edit', 'Online Edit', 'Colour Grading', 'Delivery')),
    FOREIGN KEY (client_id) REFERENCES clients(client_id)
);

CREATE TABLE deliverables (
    deliverable_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER,
    version TEXT,
    delivery_date TEXT,
    feedback TEXT,
    approved INTEGER CHECK (approved IN (0,1)),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);
