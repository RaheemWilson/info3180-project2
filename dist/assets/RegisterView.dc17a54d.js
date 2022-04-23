import{_,T as v,A as y,o as d,c,a as e,F as w,r as b,t as m,b as p,w as n,v as a,d as U,p as f,e as h,f as F,g as x}from"./index.a920636c.js";const V={data(){return{username:"",password:"",fullname:"",email:"",location:"",biography:"",photo:"",errors:null,message:"",csrf:""}},async created(){let r=await v.getCrsfToken();this.csrf=r.csrf_token},methods:{handleFileUpload(){this.photo=this.$refs.photo.files[0]},async registerUser(){let r=document.getElementById("registerForm"),o=new FormData(r),i=await y.register(o,this.csrf);console.log(i),i!=null&&i.errors?(this.errors=[...i.errors],setTimeout(()=>{this.errors=null},1500)):(this.error=null,this.message="Account was successfully created",setTimeout(()=>{this.$router.push("/login")},1500))}}},l=r=>(f("data-v-492ae7ce"),r=r(),h(),r),k={class:"register-form"},I={key:0,class:"alert alert-danger"},R={key:1,class:"alert alert-success",role:"alert"},S={class:"row"},q={class:"form-field col"},T=l(()=>e("label",{for:"username"},"Username",-1)),B={class:"form-field col"},N=l(()=>e("label",{for:"password"},"Password",-1)),A={class:"row"},C={class:"form-field col"},D=l(()=>e("label",{for:"fullname"},"Full Name",-1)),E={class:"form-field col"},M=l(()=>e("label",{for:"email"},"Email",-1)),j={class:"row"},L={class:"form-field col"},z=l(()=>e("label",{for:"location"},"Location",-1)),O=l(()=>e("div",{class:"col"},null,-1)),P={class:"form-field"},Z=l(()=>e("label",{for:"biography"},"Biography",-1)),G={class:"form-field"},H=l(()=>e("label",{for:"photo"},"Upload photo",-1)),J=l(()=>e("button",{type:"submit",class:"submit-btn"},"Register",-1));function K(r,o,i,g,t,u){return d(),c("div",k,[t.errors?(d(),c("div",I,[e("ul",null,[(d(!0),c(w,null,b(t.errors,s=>(d(),c("li",{key:t.errors.indexOf(s)},m(s),1))),128))])])):p("",!0),t.message?(d(),c("div",R,m(t.message),1)):p("",!0),e("form",{onSubmit:o[7]||(o[7]=U((...s)=>u.registerUser&&u.registerUser(...s),["prevent"])),method:"post",enctype:"multipart/form-data",id:"registerForm"},[e("div",S,[e("div",q,[T,n(e("input",{type:"text",name:"username",id:"username","onUpdate:modelValue":o[0]||(o[0]=s=>t.username=s),required:""},null,512),[[a,t.username]])]),e("div",B,[N,n(e("input",{type:"password",name:"password",id:"password",pattern:"(?=.*\\d)(?=.*[a-z])(?=.*[A-Z]).{8,}",title:"Must contain at least one  number and one uppercase and lowercase letter, and at least 8 or more characters","onUpdate:modelValue":o[1]||(o[1]=s=>t.password=s),required:""},null,512),[[a,t.password]])])]),e("div",A,[e("div",C,[D,n(e("input",{type:"text",name:"fullname",id:"fullname","onUpdate:modelValue":o[2]||(o[2]=s=>t.fullname=s),required:""},null,512),[[a,t.fullname]])]),e("div",E,[M,n(e("input",{type:"email",name:"email",id:"email","onUpdate:modelValue":o[3]||(o[3]=s=>t.email=s),required:""},null,512),[[a,t.email]])])]),e("div",j,[e("div",L,[z,n(e("input",{type:"text",name:"location",id:"location","onUpdate:modelValue":o[4]||(o[4]=s=>t.location=s),required:""},null,512),[[a,t.location]])]),O]),e("div",P,[Z,n(e("textarea",{name:"biography",id:"biography","onUpdate:modelValue":o[5]||(o[5]=s=>t.biography=s),cols:"30",rows:"10",required:""},null,512),[[a,t.biography]])]),e("div",G,[H,e("input",{type:"file",name:"photo",id:"photo",ref:"photo",accept:"image/png, image/jpg, image/jpeg",required:"",onChange:o[6]||(o[6]=(...s)=>u.handleFileUpload&&u.handleFileUpload(...s))},null,544)]),J],32)])}var Q=_(V,[["render",K],["__scopeId","data-v-492ae7ce"]]);const W={components:{RegisterForm:Q}},X=r=>(f("data-v-3d5d9f6b"),r=r(),h(),r),Y={class:"register-container"},$={class:"register-content"},ee=X(()=>e("h1",null,"Register New User",-1));function se(r,o,i,g,t,u){const s=F("RegisterForm");return d(),c("div",Y,[e("div",$,[ee,x(s)])])}var te=_(W,[["render",se],["__scopeId","data-v-3d5d9f6b"]]);export{te as default};
