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
    }
}