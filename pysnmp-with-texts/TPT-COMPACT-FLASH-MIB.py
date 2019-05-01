#
# PySNMP MIB module TPT-COMPACT-FLASH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPT-COMPACT-FLASH-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:26:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Bits, ObjectIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32, Counter64, NotificationType, ModuleIdentity, Integer32, IpAddress, MibIdentifier, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "ObjectIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32", "Counter64", "NotificationType", "ModuleIdentity", "Integer32", "IpAddress", "MibIdentifier", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tpt_tpa_eventsV2, tpt_tpa_unkparams, tpt_tpa_objs = mibBuilder.importSymbols("TPT-TPAMIBS-MIB", "tpt-tpa-eventsV2", "tpt-tpa-unkparams", "tpt-tpa-objs")
tpt_compact_flash = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 14)).setLabel("tpt-compact-flash")
tpt_compact_flash.setRevisions(('2016-05-25 18:54',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tpt_compact_flash.setRevisionsDescriptions(('Updated copyright information. Minor MIB syntax fixes.',))
if mibBuilder.loadTexts: tpt_compact_flash.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tpt_compact_flash.setOrganization('Trend Micro, Inc.')
if mibBuilder.loadTexts: tpt_compact_flash.setContactInfo('www.trendmicro.com')
if mibBuilder.loadTexts: tpt_compact_flash.setDescription("Compact flash details on the device. Copyright (C) 2016 Trend Micro Incorporated. All Rights Reserved. Trend Micro makes no warranty of any kind with regard to this material, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose. Trend Micro shall not be liable for errors contained herein or for incidental or consequential damages in connection with the furnishing, performance, or use of this material. This document contains proprietary information, which is protected by copyright. No part of this document may be photocopied, reproduced, or translated into another language without the prior written consent of Trend Micro. The information is provided 'as is' without warranty of any kind and is subject to change without notice. The only warranties for Trend Micro products and services are set forth in the express warranty statements accompanying such products and services. Nothing herein should be construed as constituting an additional warranty. Trend Micro shall not be liable for technical or editorial errors or omissions contained herein. TippingPoint(R), the TippingPoint logo, and Digital Vaccine(R) are registered trademarks of Trend Micro. All other company and product names may be trademarks of their respective holders. All rights reserved. This document contains confidential information, trade secrets or both, which are the property of Trend Micro. No part of this documentation may be reproduced in any form or by any means or used to make any derivative work (such as translation, transformation, or adaptation) without written permission from Trend Micro or one of its subsidiaries. All other company and product names may be trademarks of their respective holders. ")
class MountedOrNot(TextualConvention, Integer32):
    description = 'An indication of compact flash mount status - mounted or unmounted.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("mounted", 0), ("unmounted", 1))

class OperationMode(TextualConvention, Integer32):
    description = 'An indication of compact flash operation mode - auto-mount or secure.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("secure", 0), ("auto-mount", 1))

class FormattedOrNot(TextualConvention, Integer32):
    description = 'An indication of compact flash format status - formatted or not.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("formatted", 0), ("unformatted", 1))

class PresentOrNot(TextualConvention, Integer32):
    description = 'An indication of compact flash presence - present or not.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("present", 0), ("absent", 1))

compactFlashPresent = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 14, 1), PresentOrNot()).setMaxAccess("readonly")
if mibBuilder.loadTexts: compactFlashPresent.setStatus('current')
if mibBuilder.loadTexts: compactFlashPresent.setDescription('Compact flash presence')
compactFlashMounted = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 14, 2), MountedOrNot()).setMaxAccess("readonly")
if mibBuilder.loadTexts: compactFlashMounted.setStatus('current')
if mibBuilder.loadTexts: compactFlashMounted.setDescription('Compact flash mount status')
compactFlashFormatted = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 14, 3), FormattedOrNot()).setMaxAccess("readonly")
if mibBuilder.loadTexts: compactFlashFormatted.setStatus('current')
if mibBuilder.loadTexts: compactFlashFormatted.setDescription('Compact flash format status')
compactFlashOperationMode = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 14, 4), OperationMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: compactFlashOperationMode.setStatus('current')
if mibBuilder.loadTexts: compactFlashOperationMode.setDescription('Compact flash operation mode')
vendorInformation = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 14, 5))
if mibBuilder.loadTexts: vendorInformation.setStatus('current')
if mibBuilder.loadTexts: vendorInformation.setDescription('Sub-tree of compact flash details')
serialNumber = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 14, 5, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialNumber.setStatus('current')
if mibBuilder.loadTexts: serialNumber.setDescription('Serial number')
model = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 14, 5, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: model.setStatus('current')
if mibBuilder.loadTexts: model.setDescription('Model Name.')
capacity = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 14, 5, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capacity.setStatus('current')
if mibBuilder.loadTexts: capacity.setDescription('Capacity ')
revision = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 14, 5, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: revision.setStatus('current')
if mibBuilder.loadTexts: revision.setDescription('Firmware revision')
tptCompactFlashDeviceID = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 261), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptCompactFlashDeviceID.setStatus('current')
if mibBuilder.loadTexts: tptCompactFlashDeviceID.setDescription('The unique identifier of the device sending this notification.')
tptCompactFlashDeviceStatus = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 262), PresentOrNot()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptCompactFlashDeviceStatus.setStatus('current')
if mibBuilder.loadTexts: tptCompactFlashDeviceStatus.setDescription('Compact flash status notification.')
tptCFInsertedNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 51)).setObjects(("TPT-COMPACT-FLASH-MIB", "tptCompactFlashDeviceID"), ("TPT-COMPACT-FLASH-MIB", "tptCompactFlashDeviceStatus"))
if mibBuilder.loadTexts: tptCFInsertedNotify.setStatus('current')
if mibBuilder.loadTexts: tptCFInsertedNotify.setDescription('Notification: Compact Flash was inserted on this device')
tptCFEjectedNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 52)).setObjects(("TPT-COMPACT-FLASH-MIB", "tptCompactFlashDeviceID"), ("TPT-COMPACT-FLASH-MIB", "tptCompactFlashDeviceStatus"))
if mibBuilder.loadTexts: tptCFEjectedNotify.setStatus('current')
if mibBuilder.loadTexts: tptCFEjectedNotify.setDescription('Notification: Compact flash was ejected on this device')
mibBuilder.exportSymbols("TPT-COMPACT-FLASH-MIB", model=model, FormattedOrNot=FormattedOrNot, MountedOrNot=MountedOrNot, PresentOrNot=PresentOrNot, tptCompactFlashDeviceID=tptCompactFlashDeviceID, revision=revision, compactFlashPresent=compactFlashPresent, OperationMode=OperationMode, tptCFInsertedNotify=tptCFInsertedNotify, PYSNMP_MODULE_ID=tpt_compact_flash, serialNumber=serialNumber, tptCompactFlashDeviceStatus=tptCompactFlashDeviceStatus, compactFlashMounted=compactFlashMounted, tptCFEjectedNotify=tptCFEjectedNotify, capacity=capacity, vendorInformation=vendorInformation, compactFlashOperationMode=compactFlashOperationMode, compactFlashFormatted=compactFlashFormatted, tpt_compact_flash=tpt_compact_flash)
