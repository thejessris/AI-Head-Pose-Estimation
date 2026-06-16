const yawValue = document.getElementById("yaw");
const pitchValue = document.getElementById("pitch");
const rollValue = document.getElementById("roll");

const attentionValue =
document.getElementById("attention");

const statusValue =
document.getElementById("status");

const progressBar =
document.getElementById("progress-bar");

async function fetchPoseData(){

    try{

        const response =
        await fetch("/pose_data");

        const data =
        await response.json();

        yawValue.innerHTML =
        data.yaw + "°";

        pitchValue.innerHTML =
        data.pitch + "°";

        rollValue.innerHTML =
        data.roll + "°";

        attentionValue.innerHTML =
        data.attention_score + "%";

        progressBar.style.width =
        data.attention_score + "%";

        if(Math.abs(data.yaw) > 25){

            statusValue.innerHTML =
            "Looking Away";

            statusValue.style.color =
            "#ef4444";

        }
        else{

            statusValue.innerHTML =
            "Attentive";

            statusValue.style.color =
            "#22c55e";
        }

    }
    catch(error){

        console.log(error);

    }

}

setInterval(fetchPoseData,500);
