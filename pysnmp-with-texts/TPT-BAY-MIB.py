#
# PySNMP MIB module TPT-BAY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPT-BAY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:26:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, MibIdentifier, ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, Gauge32, ObjectIdentity, IpAddress, iso, Counter32, NotificationType, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "Gauge32", "ObjectIdentity", "IpAddress", "iso", "Counter32", "NotificationType", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tpt_tpa_unkparams, tpt_tpa_objs, tpt_tpa_eventsV2 = mibBuilder.importSymbols("TPT-TPAMIBS-MIB", "tpt-tpa-unkparams", "tpt-tpa-objs", "tpt-tpa-eventsV2")
tpt_slot_objs = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 17)).setLabel("tpt-slot-objs")
tpt_slot_objs.setRevisions(('2016-05-25 18:54',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tpt_slot_objs.setRevisionsDescriptions(('Updated copyright information. Minor MIB syntax fixes.',))
if mibBuilder.loadTexts: tpt_slot_objs.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tpt_slot_objs.setOrganization('Trend Micro, Inc.')
if mibBuilder.loadTexts: tpt_slot_objs.setContactInfo('www.trendmicro.com')
if mibBuilder.loadTexts: tpt_slot_objs.setDescription("Slot details on the device. Copyright (C) 2016 Trend Micro Incorporated. All Rights Reserved. Trend Micro makes no warranty of any kind with regard to this material, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose. Trend Micro shall not be liable for errors contained herein or for incidental or consequential damages in connection with the furnishing, performance, or use of this material. This document contains proprietary information, which is protected by copyright. No part of this document may be photocopied, reproduced, or translated into another language without the prior written consent of Trend Micro. The information is provided 'as is' without warranty of any kind and is subject to change without notice. The only warranties for Trend Micro products and services are set forth in the express warranty statements accompanying such products and services. Nothing herein should be construed as constituting an additional warranty. Trend Micro shall not be liable for technical or editorial errors or omissions contained herein. TippingPoint(R), the TippingPoint logo, and Digital Vaccine(R) are registered trademarks of Trend Micro. All other company and product names may be trademarks of their respective holders. All rights reserved. This document contains confidential information, trade secrets or both, which are the property of Trend Micro. No part of this documentation may be reproduced in any form or by any means or used to make any derivative work (such as translation, transformation, or adaptation) without written permission from Trend Micro or one of its subsidiaries. All other company and product names may be trademarks of their respective holders. ")
class SlotStatus(TextualConvention, Integer32):
    description = 'An indication of slot status'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("empty", 0), ("active", 1), ("error", 2))

class SlotEvent(TextualConvention, Integer32):
    description = 'An indication of events occuring in slot'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("insert", 0), ("remove", 1))

class SlotModuleType(TextualConvention, Integer32):
    description = 'Type of module present in the slot. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))
    namedValues = NamedValues(("type-12-port-1g-copper", 1), ("type-12-port-1g-sfp", 2), ("type-8-port-10g-sfp", 3), ("type-2-port-40g-sfp", 4), ("type-6100", 5), ("type-5100", 6), ("type-2500", 7), ("type-1400", 8), ("type-660", 9), ("type-330", 10), ("type-110", 11), ("type-10", 12), ("type-empty", 13), ("type-8-port-1g-copper-bypass", 14), ("type-4-port-1g-sfp-sr-bypass", 15), ("type-4-port-1g-sfp-lr-bypass", 16), ("type-4-port-10g-sfp-sr-bypass", 17), ("type-4-port-10g-sfp-lr-bypass", 18))

slotTempTable = MibTable((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 17, 1), )
if mibBuilder.loadTexts: slotTempTable.setStatus('current')
if mibBuilder.loadTexts: slotTempTable.setDescription('Table of slots on the device.')
slotTempEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 17, 1, 1), ).setIndexNames((0, "TPT-BAY-MIB", "slotTempIndex"))
if mibBuilder.loadTexts: slotTempEntry.setStatus('current')
if mibBuilder.loadTexts: slotTempEntry.setDescription('An entry in the slot table. Rows cannot be created or deleted.')
slotTempIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 17, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: slotTempIndex.setStatus('current')
if mibBuilder.loadTexts: slotTempIndex.setDescription('Index into the slot table, starting with 1.')
slotName = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 17, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotName.setStatus('current')
if mibBuilder.loadTexts: slotName.setDescription('String description of the name of slot.')
slotModuleName = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 17, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotModuleName.setStatus('current')
if mibBuilder.loadTexts: slotModuleName.setDescription('String description of the type of module in slot.')
slotStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 17, 1, 1, 4), SlotStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotStatus.setStatus('current')
if mibBuilder.loadTexts: slotStatus.setDescription('status of this slot')
slotModuleSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 17, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotModuleSerialNum.setStatus('current')
if mibBuilder.loadTexts: slotModuleSerialNum.setDescription('String description of the serial number of the module in the slot.')
slotModuleType = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 17, 1, 1, 6), SlotModuleType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotModuleType.setStatus('current')
if mibBuilder.loadTexts: slotModuleType.setDescription("Type of module present in the slot. This is applicable mainly for the newer devices like 6100 and above, which have multiple I/O slots. For older systems like 5100 which don't have slots, the module type would be the device model number.")
tptSlotDeviceID = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 281), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptSlotDeviceID.setStatus('current')
if mibBuilder.loadTexts: tptSlotDeviceID.setDescription('The unique identifier of the device sending this notification.')
tptSlotID = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 282), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptSlotID.setStatus('current')
if mibBuilder.loadTexts: tptSlotID.setDescription('The slot index which is sending this notification.')
tptSlotEvent = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 283), SlotEvent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptSlotEvent.setStatus('current')
if mibBuilder.loadTexts: tptSlotEvent.setDescription('The event occuring in the slot which is sending this notification.')
tptSlotChangeNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 54)).setObjects(("TPT-BAY-MIB", "tptSlotDeviceID"), ("TPT-BAY-MIB", "tptSlotID"), ("TPT-BAY-MIB", "tptSlotEvent"))
if mibBuilder.loadTexts: tptSlotChangeNotify.setStatus('current')
if mibBuilder.loadTexts: tptSlotChangeNotify.setDescription('Notification: Module was inserted on this device')
mibBuilder.exportSymbols("TPT-BAY-MIB", slotModuleName=slotModuleName, slotStatus=slotStatus, slotModuleSerialNum=slotModuleSerialNum, SlotEvent=SlotEvent, slotModuleType=slotModuleType, slotTempIndex=slotTempIndex, slotTempTable=slotTempTable, tptSlotDeviceID=tptSlotDeviceID, PYSNMP_MODULE_ID=tpt_slot_objs, slotName=slotName, SlotModuleType=SlotModuleType, tptSlotChangeNotify=tptSlotChangeNotify, tptSlotID=tptSlotID, tpt_slot_objs=tpt_slot_objs, SlotStatus=SlotStatus, slotTempEntry=slotTempEntry, tptSlotEvent=tptSlotEvent)
