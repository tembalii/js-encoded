import logging

from flask import request, jsonify
from flask.views import MethodView

from app import config as cfg
from app.models.v2 import keypad_protocol, mappings

logger = logging.getLogger(cfg.HANDLER_NAME)


class PartialSearch(MethodView):
    keypad_protocol_model = keypad_protocol.KeypadProtocolControllerImpl(
        keypad_protocol_table=keypad_protocol.KeypadProtocolTable)

    def get(self):
        search_string = request.args.get('search_string', '')
        search_column = request.args.get('column', None)
        output_columns = request.args.getlist('output_column')
        logger.debug(search_string)

        if not search_column:
            return jsonify({'message': f'Bad Request. Missing parameter `column`'}), 400

        column = mappings.KEYPAD_PROTOCOL_COLUMN_MAP.get(search_column)
        output_columns_parsed = [mappings.KEYPAD_PROTOCOL_COLUMN_MAP.get(itr) for itr in output_columns]

        db_res = self.keypad_protocol_model.get_by_partial_name(search_string,
                                                                column,
                                                                *output_columns_parsed
                                                                )

        response_list = []
        for res in db_res:
            out_res = {search_column: getattr(res, search_column)}
            for col in output_columns:
                out_res[col] = getattr(res, col)

            response_list.append(out_res)

        return jsonify({'keypad_protocol': response_list}), 200
