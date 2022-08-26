let errCount = 0;
let wordVisibility = false;

// const btn = document.querySelector('.red-btn')
const word = document.querySelector('.display-word').textContent
const displayBtn = document.querySelector('.display-btn')
const hangmanContainer = document.querySelector('.hangman-container')

// hangmanContainer.style.backgroundImage = "url('assets/hangman-1.png')";

const wordLetters = word.split("")
console.log(wordLetters)

window.addEventListener('click', (e) => {
    
    if(e.target.classList.contains('ltr-btn') && e.target.classList.contains('active')){

        e.target.classList.add('passive')
        e.target.classList.remove('active')

        console.log("err count =Z ", errCount)

        if(errCount >= 6) {window.alert("you failed yo!"); location.reload() }

        // else {

            // errCount += 1
            // console.log("err count => ", errCount)
            // hangmanImg = document.querySelector('.hangman-img')
            // hangmanImg.src = `"{% static 'hang/hangman-${errCount}.png' %}"`
        // }

        let found = false;
        wordLetters.forEach(l => {

            if(e.target.id === l){
                
                console.log("matched")
                

                if(!found) found = true;

                console.log("selected all => ",document.querySelectorAll(`.${l}`))
                
                document.querySelectorAll(`.${l}`).forEach(x => {
                    wordLetters.splice(wordLetters.indexOf(l),1)
                    x.style.opacity = "1";
                })
            }
            if(wordLetters.length===0){
                alert("you won!")
                location.reload()
            }
        })
        
        if(!found){
            errCount += 1
            console.log("err count => ", errCount)
            hangmanImg = document.querySelector('.hangman-img')
            let str = undefined
            if(errCount===1) str = "{% static 'hang/hangman-2.png' %}"
            if(errCount===2) str = "{% static 'hang/hangman-3.png' %}"
            if(errCount===3) str = "{% static 'hang/hangman-4.png' %}"
            if(errCount===4) str = "{% static 'hang/hangman-5.png' %}"
            if(errCount===5) str = "{% static 'hang/hangman-6.png' %}"
            if(errCount===6) str = "{% static 'hang/hangman-7.png' %}"
              
            hangmanImg.src = str
        }

    }else if(e.target === displayBtn) {
        let displayWord = document.querySelector('.display-word')
        if(wordVisibility){
            wordVisibility = false;
            displayBtn.textContent = "Show"
            displayWord.style.opacity = 0
        } else {
            wordVisibility = true;
            displayBtn.textContent = "Hide"
            displayWord.style.opacity = 1
        }
    }
    
})