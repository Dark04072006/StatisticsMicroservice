-- statistics table
-- depends: 
CREATE TABLE IF NOT EXISTS statistics (
    id UUID PRIMARY KEY,
    date TIMESTAMP NOT NULL,
    views INT,
    clicks INT,
    cost FLOAT,
    CONSTRAINT positive_views CHECK (views >= 0),
    CONSTRAINT positive_clicks CHECK (clicks >= 0),
    CONSTRAINT positive_cost CHECK (cost >= 0)
);
