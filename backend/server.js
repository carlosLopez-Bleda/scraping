const express = require("express");
const cors = require("cors");
const fs = require("fs");
const path = require("path");

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());

// 🆕 Servir el frontend desde /public
app.use(express.static(path.join(__dirname, "public")));

// Ruta principal para mostrar el frontend
app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "public", "index.html"));
});

// Rutas de API
app.get("/api/libros", (req, res) => {
    const filePath = path.join(__dirname, "libros_populares.json");
    fs.readFile(filePath, "utf8", (err, data) => {
        if (err) return res.status(500).json({ error: "Error al leer el archivo JSON" });
        res.json(JSON.parse(data));
    });
});

app.get("/api/noticias", (req, res) => {
    const filePath = path.join(__dirname, "noticias.json");
    fs.readFile(filePath, "utf8", (err, data) => {
        if (err) return res.status(500).json({ error: "Error al leer el archivo de noticias" });
        res.json(JSON.parse(data));
    });
});

// Iniciar el servidor
app.listen(PORT, () => {
    console.log(`🚀 Servidor corriendo en http://localhost:${PORT}`);
});
