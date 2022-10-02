odoo.define("pos_snapshot_button.CustomDemoButtons", function (require) {
  "use strict";
  const PosComponent = require('point_of_sale.PosComponent');
  const ProductScreen = require('point_of_sale.ProductScreen');
  const { useListener } = require('web.custom_hooks');
  const Registries = require('point_of_sale.Registries');
  const { Gui } = require('point_of_sale.Gui');


  class CustomDemoButtons extends PosComponent {
    constructor() {
        super(...arguments);
        useListener('click', this.onClick);
    }
  }

  CustomDemoButtons.template = 'CustomDemoButtons';

  ProductScreen.addControlButton({
    component: CustomDemoButtons,
    condition: function() {
        return this.env.pos;
    },
  });
  Registries.Component.add(CustomDemoButtons);
    return CustomDemoButtons;
});
