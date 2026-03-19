/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

class SaleOrderPopup extends Component {
    setup() {
        this.notification = useService("notification");
    }

    mounted() {
        const params = this.props.action.params;

        this.notification.add(
            `Order: ${params.order_name}, Customer: ${params.partner}, Total: ${params.amount}`,
            { type: "info" }
        );
    }
}

registry.category("actions").add("sale_order_js_action", SaleOrderPopup);