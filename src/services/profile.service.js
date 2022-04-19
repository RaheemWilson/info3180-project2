import store from '../store/store'
export default{
    async getUser(id){
        let res = await fetch(`/api/users/${id}`, {
            method: "GET",
            headers: {
                'Authorization': `Bearer ${ store.getters.getAuth || localStorage.getItem('authToken')}`,
            }
        })

        return res.status === 200 ? res.json() : null
    },
    async getFav(id){
        let res = await fetch(`/api/users/${id}/favourites`, {
            method: "GET",
            headers: {
                'Authorization': `Bearer ${ store.getters.getAuth || localStorage.getItem('authToken')}`,
            }
        })

        return res.status === 200 ? res.json() : null
    },
}
