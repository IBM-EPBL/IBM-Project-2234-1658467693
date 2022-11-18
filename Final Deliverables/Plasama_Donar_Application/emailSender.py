
def successMail(reqDetails, data):
    if data != False:
        collect = ""
        for i in data:
            collect += ''' <div class="u-row-container" style="padding: 0px;background-color: transparent">
            <div class="u-row"
              style="Margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
              <div
                style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
                <div class="u-col u-col-100"
                  style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
                  <div
                    style="background-color: #c6e9ff;height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                    <div
                      style="height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                      <table id="u_content_text_11" style="font-family:'Open Sans',sans-serif;" role="presentation"
                        cellpadding="0" cellspacing="0" width="100%" border="0">
                        <tbody>
                          <tr>
                            <td class="v-container-padding-padding"
                              style="overflow-wrap:break-word;word-break:break-word;padding:22px;font-family:'Open Sans',sans-serif;"
                              align="left">
                              <div class="v-text-align v-line-height"
                                style="line-height: 140%; text-align: left; word-wrap: break-word;">
                                <p style="font-size: 14px; line-height: 140%;">Name: {name}</p>
                                <p style="font-size: 14px; line-height: 140%;">Contact number: {cnum}</p>
                                <p style="font-size: 14px; line-height: 140%;">Blood group: {Bgroup}</p>
                                <p style="font-size: 14px; line-height: 140%;">District: {dist}</p>
                                <p style="font-size: 14px; line-height: 140%;">City: {city}</p>
                              </div>
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div><br>'''.format(name=i['NAME'], cnum=i['PHNUM'], Bgroup=i['BLOOD'], dist=i['DISTRICT'], city=i['STATES'])

        SuccessTemplate = '''
                <!DOCTYPE HTML
        PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml"
        xmlns:o="urn:schemas-microsoft-com:office:office">

        <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="x-apple-disable-message-reformatting">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title></title>
        <style type="text/css">
            @media only screen and (min-width: 620px) {
            .u-row {
                width: 600px !important;
            }

            .u-row .u-col {
                vertical-align: top;
            }

            .u-row .u-col-100 {
                width: 600px !important;
            }
            }

            @media (max-width: 620px) {
            .u-row-container {
                max-width: 100% !important;
                padding-left: 0px !important;
                padding-right: 0px !important;
            }

            .u-row .u-col {
                min-width: 320px !important;
                max-width: 100% !important;
                display: block !important;
            }

            .u-row {
                width: calc(100% - 40px) !important;
            }

            .u-col {
                width: 100% !important;
            }

            .u-col>div {
                margin: 0 auto;
            }
            }

            body {
            margin: 0;
            padding: 0;
            }

            table,
            tr,
            td {
            vertical-align: top;
            border-collapse: collapse;
            }

            p {
            margin: 0;
            }

            .ie-container table,
            .mso-container table {
            table-layout: fixed;
            }

            * {
            line-height: inherit;
            }

            a[x-apple-data-detectors='true'] {
            color: inherit !important;
            text-decoration: none !important;
            }

            table,
            td {
            color: #000000;
            }

            @media (max-width: 480px) {
            #u_content_text_3 .v-container-padding-padding {
                padding: 10px !important;
            }

            #u_content_text_3 .v-line-height {
                line-height: 130% !important;
            }

            #u_content_text_11 .v-container-padding-padding {
                padding: 22px 22px 24px !important;
            }

            #u_content_text_11 .v-line-height {
                line-height: 140% !important;
            }

            #u_content_heading_4 .v-container-padding-padding {
                padding: 44px 10px 10px !important;
            }

            #u_content_heading_4 .v-font-size {
                font-size: 21px !important;
            }

            #u_content_image_4 .v-container-padding-padding {
                padding: 3px 0px 0px !important;
            }

            #u_content_image_4 .v-src-width {
                width: auto !important;
            }

            #u_content_image_4 .v-src-max-width {
                max-width: 100% !important;
            }

            #u_content_image_4 .v-text-align {
                text-align: center !important;
            }

            #u_content_heading_5 .v-container-padding-padding {
                padding: 22px 10px 10px !important;
            }

            #u_content_heading_5 .v-font-size {
                font-size: 21px !important;
            }
            }
        </style>
        <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700&display=swap" rel="stylesheet" type="text/css">
        <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700&display=swap" rel="stylesheet" type="text/css">
        </head>

        <body class="clean-body u_body"
        style="margin: 0;padding: 0;-webkit-text-size-adjust: 100%;background-color: #effafd;color: #000000">
        <table
            style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 320px;Margin: 0 auto;background-color: #effafd;width:100%"
            cellpadding="0" cellspacing="0">
            <tbody>
            <tr style="vertical-align: top">
                <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
                <div class="u-row-container" style="padding: 0px;background-color: transparent">
                    <div class="u-row"
                    style="Margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
                    <div
                        style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
                        <div class="u-col u-col-100"
                        style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
                        <div
                            style="background-color: #effafd;height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                            <div
                            style="height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                            <table style="font-family:'Open Sans',sans-serif;" role="presentation" cellpadding="0"
                                cellspacing="0" width="100%" border="0">
                                <tbody>
                                <tr>
                                    <td class="v-container-padding-padding"
                                    style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Open Sans',sans-serif;"
                                    align="left">
                                    <h1 class="v-text-align v-line-height v-font-size"
                                        style="margin: 0px; line-height: 140%; text-align: left; word-wrap: break-word; font-weight: normal; font-size: 22px;">
                                        Hi '''+reqDetails['Name']+''' </h1>
                                    </td>
                                </tr>
                                </tbody>
                            </table>
                            <table id="u_content_text_3" style="font-family:'Open Sans',sans-serif;" role="presentation"
                                cellpadding="0" cellspacing="0" width="100%" border="0">
                                <tbody>
                                <tr>
                                    <td class="v-container-padding-padding"
                                    style="overflow-wrap:break-word;word-break:break-word;padding:0px 45px 10px;font-family:'Open Sans',sans-serif;"
                                    align="left">
                                    <div class="v-text-align v-line-height"
                                        style="line-height: 140%; text-align: center; word-wrap: break-word;">
                                        <p style="font-size: 14px; line-height: 130%;"><span
                                            style="font-family: Montserrat, sans-serif; font-size: 16px; line-height: 20.8px;">
                                            <strong>We receive you request !</strong></span></p>
                                    </div>
                                    </td>
                                </tr>
                                </tbody>
                            </table>
                            <table style="font-family:'Open Sans',sans-serif;" role="presentation" cellpadding="0"
                                cellspacing="0" width="100%" border="0">
                                <tbody>
                                <tr>
                                    <td class="v-container-padding-padding"
                                    style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Open Sans',sans-serif;"
                                    align="left">
                                    <div class="v-text-align v-line-height"
                                        style="line-height: 140%; text-align: left; word-wrap: break-word;">
                                        <p style="font-size: 14px; line-height: 140%;">As per your request we found <span
                                            style="text-decoration: underline; font-size: 14px; line-height: 19.6px;"><strong>'''+reqDetails['bloodgrp']+'''</strong></span>
                                        Plasma donor availability in <strong>'''+reqDetails['State']+'''</strong> - <strong>'''+reqDetails['City']+'''</strong> </p>
                                    </div>
                                    </td>
                                </tr>
                                </tbody>
                            </table>
                            </div>
                        </div>
                        </div>
                    </div>
                    </div>
                </div>
                <div class="u-row-container" style="padding: 0px;background-color: transparent">
                    <div class="u-row"
                    style="Margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
                    <div
                        style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
                        <div class="u-col u-col-100"
                        style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
                        <div
                            style="height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                            <div
                            style="height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                            <table style="font-family:'Open Sans',sans-serif;" role="presentation" cellpadding="0"
                                cellspacing="0" width="100%" border="0">
                                <tbody>
                                <tr>
                                    <td class="v-container-padding-padding"
                                    style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Open Sans',sans-serif;"
                                    align="left">
                                    <div class="v-text-align v-line-height"
                                        style="line-height: 140%; text-align: left; word-wrap: break-word;">
                                        <p style="font-size: 14px; line-height: 140%;">Total available donor(s): '''+str(len(data))+'''</p>
                                    </div>
                                    </td>
                                </tr>
                                </tbody>
                            </table>
                            </div>
                        </div>
                        </div>
                    </div>
                    </div>
                </div>'''+collect+'''
                </td>
            </tr>
            </tbody>
        </table>
        </body>

        </html>'''
    
    return SuccessTemplate
