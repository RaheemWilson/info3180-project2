import store from '../store/store'
export default{
    async add(payload, csrf){
        let res = await fetch('/api/cars', {
            method: "POST",
            body: payload,
            headers: {
                'Authorization': `Bearer ${ store.getters.getAuth || localStorage.getItem('authToken')}`,
                'X-CSRFToken': csrf
            }
        })

        return res.json()
    },
    async search(make, model){
        let res = await fetch(`/api/search?make=${make}&model=${model}`, {
            method: "GET",
            headers: {
                'Authorization': `Bearer ${ store.getters.getAuth || localStorage.getItem('authToken')}`,
            }
        })

        return res.json()
    }
}