// If use the meta function "await" then use async in the function

async function LoadAnimals() {
    const response = await axios.get('http://localhost:8000/animals')
    const animals = response.data
    const list = document.getElementById('animals-list');
    var count = 0;

    list.innerHTML = '';

    animals.forEach(animal => {
        const item = document.createElement('li');

        const line = `
        ------------------------------------------------------------------
        ID: ${animal.id}\nNome: ${animal.name}\nIdade: ${animal.age}\nCor: ${animal.color}\nSexo: ${animal.sex}\nTipo: ${animal.type}
        ------------------------------------------------------------------`;
        if(animal.color == "Branco" || animal.color == "branco"){
            item.style.color = "White";
        }
        if(animal.color == "Preto" || animal.color == "preto"){
            item.style.color = "Black";
            item.style.textShadow = "0.5px 1px white";
            item.style.textDecoration = "solid"
        }
        if(animal.color == "Amarelo" || animal.color == "amarelo"){
            item.style.color = "Yellow";
        }
        if(animal.color == "Laranja" || animal.color == "laranja"){
            item.style.color = "Orange";
        }
        if(animal.color == "Verde" || animal.color == "verde"){
            item.style.color = "Green";
        }
        if(animal.color == "Azul" || animal.color == "azul"){
            item.style.color = "Blue";
        }
        if(animal.color == "Vermelho" || animal.color == "vermelho"){
            item.style.color = "Red";
        }
        item.innerText = line;
        list.appendChild(item);
    });
}

function m_form_deleteByID() {
    const form_animalsID = document.getElementById('form-delete-animal')
    const input_id = document.getElementById('id-animal-to-delete');


    form_animalsID.onsubmit = async(event) => {
        event.preventDefault();
        const animal_id = input_id.value;

        await axios.delete(`http://localhost:8000/animals/${animal_id}`);

        alert(`Animal deletado com sucesso`);
        LoadAnimals();
    }
}

function m_form() {
    const form_animals = document.getElementById('form-animal')
    const input_name = document.getElementById('name');
    const input_type = document.getElementById('type');
    const input_age = document.getElementById('age');
    const input_sex = document.getElementById('sex');
    const input_color = document.getElementById('color');

    form_animals.onsubmit = async(event) => {
        event.preventDefault();
        const animal_name = input_name.value;
        const animal_type = input_type.value;
        const animal_age = input_age.value;
        const animal_sex = input_sex.value;
        const animal_color = input_color.value;

        await axios.post('http://localhost:8000/animals', {
            name: animal_name,
            age: animal_age,
            type: animal_type,
            sex: animal_sex,
            color: animal_color
        })

        alert(`Animal ${animal_name} cadastrado com sucesso`);
        LoadAnimals();
    }

}

function App() {
    console.log('App initialized');
    LoadAnimals();
    m_form();
    m_form_deleteByID();
}

App()