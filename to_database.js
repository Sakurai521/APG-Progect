// other variables
const database_name = "test";
const interval = 10000; // in milliseconds

// Do not change code below
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.0/firebase-app.js";
import { getFirestore, serverTimestamp, collection, addDoc } from "https://www.gstatic.com/firebasejs/10.7.0/firebase-firestore.js";
// Initialize Firebase
const firebaseConfig = {
    apiKey: "AIzaSyDpBOrJoi8aLeF6qCwuNJ8fBZfAJ-fydFc",
    authDomain: "apg-project-6e243.firebaseapp.com",
    projectId: "apg-project-6e243",
    storageBucket: "apg-project-6e243.appspot.com",
    messagingSenderId: "707707789871",
    appId: "1:707707789871:web:8ec23d101d48c0adb4dcda",
    measurementId: "G-WYP4CLL864"
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

// counter variables
let button1_count = 0;
let button2_count = 0;

// send to firebase every interval
window.onload = function(){setInterval(function(){
var dt = new Date();
// alert(button1_count, button2_count);
const docRef = addDoc(collection(db, database_name), {
        "button1": button1_count,
        "button2": button2_count,
        "date": serverTimestamp()
    });
    button1_count = 0;
    button2_count = 0;
}, interval);
}

// increment button1-counter variables
var button1 = document.getElementById('button1');
button1.addEventListener('click', function() {
        button1_count++;
}, false);

// increment button2-counter variables
var button2 = document.getElementById('button2');
button2.addEventListener('click', function(){
    button2_count++;
}, false);