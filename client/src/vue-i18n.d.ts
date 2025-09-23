import { I18n } from 'vue-i18n';

declare module '@vue/runtime-core' {
  interface ComponentCustomProperties {
    $t: typeof I18n['global']['t'];
    $tc: typeof I18n['global']['tc'];
    $te: typeof I18n['global']['te'];
    $d: typeof I18n['global']['d'];
    $n: typeof I18n['global']['n'];
    $i18n: typeof I18n;
  }
}