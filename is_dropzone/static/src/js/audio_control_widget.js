odoo.define('is_dropzone.AudioWidget', function (require) {
    "use strict";

    var AbstractField = require('web.AbstractField');
    var fieldRegistry = require('web.field_registry');
    var core = require('web.core');

    var AudioWidget = AbstractField.extend({
        className: 'o_field_audio',

        supportedFieldTypes: ['char'],

        _renderReadonly: function () {
            var validExtensions = ['mp3', 'ogg', 'wav'];
            var fileExtension = this.value.split('.').pop();
            if (validExtensions.includes(fileExtension)) {
//                render(this.template, {'audioSrc': this.valu})
                var html = `<audio controls>
                                <source src="${this.value}" type="audio/mpeg">
                                <source src="${this.value}" type="audio/ogg">
                                <source src="${this.value}" type="audio/wav">
                                This is not an audio file
                            </audio>`;
                this.$el.html(html);
            } else {
                this.$el.empty();
            }
        },
    });

    fieldRegistry.add('audio', AudioWidget);

    return {
        AudioWidget: AudioWidget,
    };
});
