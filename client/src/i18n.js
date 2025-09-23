import Vue from "vue";
import VueI18n from "vue-i18n";

Vue.use(VueI18n)

function loadMessages() {
    const context = require.context('@/locales', true, /\.json$/)
}
const options = {
    locale: 'ko',
    fallbackLocale: 'en',
    messages,
};

export default new VueI18n(options);