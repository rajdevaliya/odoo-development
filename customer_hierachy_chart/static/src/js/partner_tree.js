odoo.define('customer_hierachy_chart.partner_tree', function (require) {
    "use strict";

    var core = require('web.core');
    var _t = core._t;
    var ListView = require('web.ListView');

    ListView.include({
        render_buttons: function () {
            this._super.apply(this, arguments);
            if (this.$buttons) {
                var $toggleChildIdsButton = $('<button/>', {
                    type: 'button',
                    class: 'btn btn-default',
                    text: _t('Toggle Child IDs'),
                }).on('click', this.proxy('toggleChildIds'));
                this.$buttons.append($toggleChildIdsButton);
            }
        },

        toggleChildIds: function () {
            var $companyField = this.$('.o_list_view .o_data_cell.o_list_number[name="company_id"]');
            var $childIds = this.$('.o_list_view tr.o_data_row[data-id]:not(.o_group_header)').not($companyField.closest('tr'));
            if ($childIds.length) {
                if ($companyField.data('child-ids-visible')) {
                    $companyField.data('child-ids-visible', false).css('font-weight', 'normal');
                    $childIds.hide();
                } else {
                    $companyField.data('child-ids-visible', true).css('font-weight', 'bold');
                    $childIds.show();
                }
            }
        },
    });
});
