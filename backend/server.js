const express = require("express");
const cors = require("cors");
const fs = require("fs");
const path = require("path");

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());

// Ruta principal para verificar que el servidor funciona
app.get("/", (req, res) => {
    res.send("🚀 API de Scraping en funcionamiento. Usa /api/libros o /api/noticias.");
});

// Ruta para obtener los libros
app.get("/api/libros", (req, res) => {
    const filePath = path.join(__dirname, "libros_populares.json");

    fs.readFile(filePath, "utf8", (err, data) => {
        if (err) {
            return res.status(500).json({ error: "Error al leer el archivo JSON" });
        }
        res.json(JSON.parse(data));
    });
});

// Ruta para obtener noticias
app.get("/api/noticias", (req, res) => {
    const filePath = path.join(__dirname, "noticias.json");

    fs.readFile(filePath, "utf8", (err, data) => {
        if (err) {
            return res.status(500).json({ error: "Error al leer el archivo de noticias" });
        }
        res.json(JSON.parse(data));
    });
});

// Iniciar el servidor
app.listen(PORT, () => {
    console.log(`🚀 Servidor corriendo en http://localhost:${PORT}`);
});
