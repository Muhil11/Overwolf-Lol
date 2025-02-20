# Champion Coach – AI-Powered Overwolf App

🚀 AI-powered match analysis tool for League of Legends using Overwolf & Flask.

## Features
✅ AI-powered **match analysis** (Flask + scikit-learn)
✅ Real-time **performance insights** based on match history
✅ Overwolf UI integration for an in-game experience

## Installation & Setup

### Backend (Flask) Setup
**Install dependencies:**  
```sh
pip install flask pandas scikit-learn
```
**Run the Flask API:**  
```sh
python champion_coach.py
```
Backend will start on: **http://127.0.0.1:5000/**

### Frontend (React + Vite) Setup
**Install dependencies:**  
```sh
npm install
```
**Start the frontend server:**  
```sh
npm run dev
```
Frontend runs at: **http://localhost:5173/**

### Overwolf Integration
1️⃣ **Package the frontend** into a `.zip` file  
2️⃣ Open **Overwolf Developer Console**  
3️⃣ Click **“Load Unpacked Extension”**  
4️⃣ Select your **frontend zip folder** and load it  
5️⃣ Open **Overwolf** → **My Apps** → **Launch Champion Coach**  

## API Endpoints
### Analyze Match Stats
**POST** `/analyze-match`  
**Example Request:**  
```json
{
  "kills": 5,
  "deaths": 2,
  "assists": 8,
  "cs": 150
}
```
**Example Response:**  
```json
{
  "win_probability": 75.23,
  "suggestions": [
    "Improve creep score for better gold income.",
    "Keep up good positioning for kills."
  ]
}
```

## Contributing
1. Fork the repo & clone it  
2. Create a new branch (`git checkout -b feature-branch`)  
3. Commit your changes (`git commit -m "Added new feature"`)  
4. Push to GitHub (`git push origin feature-branch`)  
5. Create a **Pull Request**  

## License
Champion Coach is open-source and available under the **MIT License**.

