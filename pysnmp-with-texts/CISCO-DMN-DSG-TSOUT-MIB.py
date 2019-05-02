#
# PySNMP MIB module CISCO-DMN-DSG-TSOUT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DMN-DSG-TSOUT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:55:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
iso, Unsigned32, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, MibIdentifier, NotificationType, TimeTicks, Counter64, Bits, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "MibIdentifier", "NotificationType", "TimeTicks", "Counter64", "Bits", "Integer32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDSGTSOUT = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34))
ciscoDSGTSOUT.setRevisions(('2012-03-20 11:00', '2010-08-24 07:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDSGTSOUT.setRevisionsDescriptions(('V01.00.01 2012-03-20 Updated for D9854 R4 Release.', 'V01.00.00 2010-08-24 Initial Version.',))
if mibBuilder.loadTexts: ciscoDSGTSOUT.setLastUpdated('201203201130Z')
if mibBuilder.loadTexts: ciscoDSGTSOUT.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDSGTSOUT.setContactInfo('Cisco Systems, Inc. Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553 NETS E-mail: cs-ipsla@cisco.com')
if mibBuilder.loadTexts: ciscoDSGTSOUT.setDescription('Cisco SDI MIB.')
tsoutTable = MibTable((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 1), )
if mibBuilder.loadTexts: tsoutTable.setStatus('current')
if mibBuilder.loadTexts: tsoutTable.setDescription('Transport Stream Output Table.')
tsoutEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 1, 1), ).setIndexNames((0, "CISCO-DMN-DSG-TSOUT-MIB", "tsoutID"))
if mibBuilder.loadTexts: tsoutEntry.setStatus('current')
if mibBuilder.loadTexts: tsoutEntry.setDescription('Entry for Transport Stream output.')
tsoutID = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsoutID.setStatus('current')
if mibBuilder.loadTexts: tsoutID.setDescription('Transport Stream output instance Id.')
tsoutInstanceName = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsoutInstanceName.setStatus('current')
if mibBuilder.loadTexts: tsoutInstanceName.setDescription('Transport Stream output instance name.')
tsoutOutputMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("noOutput", 1), ("passThrough", 2), ("serviceChannelOnly", 3), ("mapPassthrough", 4), ("mapserviceChannelOnly", 5), ("fullDpmControl", 6), ("transcoding", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsoutOutputMode.setStatus('current')
if mibBuilder.loadTexts: tsoutOutputMode.setDescription('Transport Stream output mode selction.')
tsoutDescrambleMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("deScrambled", 1), ("scrambled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsoutDescrambleMode.setStatus('current')
if mibBuilder.loadTexts: tsoutDescrambleMode.setDescription('Transport Stream output descramble mode selction.')
tsoutRateControl = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("auto", 1), ("user", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsoutRateControl.setStatus('current')
if mibBuilder.loadTexts: tsoutRateControl.setDescription('Transport Stream output rate control selction. Auto should not be used if TS mode is Transcoding')
tsoutOutputRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 206000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsoutOutputRate.setStatus('current')
if mibBuilder.loadTexts: tsoutOutputRate.setDescription('Transport Stream output rate selction Range of 0 to 206 Mbps.')
tsoutInsertNullPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsoutInsertNullPkt.setStatus('current')
if mibBuilder.loadTexts: tsoutInsertNullPkt.setDescription('Insert null packet stuffing option.')
tsoutMOIPOutputMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("noOutput", 1), ("passThrough", 2), ("serviceChannelsOnly", 3), ("mapPassthrough", 4), ("mapServiceChannelsOnly", 5), ("fullDpmControl", 6), ("transcoding", 7), ("sptsServiceChannelsOnly", 8), ("sptsMapServiceChannelsOnly", 9), ("sptsFullDpmControl", 10)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsoutMOIPOutputMode.setStatus('current')
if mibBuilder.loadTexts: tsoutMOIPOutputMode.setDescription('MoIP Transport Stream output mode selection.')
tsoutStatusTable = MibTable((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 2), )
if mibBuilder.loadTexts: tsoutStatusTable.setStatus('current')
if mibBuilder.loadTexts: tsoutStatusTable.setDescription('Transport Stream Output Status Table.')
tsoutStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 2, 1), ).setIndexNames((0, "CISCO-DMN-DSG-TSOUT-MIB", "tsoutStatusID"))
if mibBuilder.loadTexts: tsoutStatusEntry.setStatus('current')
if mibBuilder.loadTexts: tsoutStatusEntry.setDescription('Entry for Transport Stream output status.')
tsoutStatusID = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)))
if mibBuilder.loadTexts: tsoutStatusID.setStatus('current')
if mibBuilder.loadTexts: tsoutStatusID.setDescription('Transport Stream output status instance Id.')
tsoutStatusInstanceName = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsoutStatusInstanceName.setStatus('current')
if mibBuilder.loadTexts: tsoutStatusInstanceName.setDescription('Transport Stream output status instance name.')
tsoutStatusRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsoutStatusRate.setStatus('current')
if mibBuilder.loadTexts: tsoutStatusRate.setDescription('Transport Stream output rate status.')
tsoutStatusFree = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsoutStatusFree.setStatus('current')
if mibBuilder.loadTexts: tsoutStatusFree.setDescription('Transport Stream output bandwidth free.')
mibBuilder.exportSymbols("CISCO-DMN-DSG-TSOUT-MIB", tsoutMOIPOutputMode=tsoutMOIPOutputMode, tsoutStatusTable=tsoutStatusTable, ciscoDSGTSOUT=ciscoDSGTSOUT, PYSNMP_MODULE_ID=ciscoDSGTSOUT, tsoutStatusID=tsoutStatusID, tsoutDescrambleMode=tsoutDescrambleMode, tsoutEntry=tsoutEntry, tsoutInsertNullPkt=tsoutInsertNullPkt, tsoutOutputMode=tsoutOutputMode, tsoutStatusEntry=tsoutStatusEntry, tsoutInstanceName=tsoutInstanceName, tsoutRateControl=tsoutRateControl, tsoutOutputRate=tsoutOutputRate, tsoutStatusRate=tsoutStatusRate, tsoutStatusInstanceName=tsoutStatusInstanceName, tsoutTable=tsoutTable, tsoutID=tsoutID, tsoutStatusFree=tsoutStatusFree)
