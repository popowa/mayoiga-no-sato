<script>
jQuery(document).ready(function($) {
    $.fn.tagcloud.defaults = {
        size: {start: 9, end: 25, unit: 'pt'},
        color: {start: '#5c9291', end: '#1f3134'}
    };

    $(function () {
      $('#tagcloud a').tagcloud();
    });
});
</script>
