odoo.define('dairy.web_form', function (require) {
'use strict';

var publicWidget = require('web.public.widget');

publicWidget.registry.DairyForm = publicWidget.Widget.extend({
    selector: '.dairy_seller',
    events: _.extend({}, publicWidget.Widget.events || {}, {
        'change select[name="country_id"]': '_onChangeCountry',
    }),

     /**
     * @constructors
     */
    init: function () {
        this._super.apply(this, arguments);

        this._changeCountry = _.debounce(this._changeCountry.bind(this), 50);

        this.isWebsite = true;
    },
    /**
     * @private
     */

    _changeCountry: function () {
        var country_id = this.$el.find("#country_id").val();
        if (!country_id) {
            return;
        }

        this._rpc({
            route: "/dairy/country_infos/" + country_id,
        }).then(function (data) {

//            console.log("======= Data =====", data);
            // populate states and display
//            debugger;
            var selectStates = $("select[name='state_id']");
//            console.log("===========", selectStates);

            // dont reload state at first loading (done in qweb)
            if (selectStates.data('init')===0 || selectStates.find('option').length===1) {
                if (data.states.length || data.state_required) {
                    selectStates.html('');
                    _.each(data.states, function (x) {
                        var opt = $('<option>').text(x[1])
                            .attr('value', x[0])
                            .attr('data-code', x[2]);
                        selectStates.append(opt);
                    });
                    selectStates.parent('div').show();
                }else {
                    selectStates.val('').parent('div').hide();
                    }
                    selectStates.data('init', 0);
            }else {
                    selectStates.data('init', 0);
                }
            });
        },


    _onChangeCountry: function (ev) {
        if (!this.$el.find('.o_country').length) {
            return;
        }
        this._changeCountry();
    },
});
})
