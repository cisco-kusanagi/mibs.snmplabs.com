#
# PySNMP MIB module TPT-TANK-NOTIFY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPT-TANK-NOTIFY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:26:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Counter32, ObjectIdentity, IpAddress, Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity, iso, NotificationType, Gauge32, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "ObjectIdentity", "IpAddress", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity", "iso", "NotificationType", "Gauge32", "Unsigned32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tptMiscNotifyDeviceID, = mibBuilder.importSymbols("TPT-MISC-NOTIFY-MIB", "tptMiscNotifyDeviceID")
tpt_tpa_eventsV2, tpt_tpa_unkparams, tpt_tpa_objs = mibBuilder.importSymbols("TPT-TPAMIBS-MIB", "tpt-tpa-eventsV2", "tpt-tpa-unkparams", "tpt-tpa-objs")
tpt_tank_notify = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 11)).setLabel("tpt-tank-notify")
tpt_tank_notify.setRevisions(('2016-05-25 18:54',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tpt_tank_notify.setRevisionsDescriptions(('Updated copyright information. Minor MIB syntax fixes.',))
if mibBuilder.loadTexts: tpt_tank_notify.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tpt_tank_notify.setOrganization('Trend Micro, Inc.')
if mibBuilder.loadTexts: tpt_tank_notify.setContactInfo('www.trendmicro.com')
if mibBuilder.loadTexts: tpt_tank_notify.setDescription("Notification definitions for X-Series. Copyright (C) 2016 Trend Micro Incorporated. All Rights Reserved. Trend Micro makes no warranty of any kind with regard to this material, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose. Trend Micro shall not be liable for errors contained herein or for incidental or consequential damages in connection with the furnishing, performance, or use of this material. This document contains proprietary information, which is protected by copyright. No part of this document may be photocopied, reproduced, or translated into another language without the prior written consent of Trend Micro. The information is provided 'as is' without warranty of any kind and is subject to change without notice. The only warranties for Trend Micro products and services are set forth in the express warranty statements accompanying such products and services. Nothing herein should be construed as constituting an additional warranty. Trend Micro shall not be liable for technical or editorial errors or omissions contained herein. TippingPoint(R), the TippingPoint logo, and Digital Vaccine(R) are registered trademarks of Trend Micro. All other company and product names may be trademarks of their respective holders. All rights reserved. This document contains confidential information, trade secrets or both, which are the property of Trend Micro. No part of this documentation may be reproduced in any form or by any means or used to make any derivative work (such as translation, transformation, or adaptation) without written permission from Trend Micro or one of its subsidiaries. All other company and product names may be trademarks of their respective holders. ")
class ExternalVIStatus(TextualConvention, Integer32):
    description = 'An indication of whether external virtual interface is up or down.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class WebFilterStatus(TextualConvention, Integer32):
    description = 'An indication of the web filtering status.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("uninitialized", 1), ("success", 2), ("timeout", 3), ("failure", 4))

tptTankNotifyExternalVIStatus = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 151), ExternalVIStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptTankNotifyExternalVIStatus.setStatus('current')
if mibBuilder.loadTexts: tptTankNotifyExternalVIStatus.setDescription('Whether the external virtual interface is up or down.')
tptTankNotifyWebFilterStatus = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 152), WebFilterStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptTankNotifyWebFilterStatus.setStatus('current')
if mibBuilder.loadTexts: tptTankNotifyWebFilterStatus.setDescription('Status of web filtering status.')
tptTankNotifyExternalVI = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 22)).setObjects(("TPT-MISC-NOTIFY-MIB", "tptMiscNotifyDeviceID"), ("TPT-TANK-NOTIFY-MIB", "tptTankNotifyExternalVIStatus"))
if mibBuilder.loadTexts: tptTankNotifyExternalVI.setStatus('current')
if mibBuilder.loadTexts: tptTankNotifyExternalVI.setDescription('Notification: Used to inform the management station that external virtual interface came up or went down.')
tptTankNotifyWebFilter = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 23)).setObjects(("TPT-MISC-NOTIFY-MIB", "tptMiscNotifyDeviceID"), ("TPT-TANK-NOTIFY-MIB", "tptTankNotifyWebFilterStatus"))
if mibBuilder.loadTexts: tptTankNotifyWebFilter.setStatus('current')
if mibBuilder.loadTexts: tptTankNotifyWebFilter.setDescription('Notification: Used to inform the management station of the web filtering status.')
mibBuilder.exportSymbols("TPT-TANK-NOTIFY-MIB", PYSNMP_MODULE_ID=tpt_tank_notify, tptTankNotifyWebFilterStatus=tptTankNotifyWebFilterStatus, tptTankNotifyExternalVI=tptTankNotifyExternalVI, tptTankNotifyWebFilter=tptTankNotifyWebFilter, ExternalVIStatus=ExternalVIStatus, tpt_tank_notify=tpt_tank_notify, tptTankNotifyExternalVIStatus=tptTankNotifyExternalVIStatus, WebFilterStatus=WebFilterStatus)
