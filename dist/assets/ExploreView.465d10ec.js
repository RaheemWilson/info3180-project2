import{_,C as u,g as i,r as h,o as l,c as n,b as s,d as v,w as c,v as m,F as f,h as k,p as b,e as C,i as y}from"./index.f5b0d47a.js";const w={components:{CarCard:u},data(){return{make:"",model:"",error:!1,message:"",cars:[]}},async beforeMount(){let o=await i.getAll();o?this.cars=[...o.data.slice(-3)]:(this.error=!0,AuthService.handleLogout())},methods:{async searchCars(){let o=await i.querySearch(this.make,this.model);o?(this.error=!1,this.cars=[...o],console.log(o)):(this.error=!0,AuthService.handleLogout())}}},d=o=>(b("data-v-4bd39be9"),o=o(),C(),o),x={class:"about container"},S=d(()=>s("h2",null,"Explore",-1)),g={class:"search-bar"},M={class:"row"},V={class:"form-field col"},B=d(()=>s("label",{for:"make"},"Make",-1)),E={class:"form-field col"},I=d(()=>s("label",{for:"model"},"Model",-1)),A={class:"col"},L={class:"cards-view"};function F(o,t,U,q,r,a){const p=h("CarCard");return l(),n("div",x,[S,s("div",g,[s("form",{method:"post",onSubmit:t[3]||(t[3]=v((...e)=>a.searchCars&&a.searchCars(...e),["prevent"]))},[s("div",M,[s("div",V,[B,c(s("input",{type:"text",name:"make",id:"make","onUpdate:modelValue":t[0]||(t[0]=e=>r.make=e)},null,512),[[m,r.make]])]),s("div",E,[I,c(s("input",{type:"text",name:"model",id:"model","onUpdate:modelValue":t[1]||(t[1]=e=>r.model=e)},null,512),[[m,r.model]])]),s("div",A,[s("button",{type:"submit",class:"submit-btn",onClick:t[2]||(t[2]=(...e)=>a.searchCars&&a.searchCars(...e))},"Search")])])],32)]),s("div",L,[(l(!0),n(f,null,k(r.cars,e=>(l(),y(p,{key:e.id,id:e.id,make:e.make,model:e.model,photo:`../uploads/${e.photo}`,price:e.price,year:e.year},null,8,["id","make","model","photo","price","year"]))),128))])])}var N=_(w,[["render",F],["__scopeId","data-v-4bd39be9"]]);export{N as default};
