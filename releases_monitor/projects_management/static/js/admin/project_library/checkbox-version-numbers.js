/* checkbox-version-number.js will check-uncheck mayor/minor/patch checkboxs
  Example:
  - If patch number must be checked, it is mandatory to check also mayor and minor number
  - If mayor number is not checked, minor and patch numbers can't be checked
*/

(function ($) {
  $(document).ready(function () {
    /* When MAYOR update is unchecked:
      - Minor and Patch must be also unchecked
    */
    $('input#id_check_mayor_version_update').change(function () {
      if (!this.checked) {
        $('input#id_check_minor_version_update').prop('checked', false)
        $('input#id_check_patch_version_update').prop('checked', false)
      }
    })

    /*
      When MINOR update is checked:
        - Mayor must be also checked
      When MINOR update is unchecked:
        - Minor must be also unchecked
    */
    $('input#id_check_minor_version_update').change(function () {
      if (this.checked) {
        $('input#id_check_mayor_version_update').prop('checked', true)
      } else {
        $('input#id_check_patch_version_update').prop('checked', false)
      }
    })

    /*
      When PATCH update is checked:
        - Mayor and Minor must be also checked
    */
    $('input#id_check_patch_version_update').change(function () {
      if (this.checked) {
        $('input#id_check_mayor_version_update').prop('checked', true)
        $('input#id_check_minor_version_update').prop('checked', true)
      }
    })
  })
}(django.jQuery))
