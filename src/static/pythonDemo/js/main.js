namespace = function(identifier) {
    var classes = arguments[1] || false;
    var ns = window;

    if (identifier !== '') {
        var parts = identifier.split('.');
        for (var i = 0; i < parts.length; i++) {
            if (!ns[parts[i]]) {
                ns[parts[i]] = {};
            }
            ns = ns[parts[i]];
        }
    }

    if (classes) {
        for (var _class in classes) {
            if (classes.hasOwnProperty(_class)) {
                ns[_class] = classes[_class];
            }
        }
    }

    return ns;
};