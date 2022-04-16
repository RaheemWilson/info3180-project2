export default{
    async getCrsfToken(){
        let res = await fetch('/api/csrf-token', {
            method: 'GET'
        })

        return await res.json()
    }
}