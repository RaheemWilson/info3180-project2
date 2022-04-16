export default {
    /**
     * 
     * @param {*} payload Contain's the user's password and username
     * @returns JWT Token if successful else returns errors
     */
    async login(payload, csrf){
        let res = await fetch('/api/auth/login', {
            method: "POST",
            body: JSON.stringify(payload),
            headers: {
                "Content-Type": "application/json",
                'X-CSRFToken': csrf
            },
        })

        return res.json()
    },

    async register(payload, csrf){
        let res = await fetch('/api/register', {
            method: "POST",
            body: payload,
            headers: {
                'X-CSRFToken': csrf
            }
        })

        return res.json()
    }


}