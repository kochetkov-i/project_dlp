window.addEventListener('load', () => {
    const bars = document.querySelectorAll('.progress-bar')
    bars.forEach((bar) => {
        const amount = parseInt(bar.getAttribute("aria-valuenow"), 10)
        const target = parseInt(bar.getAttribute("aria-valuemax"), 10)
        if(amount >= target){
            bar.setAttribute("style", "width: 100%")
        }
        else{
            const percent = Math.floor((amount * 100)/target)
            bar.setAttribute("style", "width:" + percent + "%")
        }
    })      
})