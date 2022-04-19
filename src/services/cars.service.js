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
    },
    async getAll(){
        let res = await fetch(`/api/cars`, {
            method: "GET",
            headers: {
                'Authorization': `Bearer ${ store.getters.getAuth || localStorage.getItem('authToken')}`,
            }
        })

        return res.status === 200 ? res.json() : null
    },
    async getCar(id){
        let res = await fetch(`/api/cars/${id}`, {
            method: "GET",
            headers: {
                'Authorization': `Bearer ${ store.getters.getAuth || localStorage.getItem('authToken')}`,
            }
        })

        return res.status === 200 ? res.json() : null
    },
    async querySearch(make, model){
        let res = await fetch(`/api/search?make=${make}&model=${model}`, {
            method: "GET",
            headers: {
                'Authorization': `Bearer ${ store.getters.getAuth || localStorage.getItem('authToken')}`,
            }
        })

        return res.status === 200 ? res.json() : null
    },
    async addFav(id, csrf){
        let res = await fetch(`/api/cars/${id}/favourite`, {
            method: "POST",
            body: JSON.stringify({
                "car_id": id,
                "user_id": store.getters.getUser || localStorage.getItem('id')
            }),
            headers: {
                'Content-type': 'application/json',
                'Authorization': `Bearer ${ store.getters.getAuth || localStorage.getItem('authToken')}`,
                'X-CSRFToken': csrf
            }
        })

        return res.json()
    },


}