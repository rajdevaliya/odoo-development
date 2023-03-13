odoo.define('is_website_purchase_modified.PurchasePortalSidebarAction', function (require) {
    'use strict';
    
    console.log("Receipt date js run");
    const time = require('web.time');
    const publicWidget = require('web.public.widget');
    const core = require('web.core');
    const QWeb = core.qweb;
    // const rpc = require('web.rpc');
    console.log("New Receipt date js run");
    
    
    publicWidget.registry.websiteChangeDate = publicWidget.Widget.extend({
        selector: '.o_portal_purchase_sidebar',
        xmlDependencies: ['/is_website_purchase_modified/static/xml/purchase_date_change.xml'],
        events: {
            'click .o_calendar_btn': '_onClick',
        },
        _onClick: function (ev) {
            if (!this.$createModal) {
                console.log($("#raj"));
                console.log("this", this);
                console.log(time.getLangDatetimeFormat());
                console.log("ev", ev);
                debugger;
                // var self = this;
                var poId = $(ev.currentTarget).data('po-id');
                var access_token = $(ev.currentTarget).data('access');
                var poDate = $(ev.currentTarget).data('po-date');

                

                this.$createModal = $(QWeb.render(
                    'frontend_po_date_change',
                    {
                        csrf_token: odoo.csrf_token,
                        order_id : poId,
                        receiptDate: poDate,
                        access_token : access_token,

                    }
                ));
                this.$createModal.appendTo(this.$el.parentNode);
                // $('#datetimepickerID').datetimepicker({format : 'DD/MM/YYYY HH:mm:ss');
            }
            
            this.$createModal.modal('show');
            $('#raj').datetimepicker({
                calendarWeeks: true,
                icons : {
                    time: 'fa fa-clock-o',
                    date: 'fa fa-calendar',
                    next: 'fa fa-chevron-right',
                    previous: 'fa fa-chevron-left',
                    up: 'fa fa-chevron-up',
                    down: 'fa fa-chevron-down',
                },
                locale : moment.locale(),
                format : time.getLangDatetimeFormat(),
                widgetPositioning : {
                    horizontal: 'auto',
                    vertical: 'top',
                },
                widgetParent: 'body',
                allowInputToggle: true,
            });
            
        },
        destroy: function(){
            debugger;
            var res = this._super.apply(this, arguments);
            console.log('destroy worked')
            $('#abc').click(function(){
                $('.raj_change_date').remove();
            });
            return res
        },
    });
    return publicWidget.registry.websiteChangeDate;
});




// odoo.define('calendar_demo.calendar.systray.ActivityMenu', function (require) {
//     "use strict";
//     console.log('am here');
//     var core = require('web.core');
//     var session = require('web.session');
//     var SystrayMenu = require('web.SystrayMenu');
//     var Widget = require('web.Widget');
//     var QWeb = core.qweb;
//     const { DatePicker, DateTimePicker } = require('web.DatePickerOwl');
//     console.log('DatePicker', DatePicker);
//     var Datepicker = require('web.datepicker');
//     console.log('datepicker', Datepicker);
//     const { Component } = owl;
//     var CalendarMenu = Widget.extend({
//         name: 'calendar_menu',
//         template: 'calendar_demo.calendar.systray.ActivityMenu',


//         start: function () {
//             this._$calendarPreview = this.$('.o_calendar_systray_dropdown_items');
//             console.log('inside start function');
//             var self = this;
//             // self._$calendarPreview.html(QWeb.render('web.datepicker', {// When i use this line ith shows input textbox only
//             self._$calendarPreview.html(QWeb.render('calendar_demo.calendar.systray.ActivityMenu.Calendar', {// When i use this line its show balnk area
//                 widget: self
//             }));
//             return this._super();
//         },
//     });
//     console.log('CalendarMenu', CalendarMenu);
//     SystrayMenu.Items.push(CalendarMenu);


//     return CalendarMenu

//     //The below code not executing
//     Datepicker.include({
//         // console.log();
//         // console.log('inside datepicker funciton');
//         _onInputClicked: function () {
//             console.log('_onInputClicked------------');
//             this._super();
//         },
//     });

// });

// odoo.define('is_website_purchase_modified.PurchasePortalSidebarAction', function (require) {
//     'use strict';
    
//     var rpc = require('web.rpc');
//     console.log(rpc);
    
//     $(document).on('click', '#calendar_button', function(){
    
//         console.log("test");
//         console.log('Calendar View');
    
    
//      });
//     });