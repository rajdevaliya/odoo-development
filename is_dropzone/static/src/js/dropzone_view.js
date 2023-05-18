/** @odoo-module **/

import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

const { Component } = owl;
const { useRef, useState } = owl.hooks;

class FilesDropzone extends Component {
    setup() {
        this.action = useService("action");
        this.id = 0;
        this.csrf_token = useState('');
        this.rpc = useService("rpc");
        this.dT = new DataTransfer();
        this.FileList = useState([]);
        this.file_objs = [];
        this.isDraggingInside = useState({ value: true, hide: false, background: '' });
         this.allowedTypes = [
            'text/plain',
            'application/msword',
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            'application/pdf',
            'application/rtf',
            'application/vnd.oasis.opendocument.text',
            'image/jpeg',
            'image/png',
            'image/gif',
            'image/bmp',
            'image/svg+xml',
            'audio/mpeg',
            'audio/wav',
            'audio/ogg',
            'audio/flac',
            'audio/aac',
            'video/mp4'
          ];

    }
    removeFile(id) {
//        ev.preventDefault()
//        ev.stopPropagation()
        var list_id = id //parseInt(ev.target.id)
        var fileIndex1 = this.FileList.findIndex((todo) => todo.id === list_id);
        var fileIndex2 = this.file_objs.findIndex((todo) => todo.id === list_id);
        if (fileIndex1 >= 0) {
            this.FileList.splice(fileIndex1, 1);
            this.file_objs.splice(fileIndex2, 1);
        }
        if(this.FileList.length === 0) {
            this.isDraggingInside.hide = false;
            this.id = 0;
        }
        console.log(id);
    }
    submitForm(ev) {
        ev.preventDefault()
        this.isDraggingInside.hide = false;
        this.isDraggingInside.value = false;
        for(var file of this.file_objs) {this.dT.items.add(file.obj);}
        var fileForm = document.getElementById("dropzone-form");
        var inpFile = document.getElementById("formFileMultiple");
        inpFile.files = this.dT.files;
        fileForm.submit();
        fileForm.reset();
        this.dT.clearData();
        this.FileList.length = 0;
        this.csrf_token = '';

    }
    onDragenter (ev){
        ev.preventDefault();
        this.isDraggingInside.background = 'background-color: lightblue;';
    }
    onDragleave(ev){
        ev.preventDefault();
        this.isDraggingInside.background = '';
    }
    onDragover(ev){
        ev.preventDefault();
        this.isDraggingInside.background = 'background-color: lightblue;';
    }
    onDrop (ev) {
        this.isDraggingInside.background = '';
        ev.preventDefault();
        var files = ev.dataTransfer.files;
        if (files.length > 0) {
            this.csrf_token = odoo.csrf_token;
            this.isDraggingInside.hide = true;
            var inpFile = document.getElementById("formFileMultiple");
            for (var i = 0; i < files.length; i++) {
                if (this.isFileTypeAllowed(files[i].type)) {
                    if (!this.FileList.includes(files[i].name)) {
                        var obj_id = this.id++
                        this.FileList.push({id: obj_id, name: files[i].name});
                        this.file_objs.push({id: obj_id, obj: files[i]});
                    }
                }
            }
        }
    }
    isFileTypeAllowed(fileType) {
        return this.allowedTypes.includes(fileType);
    }
}

FilesDropzone.template = "is_dropzone.FileDropArea";

registry.category("actions").add("dropzone_board", FilesDropzone);
