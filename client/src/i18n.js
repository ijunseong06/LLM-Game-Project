import { createI18n } from "vue-i18n";
import ko from '@/locales/ko.json';
import en from '@/locales/en.json';

const messages = {
    ko,
    en
}

const i18n = createI18n({
    locale: 'ko',
    fallbackLocale: 'en',
    messages: messages,
});

export default i18n;