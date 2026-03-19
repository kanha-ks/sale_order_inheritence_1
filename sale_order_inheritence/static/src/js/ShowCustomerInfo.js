/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { FormController } from "@web/views/form/form_controller";
import { useExternalListener } from "@odoo/owl";

patch(FormController.prototype, {
    setup() {
//        debugger;
        super.setup(...arguments);
        console.log("setup of ShowCustomer Info is loaded");


//        useExternalListener(window, "click", (ev) => {
//            const btn = ev.target.closest(".customer_info_btn");
//            if (btn) {
//                this.myCustomClickLogic(ev);
//            }
//        });
    },

   onClick(ev) {
     console.log("Onclick worked");
//        debugger;
        const isMyButton = ev.target.closest(".customer_info_btn");

        if (isMyButton) {
            console.log("Customer Info Button Clicked");
        }

        console.log("Onclick works");
         return super.onClick(ev);
    }


//    myCustomClickLogic(ev) {
//        console.log("BINGO! Button Clickeddd");
//        const record = this.model.root.data;
//        alert("Sale Order: " + record.display_name);
//    }
});
















//    /** @odoo-module **/




//    import { patch } from "@web/core/utils/patch";
//    import { FormController } from "@web/views/form/form_controller";
//    import { useService } from "@web/core/utils/hooks";
//
//    patch(FormController.prototype, {
//        setup() {
//            super.setup(...arguments);
//            this.notification = useService("notification");
//            this.rpc = useService("rpc");
//            console.log("JS Loaded: Form Controller Patched Successfully");
//        },
//
//         async onClick(ev) {
//            console.log("Onclick function inside controller called!!")
//            // Check if our specific button was clicked
//    //        if (ev.target.classList.contains("customer_info_btn")) {
//    //            console.log("Button Clicked!");
//    //
//    //            const orderId = this.model.root.resId;
//    //            const orderName = this.model.root.data.display_name;
//    //
//    //            if (!orderId) {
//    //                this.notification.add("Please save the record first.", { type: "danger" });
//    //                return;
//    //            }
//    //
//    //            try {
//    //                const result = await this.rpc("/web/dataset/call_kw/sale.order/get_order_details_rpc", {
//    //                    model: "sale.order",
//    //                    method: "get_order_details_rpc",
//    //                    args: [orderId],
//    //                    kwargs: {},
//    //                });
//    //
//    //                this.notification.add(`Info: ${result}`, {
//    //                    title: orderName,
//    //                    type: "success",
//    //                });
//    //            } catch (error) {
//    //                console.error("RPC Error:", error);
//    //            }
//            }
//            return super.onClick(ev);
////            return "Hello";
//        },
//    });









    ///** @odoo-module **/
    //import { registry } from "@web/core/registry";
    //import { rpc } from "@web/core/network/rpc";
    //
    //class ShowCustomerInfo extends Component {
    //
    //
    //       setup(){
    //            console.log("This showCustomerInfo is called")
    //       }
    ////    static components = {  };
    //    static template = "sale.ShowCustomerInfo";
    ////    onClick() {
    ////            this.showNotification(info);
    ////    }
    //
    //    onClickCustomerInfo() {
    //        console.log("Customer Info is Null")
    //    }
    //}
    //
    //
    //ExpressionWidget.template = "sale_order_inheritence.ShowCustomerInfo";
    //
    //registry.category("views").add("customer_info", {
    //    component: ShowCustomerInfo,
    //});
    //
    //
    //
    //
    //
    //
    //
    //
    //
    //
    //
    //
    //
    //
    //
    //
    //
    //
    //
    //
    //
    //
    //
    ////ExpressionWidget.props = {
    ////    ...standardFieldProps,
    ////};
    ////
    ////registry.category("fields").add("expression", {
    ////    component: ExpressionWidget,
    ////});
    //
    ////registry.category("views").add("js_check_custom", {
    ////    ...formView,
    ////    component: ShowCustomerInfo,
    ////});
    //
    //
    //// Register the component to make it usable
    //
    ////
    ////registry.category('actions').add('sale.ShowCustomerInfo', ShowCustomerInfo);
    //
    ////
    /////** @odoo-module **/
    ////
    ////import { formView } from "@web/views/form/form_view";
    ////import { FormController } from "@web/views/form/form_controller";
    ////import { registry } from "@web/core/registry";
    ////
    ////export class CustomerInfoController extends FormController {
    ////    async onClickCustomerInfo() {
    ////        console.log("Button Clicked!");
    ////        this.env.services.notification.add("Customer Info Checked!", {
    ////            type: "success",
    ////        });
    ////    }
    ////}
