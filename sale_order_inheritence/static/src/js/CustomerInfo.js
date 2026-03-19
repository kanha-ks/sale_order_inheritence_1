/** @odoo-module **/
import { registry } from "@web/core/registry";
import { Component, useEffect } from "@odoo/owl";
import { standardWidgetProps } from "@web/views/widgets/standard_widget_props";
import { useService } from "@web/core/utils/hooks";
import { ConfirmationDialog } from "@web/core/confirmation_dialog/confirmation_dialog";

export class CustomerInfo extends Component {
    setup() {
        this.notification = useService("notification");
        this.dialog = useService("dialog");
        this.effect = useService("effect");
        this.orm = useService("orm");
        this.action = useService("action");
        this.title = useService("title");
//        this.user = useService("user");
    }

    showCustomerInfo() {

//            debugger;

//            this.getDataORM();
            //anther is to show the data on the dialog

            const notif = this.env.services.notification;

            notif.add("",{
                title : "Customer Information",
                type : "info", //info, warning, danger, success
                sticky : false, //false is also possible
                className : "p-4",

                buttons : [
                    //dialog button
                    {
                        name : "show dialog",
                        primary : true,
                        onClick : ()=>{
                            console.log("Notification button called")
                            this.getDataORM()
                        },
                    },

//                    //effect button
//                    {
//                        name : "Show Effect",
//                        onClick : ()=>{
//                            console.log("Effect button called");
//                            this.showEffect()
//                        },
//                    },
//
//                    //ORM button
//                    {
//                        name : "ORM method to get data",
//                        onClick : ()=>{
////                            debugger;
//                            console.log("ORM Method called");
//                            this.getDataORM()
//                        },
//                    },
//
//                    //Action Service button
//                    {
//                        name : "Action Service",
//                        onClick : ()=>{
//                            this.getActionService()
//                        },
//                    },
//
//                    //title Service button
//                    {
//                        name : "Title",
//                        onClick : ()=>{
//                            this.getTitle()
//                        },
//                    },
                ],
            });
     }

    showDialog(){

        console.log("Show dialog called");
        const dialog = this.env.services.dialog;

        dialog.add(ConfirmationDialog, {
            title : "This is dialog component",
            body : "Do you want to continue ?",
            confirm : ()=>{console.log("Dialog confirm clicked!!!")},
            cancel : ()=>{console.log("Dialog Cancelled");},
//            onClose : ()=>{console.log("Dialoge Closed without any input")}
        });
    }

    //dialog of customer data show
    showCustomerInfoDialog(data){

        console.log("Show dialog called");
        const dialog = this.env.services.dialog;

        dialog.add(ConfirmationDialog, {
            title : `Hello ${data.name}`,
            body : `Customer Information : \n Name : ${data.name} \n Email : ${data.email}`,
            confirm : ()=>{this.showEffect(data.name)},
            cancel : ()=>{console.log("Dialog Cancelled");},
//            onClose : ()=>{console.log("Dialoge Closed without any input")}
        });
    }

    showEffect(name){
        const effect = this.env.services.effect;

        effect.add({
            type : "rainbow_man", //here men is wrong
            message : `Thanks ${name} for using us!!`,
        });
    }

//    callThroughHttp(){
//        const http = this.env.services.http;
//
//        console.log(http);
//    }

    async getDataORM(){
        const orm = this.env.services.orm;

        const record = this.props.record;
        const partnerData = record._values.partner_id;
        const partnerId = partnerData.id;

        console.log(partnerId);

        const data = await orm.searchRead("res.partner", [['id','=', partnerId]], ['name','email']);

        console.log("Customer Data is : ",data[0]);
        this.showCustomerInfoDialog(data[0]); //show the customer info on the dialog
    }

    getActionService(){
         const action = this.env.services.action;

         action.doAction({
            type : "ir.actions.act_window",
            name : "Action service",
            res_model : "res.partner",
            views : [
                [false, "form"],
                [false, "list"]
            ],
            view_mode : "list, form",
            target : "current"
         });
    }

    getTitle(){
        const title = this.env.services.title;
        console.log(title);
    }




}

CustomerInfo.template = "sale_order_inheritence.CustomButtonTemplate";
CustomerInfo.props = { ...standardWidgetProps };

registry.category("view_widgets").add("show_customer_info", {
    component: CustomerInfo,
});

