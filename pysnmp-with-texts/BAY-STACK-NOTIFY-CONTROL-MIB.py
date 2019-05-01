#
# PySNMP MIB module BAY-STACK-NOTIFY-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BAY-STACK-NOTIFY-CONTROL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:36:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ModuleIdentity, ObjectIdentity, Counter64, Gauge32, iso, Bits, Integer32, NotificationType, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ModuleIdentity", "ObjectIdentity", "Counter64", "Gauge32", "iso", "Bits", "Integer32", "NotificationType", "Counter32", "IpAddress")
RowStatus, TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "TruthValue", "DisplayString")
bayStackMibs, = mibBuilder.importSymbols("SYNOPTICS-ROOT-MIB", "bayStackMibs")
bayStackNotifyControlMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 5, 31))
bayStackNotifyControlMib.setRevisions(('2010-09-08 00:00', '2008-10-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bayStackNotifyControlMib.setRevisionsDescriptions(('v2: Added bsncNotifyControlPortListEnabled.', 'v1: Initial version.',))
if mibBuilder.loadTexts: bayStackNotifyControlMib.setLastUpdated('201009080000Z')
if mibBuilder.loadTexts: bayStackNotifyControlMib.setOrganization('Avaya')
if mibBuilder.loadTexts: bayStackNotifyControlMib.setContactInfo('Avaya')
if mibBuilder.loadTexts: bayStackNotifyControlMib.setDescription("Avaya Notification Control MIB Copyright 2008-2010 Avaya, Inc. All rights reserved. This Avaya SNMP Management Information Base Specification embodies Avaya's confidential and proprietary intellectual property. Avaya retains all title and ownership in the Specification, including any revisions. This Specification is supplied 'AS IS,' and Avaya makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
bsncObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 31, 1))
bsncNotifyControlTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 31, 1, 1), )
if mibBuilder.loadTexts: bsncNotifyControlTable.setStatus('current')
if mibBuilder.loadTexts: bsncNotifyControlTable.setDescription('This table is used to control generation of individual SNMP notification types. The table is indexed by the OID of the NOTIFICATION-TYPE, and contains a flag to enable or disable generation of that notification type.')
bsncNotifyControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 31, 1, 1, 1), ).setIndexNames((0, "BAY-STACK-NOTIFY-CONTROL-MIB", "bsncNotifyControlType"))
if mibBuilder.loadTexts: bsncNotifyControlEntry.setStatus('current')
if mibBuilder.loadTexts: bsncNotifyControlEntry.setDescription('Each entry contains a flag to control generation of a specific notification type.')
bsncNotifyControlType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 31, 1, 1, 1, 1), ObjectIdentifier())
if mibBuilder.loadTexts: bsncNotifyControlType.setStatus('current')
if mibBuilder.loadTexts: bsncNotifyControlType.setDescription('The OID of a NOTIFICATION-TYPE. Note that this object cannot exceed a length of 114 sub-identifiers.')
bsncNotifyControlEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 31, 1, 1, 1, 2), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsncNotifyControlEnabled.setStatus('current')
if mibBuilder.loadTexts: bsncNotifyControlEnabled.setDescription('Indicates whether this notification type may be generated.')
bsncNotifyControlRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 31, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsncNotifyControlRowStatus.setStatus('current')
if mibBuilder.loadTexts: bsncNotifyControlRowStatus.setDescription('Used to create/delete entries in the table. Note that an implementation may simply provide permanent entries for every supported NOTIFICATION-TYPE.')
bsncNotifyControlPortListEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 31, 1, 1, 1, 4), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsncNotifyControlPortListEnabled.setStatus('current')
if mibBuilder.loadTexts: bsncNotifyControlPortListEnabled.setDescription('Indicates the interface port list for which the notification is enabled or disabled, subject to the bsncNotifyControlEnabled value. Note that for a global notification type, the value of this object is always an empty string.')
mibBuilder.exportSymbols("BAY-STACK-NOTIFY-CONTROL-MIB", bayStackNotifyControlMib=bayStackNotifyControlMib, bsncNotifyControlEntry=bsncNotifyControlEntry, bsncNotifyControlEnabled=bsncNotifyControlEnabled, bsncNotifyControlTable=bsncNotifyControlTable, bsncNotifyControlRowStatus=bsncNotifyControlRowStatus, bsncObjects=bsncObjects, PYSNMP_MODULE_ID=bayStackNotifyControlMib, bsncNotifyControlType=bsncNotifyControlType, bsncNotifyControlPortListEnabled=bsncNotifyControlPortListEnabled)