#
# PySNMP MIB module RBTWS-INFO-RF-DETECT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBTWS-INFO-RF-DETECT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:53:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
RbtwsChannelNum, RbtwsRssi = mibBuilder.importSymbols("RBTWS-AP-TC", "RbtwsChannelNum", "RbtwsRssi")
RbtwsRFDetectNetworkingMode, RbtwsRFDetectClassification, RbtwsRFDetectClassificationReason = mibBuilder.importSymbols("RBTWS-RF-DETECT-TC", "RbtwsRFDetectNetworkingMode", "RbtwsRFDetectClassification", "RbtwsRFDetectClassificationReason")
rbtwsMibs, = mibBuilder.importSymbols("RBTWS-ROOT-MIB", "rbtwsMibs")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, ObjectIdentity, Counter64, MibIdentifier, Unsigned32, Bits, ModuleIdentity, IpAddress, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "Counter64", "MibIdentifier", "Unsigned32", "Bits", "ModuleIdentity", "IpAddress", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32", "iso")
TextualConvention, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "DisplayString")
rbtwsInfoRFDetectMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9))
rbtwsInfoRFDetectMib.setRevisions(('2007-06-27 00:11', '2007-04-18 00:10', '2006-10-11 00:03',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rbtwsInfoRFDetectMib.setRevisionsDescriptions(('v1.2.0: Added one scalar: rbtwsInfoRFDetectCurrentXmtrTableSize (for 6.2 release)', 'v1.1.0: Added three new columnar objects: - rbtwsInfoRFDetectXmtrNetworkingMode, - rbtwsInfoRFDetectXmtrClassification, - rbtwsInfoRFDetectXmtrClassificationReason (for 6.2 release)', 'v1.0.3: Initial version, for 6.0 release',))
if mibBuilder.loadTexts: rbtwsInfoRFDetectMib.setLastUpdated('200708301716Z')
if mibBuilder.loadTexts: rbtwsInfoRFDetectMib.setOrganization('Enterasys Networks')
if mibBuilder.loadTexts: rbtwsInfoRFDetectMib.setContactInfo('www.enterasys.com')
if mibBuilder.loadTexts: rbtwsInfoRFDetectMib.setDescription("RF Detect MIB. Copyright 2007 Enterasys Networks, Inc. All rights reserved. This SNMP Management Information Base Specification (Specification) embodies confidential and proprietary intellectual property. This Specification is supplied 'AS IS' and Enterasys Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
rbtwsInfoRFDetectObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1))
rbtwsInfoRFDetectDataObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1, 1))
rbtwsInfoRFDetectXmtrTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1, 1, 1), )
if mibBuilder.loadTexts: rbtwsInfoRFDetectXmtrTable.setStatus('current')
if mibBuilder.loadTexts: rbtwsInfoRFDetectXmtrTable.setDescription('Transmitter table. May contain tens of thousands of entries (different Transmitter-Listener-Channel combinations).')
rbtwsInfoRFDetectXmtrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1, 1, 1, 1), ).setIndexNames((0, "RBTWS-INFO-RF-DETECT-MIB", "rbtwsInfoRFDetectXmtrTransmitterMacAddress"), (0, "RBTWS-INFO-RF-DETECT-MIB", "rbtwsInfoRFDetectXmtrListenerMacAddress"), (0, "RBTWS-INFO-RF-DETECT-MIB", "rbtwsInfoRFDetectXmtrChannelNum"))
if mibBuilder.loadTexts: rbtwsInfoRFDetectXmtrEntry.setStatus('current')
if mibBuilder.loadTexts: rbtwsInfoRFDetectXmtrEntry.setDescription('Transmitter-Listener-Channel combination.')
rbtwsInfoRFDetectXmtrTransmitterMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1, 1, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: rbtwsInfoRFDetectXmtrTransmitterMacAddress.setStatus('current')
if mibBuilder.loadTexts: rbtwsInfoRFDetectXmtrTransmitterMacAddress.setDescription('The MAC Address of this Transmitter.')
rbtwsInfoRFDetectXmtrListenerMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1, 1, 1, 1, 2), MacAddress())
if mibBuilder.loadTexts: rbtwsInfoRFDetectXmtrListenerMacAddress.setStatus('current')
if mibBuilder.loadTexts: rbtwsInfoRFDetectXmtrListenerMacAddress.setDescription('The MAC Address of this Listener.')
rbtwsInfoRFDetectXmtrChannelNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1, 1, 1, 1, 3), RbtwsChannelNum())
if mibBuilder.loadTexts: rbtwsInfoRFDetectXmtrChannelNum.setStatus('current')
if mibBuilder.loadTexts: rbtwsInfoRFDetectXmtrChannelNum.setDescription('Channel Number this transmitter was using when this listener detected it.')
rbtwsInfoRFDetectXmtrRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1, 1, 1, 1, 4), RbtwsRssi()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbtwsInfoRFDetectXmtrRssi.setStatus('current')
if mibBuilder.loadTexts: rbtwsInfoRFDetectXmtrRssi.setDescription('Received Signal Strength Indicator at this listener.')
rbtwsInfoRFDetectXmtrSsid = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbtwsInfoRFDetectXmtrSsid.setStatus('current')
if mibBuilder.loadTexts: rbtwsInfoRFDetectXmtrSsid.setDescription('The service/SSID name this transmitter was using. Zero-length string when unknown or not applicable.')
rbtwsInfoRFDetectXmtrNetworkingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1, 1, 1, 1, 6), RbtwsRFDetectNetworkingMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbtwsInfoRFDetectXmtrNetworkingMode.setStatus('current')
if mibBuilder.loadTexts: rbtwsInfoRFDetectXmtrNetworkingMode.setDescription('The way this transmitter is doing wireless networking: ad-hoc mode networking or infrastructure mode networking.')
rbtwsInfoRFDetectXmtrClassification = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1, 1, 1, 1, 7), RbtwsRFDetectClassification()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbtwsInfoRFDetectXmtrClassification.setStatus('current')
if mibBuilder.loadTexts: rbtwsInfoRFDetectXmtrClassification.setDescription('The RF classification of this transmitter.')
rbtwsInfoRFDetectXmtrClassificationReason = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1, 1, 1, 1, 8), RbtwsRFDetectClassificationReason()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbtwsInfoRFDetectXmtrClassificationReason.setStatus('current')
if mibBuilder.loadTexts: rbtwsInfoRFDetectXmtrClassificationReason.setDescription('The reason why this transmitter was classified by RF detection the way it is.')
rbtwsInfoRFDetectCurrentXmtrTableSize = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbtwsInfoRFDetectCurrentXmtrTableSize.setStatus('current')
if mibBuilder.loadTexts: rbtwsInfoRFDetectCurrentXmtrTableSize.setDescription('Current number of Transmitter-Listener-Channel combinations found and recorded by RF detection.')
rbtwsInfoRFDetectConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1, 2))
rbtwsInfoRFDetectCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1, 2, 1))
rbtwsInfoRFDetectGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1, 2, 2))
rbtwsInfoRFDetectCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1, 2, 1, 1)).setObjects(("RBTWS-INFO-RF-DETECT-MIB", "rbtwsInfoRFDetectXmtrGroup"), ("RBTWS-INFO-RF-DETECT-MIB", "rbtwsInfoRFDetectXmtrClassificationGroup"), ("RBTWS-INFO-RF-DETECT-MIB", "rbtwsInfoRFDetectCurrentXmtrTableSizeGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbtwsInfoRFDetectCompliance = rbtwsInfoRFDetectCompliance.setStatus('current')
if mibBuilder.loadTexts: rbtwsInfoRFDetectCompliance.setDescription('The compliance statement for devices that implement the RF Detect MIB.')
rbtwsInfoRFDetectXmtrGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1, 2, 2, 1)).setObjects(("RBTWS-INFO-RF-DETECT-MIB", "rbtwsInfoRFDetectXmtrRssi"), ("RBTWS-INFO-RF-DETECT-MIB", "rbtwsInfoRFDetectXmtrSsid"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbtwsInfoRFDetectXmtrGroup = rbtwsInfoRFDetectXmtrGroup.setStatus('current')
if mibBuilder.loadTexts: rbtwsInfoRFDetectXmtrGroup.setDescription('Mandatory group of objects implemented to provide RF Detect Transmitter info.')
rbtwsInfoRFDetectXmtrClassificationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1, 2, 2, 2)).setObjects(("RBTWS-INFO-RF-DETECT-MIB", "rbtwsInfoRFDetectXmtrNetworkingMode"), ("RBTWS-INFO-RF-DETECT-MIB", "rbtwsInfoRFDetectXmtrClassification"), ("RBTWS-INFO-RF-DETECT-MIB", "rbtwsInfoRFDetectXmtrClassificationReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbtwsInfoRFDetectXmtrClassificationGroup = rbtwsInfoRFDetectXmtrClassificationGroup.setStatus('current')
if mibBuilder.loadTexts: rbtwsInfoRFDetectXmtrClassificationGroup.setDescription('Group of objects implemented to provide RF Detect Classification info. Introduced in 6.2 release.')
rbtwsInfoRFDetectCurrentXmtrTableSizeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 9, 1, 2, 2, 3)).setObjects(("RBTWS-INFO-RF-DETECT-MIB", "rbtwsInfoRFDetectCurrentXmtrTableSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbtwsInfoRFDetectCurrentXmtrTableSizeGroup = rbtwsInfoRFDetectCurrentXmtrTableSizeGroup.setStatus('current')
if mibBuilder.loadTexts: rbtwsInfoRFDetectCurrentXmtrTableSizeGroup.setDescription('Group for one object that provides the current number of Transmitter-Listener-Channel combinations found and recorded by RF detection. Introduced in 6.2 release.')
mibBuilder.exportSymbols("RBTWS-INFO-RF-DETECT-MIB", rbtwsInfoRFDetectXmtrGroup=rbtwsInfoRFDetectXmtrGroup, rbtwsInfoRFDetectXmtrClassificationReason=rbtwsInfoRFDetectXmtrClassificationReason, rbtwsInfoRFDetectXmtrListenerMacAddress=rbtwsInfoRFDetectXmtrListenerMacAddress, rbtwsInfoRFDetectXmtrRssi=rbtwsInfoRFDetectXmtrRssi, rbtwsInfoRFDetectXmtrTransmitterMacAddress=rbtwsInfoRFDetectXmtrTransmitterMacAddress, rbtwsInfoRFDetectXmtrChannelNum=rbtwsInfoRFDetectXmtrChannelNum, rbtwsInfoRFDetectCompliances=rbtwsInfoRFDetectCompliances, rbtwsInfoRFDetectConformance=rbtwsInfoRFDetectConformance, rbtwsInfoRFDetectGroups=rbtwsInfoRFDetectGroups, rbtwsInfoRFDetectXmtrSsid=rbtwsInfoRFDetectXmtrSsid, rbtwsInfoRFDetectMib=rbtwsInfoRFDetectMib, rbtwsInfoRFDetectObjects=rbtwsInfoRFDetectObjects, rbtwsInfoRFDetectDataObjects=rbtwsInfoRFDetectDataObjects, rbtwsInfoRFDetectCompliance=rbtwsInfoRFDetectCompliance, rbtwsInfoRFDetectXmtrEntry=rbtwsInfoRFDetectXmtrEntry, PYSNMP_MODULE_ID=rbtwsInfoRFDetectMib, rbtwsInfoRFDetectXmtrTable=rbtwsInfoRFDetectXmtrTable, rbtwsInfoRFDetectXmtrNetworkingMode=rbtwsInfoRFDetectXmtrNetworkingMode, rbtwsInfoRFDetectCurrentXmtrTableSizeGroup=rbtwsInfoRFDetectCurrentXmtrTableSizeGroup, rbtwsInfoRFDetectCurrentXmtrTableSize=rbtwsInfoRFDetectCurrentXmtrTableSize, rbtwsInfoRFDetectXmtrClassificationGroup=rbtwsInfoRFDetectXmtrClassificationGroup, rbtwsInfoRFDetectXmtrClassification=rbtwsInfoRFDetectXmtrClassification)
