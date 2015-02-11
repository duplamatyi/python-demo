namespace('PythonDemo.Hotel', {
    config: {},
    Index:{
        suggestionTemplate: '<a data-id="<%= pk %>" href="javascript:void(0)"><%= fields.name %></a>',
        hotelTemplate: '<li class="hotel-list-item" data-id="<%= pk %>"><%= fields.name %></li>',
        init: function(conf) {
            // constructs the suggestion engine
            var that = this,
                hotelContainer = $('#hotel-container'),
                hotelList = hotelContainer.find('#hotel-list'),
                hotelListTitle = hotelContainer.find('#hotel-list-title'),
                hotelListErrors = hotelContainer.find('#hotel-list-errors'),
                cities = new Bloodhound({
                datumTokenizer: Bloodhound.tokenizers.obj.whitespace('value'),
                queryTokenizer: Bloodhound.tokenizers.whitespace,
                remote: {
                    url: Django.url('city') + '?q=%QUERY'
                }
            });

            // kicks off the loading/processing of `local` and `prefetch`
            cities.initialize();

            $('#city-typeahead').typeahead({
                    hint: true,
                    highlight: true,
                    minLength: 1
                },
                {
                    name: 'fields',
                    display: function(obj) {
                        return obj.fields.name;
                    },
                    // `ttAdapter` wraps the suggestion engine in an adapter that
                    // is compatible with the typeahead jQuery plugin
                    source: cities.ttAdapter(),
                    templates: {
                        'empty': '<div class="empty-message">No cities found...</div>',
                        'suggestion': _.template(that.suggestionTemplate),
                        'header': '<h3 class="typeahead-title">Cities</h3>'
                    }
                }
            ).on('typeahead:selected', function($event, suggestion, dataset) {
                $.getJSON( Django.url('hotel', suggestion.pk), function(data) {
                    var hotelTemplate = _.template(that.hotelTemplate);

                    hotelListTitle.text('The following hotels could be found:');
                    if (0 < data.length) {
                        $.each( data, function( i, item ) {
                            hotelList.append(hotelTemplate(item));
                        });

                    } else {
                        hotelListErrors.text('Could not find any hotel.');
                    }
                }).fail(function() {
                    hotelListErrors.text('Failed listing the hotels. Please select a city again.');
                });
            }).on('typeahead:opened', function($event, suggestion, dataset) {
                    hotelListErrors.empty();
                    hotelListTitle.empty();
                    hotelList.empty();
            });
        }
    }
});
