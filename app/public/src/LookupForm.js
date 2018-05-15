const validationErrorCodes = {
    0: 'Invalid number',
    1: 'Invalid country code',
    2: 'Number is too short.',
    3: 'Number is too long.',
    4: 'Phone number incorrect.'
};

export default class {

    constructor(lookupResults) {
        this._resetValidation();
        this.lookupResults = lookupResults;

        $('.lookup-input').each((i, element) => {
            $(element).intlTelInput();
        });
        $("#lookupForm").submit(event => this._onSubmit(event));
    }

    _onSubmit(e) {
        this._startLoading();
        this._resetValidation();
        let numbers = [];

        $(".lookup-input").each((index, element) => {
            if ($(element).val() != '') {
                this._validate(element);
                numbers.push($(element).intlTelInput("getNumber"));
            }
        });

        if (!this.isValid) {
            this._stopLoading();
            return false;
        }

        if (numbers.length == 0) {
            this._stopLoading();
            return false;
        }

        this._request(numbers);

        return false;
    }

    _request(numbers) {
        $.ajax({
            url: '/',
            method: 'post',
            contentType: "application/json",
            data: JSON.stringify({phone_numbers: numbers}),
            success: (result) => this._onSuccess(result),
            complete: () => {
                this._stopLoading();
            }
        });
    }

    _onSuccess(results) {
        this.lookupResults.addResults(results);
    }

    _startLoading() {
        $('.lookup-input').attr('disabled', 'disabled');
        $('#lookupSubmitButton').attr('disabled', 'disabled');
        this.lookupResults.startLoading();
    }

    _stopLoading() {
        $('.lookup-input').removeAttr('disabled');
        $('#lookupSubmitButton').removeAttr('disabled');
        this.lookupResults.stopLoading();
    }

    _resetValidation() {
        this.isValid = true;
        $(".invalid-feedback").hide();
        $(".lookup-input").removeClass('is-invalid');
    }

    _validate(element) {
        let $element = $(element);

        if (!$element.intlTelInput("isValidNumber")) {
            $element.addClass('is-invalid');
            $element.parent().next().html(this._getValidationError($element.intlTelInput("getValidationError"))).show();
            this.isValid = false;
        }
    }

    _getValidationError(errorCode) {
        if (errorCode in validationErrorCodes) {
            return validationErrorCodes[errorCode]
        }
        return "Invalid number.";
    }
}