require('./utils.js');
import 'bootstrap';
import feather from 'feather-icons';
import 'intl-tel-input';
import LookupForm from './LookupForm';
import LookupResults from './LookupResults';
import './styles.scss';

$(() => {
    feather.replace();

    let lookupResults = new LookupResults();
    new LookupForm(lookupResults);
});