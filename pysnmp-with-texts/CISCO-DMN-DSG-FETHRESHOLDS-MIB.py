#
# PySNMP MIB module CISCO-DMN-DSG-FETHRESHOLDS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DMN-DSG-FETHRESHOLDS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:55:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, NotificationType, Unsigned32, iso, Gauge32, Counter32, Bits, Counter64, MibIdentifier, ObjectIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "NotificationType", "Unsigned32", "iso", "Gauge32", "Counter32", "Bits", "Counter64", "MibIdentifier", "ObjectIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoDSGFeThresholds = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 9))
ciscoDSGFeThresholds.setRevisions(('2010-08-30 11:00', '2010-04-26 05:00', '2010-03-22 05:00', '2009-12-07 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDSGFeThresholds.setRevisionsDescriptions(('V01.00.03 2010-08-30 Updated for adherence to SNMPv2 format.', 'V01.00.02 2010-04-26 The name of MIB objects are modified to make the terminology common across the OSD, WebUI and MIB.', 'V01.00.01 2010-03-22 The Syntax of Unsigned32 MIB objects whose range is within the range of Integer32, is updated to Integer32.', 'V01.00.00 2009-12-07 Initial Version.',))
if mibBuilder.loadTexts: ciscoDSGFeThresholds.setLastUpdated('201008301100Z')
if mibBuilder.loadTexts: ciscoDSGFeThresholds.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDSGFeThresholds.setContactInfo('Cisco Systems, Inc. Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553 NETS E-mail: cs-ipsla@cisco.com')
if mibBuilder.loadTexts: ciscoDSGFeThresholds.setDescription('Cisco FE Muting Thresholds MIB.')
mutingThresholdsTable = MibTable((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 9, 1), )
if mibBuilder.loadTexts: mutingThresholdsTable.setStatus('current')
if mibBuilder.loadTexts: mutingThresholdsTable.setDescription('Muting Thresholds Table.')
mutingThresholdsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 9, 1, 1), ).setIndexNames((0, "CISCO-DMN-DSG-FETHRESHOLDS-MIB", "mutingThreshholdsInstance"))
if mibBuilder.loadTexts: mutingThresholdsEntry.setStatus('current')
if mibBuilder.loadTexts: mutingThresholdsEntry.setDescription('Entry for Muting Thresholds Table.')
mutingThreshholdsInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 9, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1)))
if mibBuilder.loadTexts: mutingThreshholdsInstance.setStatus('current')
if mibBuilder.loadTexts: mutingThreshholdsInstance.setDescription('Instance for Muting Thresholds Table.')
mutThreshRestoreDefaults = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 9, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("writeOnly", 1), ("yes", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mutThreshRestoreDefaults.setStatus('current')
if mibBuilder.loadTexts: mutThreshRestoreDefaults.setDescription('Control restores software defaults to the Muting Thresholds. When set to yes( 2 ) it restores Default Muting BER Levels.')
mutThreshControl = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 9, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mutThreshControl.setStatus('current')
if mibBuilder.loadTexts: mutThreshControl.setDescription('Turns on or off the muting algorithm.')
mutThreshDVBSTransportMute = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 9, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-50, 200))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mutThreshDVBSTransportMute.setStatus('current')
if mibBuilder.loadTexts: mutThreshDVBSTransportMute.setDescription('Transport Mute CN Margin ( DVB-S )in dB in steps of 1. The scaling factor is 1/10.')
mutThreshDVBSTransportRestore = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 9, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-50, 200))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mutThreshDVBSTransportRestore.setStatus('current')
if mibBuilder.loadTexts: mutThreshDVBSTransportRestore.setDescription('Transport Restore CN Margin ( DVB-S )in dB in steps of 1. The scaling factor is 1/10..')
mutThreshDVBSAudioMute = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 9, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-50, 200))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mutThreshDVBSAudioMute.setStatus('current')
if mibBuilder.loadTexts: mutThreshDVBSAudioMute.setDescription('Audio Mute CN Margin ( DVB-S )in dB in steps of 1. The scaling factor is 1/10.')
mutThreshDVBSAudioRestore = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 9, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-50, 200))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mutThreshDVBSAudioRestore.setStatus('current')
if mibBuilder.loadTexts: mutThreshDVBSAudioRestore.setDescription('Audio Restore CN Margin ( DVB-S )in dB in steps of 1. The scaling factor is 1/10.')
mutThreshDVBS2TransportMute = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 9, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-50, 200))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mutThreshDVBS2TransportMute.setStatus('current')
if mibBuilder.loadTexts: mutThreshDVBS2TransportMute.setDescription('Transport Mute CN Margin ( DVB-S2 )in dB in steps of 1. The scaling factor is 1/10.')
mutThreshDVBS2TransportRestore = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 9, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-50, 200))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mutThreshDVBS2TransportRestore.setStatus('current')
if mibBuilder.loadTexts: mutThreshDVBS2TransportRestore.setDescription('Transport Restore CN Margin ( DVB-S2 )in dB in steps of 1. The scaling factor is 1/10.')
mutThreshDVBS2AudioMute = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 9, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-50, 200))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mutThreshDVBS2AudioMute.setStatus('current')
if mibBuilder.loadTexts: mutThreshDVBS2AudioMute.setDescription('Audio Mute CN Margin (DVB-S2)in dB in steps of 1. The scaling factor is 1/10.')
mutThreshDVBS2AudioRestore = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 9, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-50, 200))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mutThreshDVBS2AudioRestore.setStatus('current')
if mibBuilder.loadTexts: mutThreshDVBS2AudioRestore.setDescription('Audio Restore Margin ( DVB-S2 ) in dB in steps of 1. The scaling factor is 1/10.')
mibBuilder.exportSymbols("CISCO-DMN-DSG-FETHRESHOLDS-MIB", PYSNMP_MODULE_ID=ciscoDSGFeThresholds, mutThreshDVBS2TransportRestore=mutThreshDVBS2TransportRestore, mutThreshDVBS2AudioRestore=mutThreshDVBS2AudioRestore, mutThreshDVBSAudioMute=mutThreshDVBSAudioMute, ciscoDSGFeThresholds=ciscoDSGFeThresholds, mutThreshRestoreDefaults=mutThreshRestoreDefaults, mutThreshControl=mutThreshControl, mutThreshDVBSTransportMute=mutThreshDVBSTransportMute, mutThreshDVBS2TransportMute=mutThreshDVBS2TransportMute, mutThreshDVBSAudioRestore=mutThreshDVBSAudioRestore, mutingThresholdsEntry=mutingThresholdsEntry, mutingThreshholdsInstance=mutingThreshholdsInstance, mutThreshDVBSTransportRestore=mutThreshDVBSTransportRestore, mutThreshDVBS2AudioMute=mutThreshDVBS2AudioMute, mutingThresholdsTable=mutingThresholdsTable)
