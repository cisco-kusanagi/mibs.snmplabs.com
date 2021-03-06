#
# PySNMP MIB module INTEL-DHCPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/INTEL-DHCPS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:42:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
mib2ext, = mibBuilder.importSymbols("INTEL-GEN-MIB", "mib2ext")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, ModuleIdentity, Bits, Integer32, NotificationType, iso, TimeTicks, Gauge32, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ModuleIdentity", "Bits", "Integer32", "NotificationType", "iso", "TimeTicks", "Gauge32", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dhcps = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 7))
dhcpsInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 7, 1))
dhcpsConf = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 7, 2))
dhcpsInfoTable = MibTable((1, 3, 6, 1, 4, 1, 343, 6, 7, 1, 1), )
if mibBuilder.loadTexts: dhcpsInfoTable.setStatus('mandatory')
dhcpsInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 343, 6, 7, 1, 1, 1), ).setIndexNames((0, "INTEL-DHCPS-MIB", "dhcpsInfoHostAddress"))
if mibBuilder.loadTexts: dhcpsInfoEntry.setStatus('mandatory')
dhcpsInfoHostAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 7, 1, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpsInfoHostAddress.setStatus('mandatory')
dhcpsInfoMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 7, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpsInfoMacAddress.setStatus('mandatory')
dhcpsInfoHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 7, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(20, 20)).setFixedLength(20)).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpsInfoHostName.setStatus('mandatory')
dhcpsInfoAge = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 7, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpsInfoAge.setStatus('mandatory')
dhcpsInfoState = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 7, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("deleted", 1), ("declined", 2), ("offered", 3), ("assigned", 4), ("modified", 5), ("pinged", 6), ("reserved", 7), ("released", 8), ("obsolete", 9)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpsInfoState.setStatus('mandatory')
dhcpsConfInfoTable = MibTable((1, 3, 6, 1, 4, 1, 343, 6, 7, 2, 1), )
if mibBuilder.loadTexts: dhcpsConfInfoTable.setStatus('mandatory')
dhcpsConfInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 343, 6, 7, 2, 1, 1), ).setIndexNames((0, "INTEL-DHCPS-MIB", "dhcpsConfInfoId"))
if mibBuilder.loadTexts: dhcpsConfInfoEntry.setStatus('mandatory')
dhcpsConfInfoId = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 7, 2, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpsConfInfoId.setStatus('mandatory')
dhcpsConfInfoHandle = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 7, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpsConfInfoHandle.setStatus('mandatory')
dhcpsConfInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 7, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noTable", 1), ("tableIndexSize0", 2), ("tableIndexSize1", 3), ("tableIndexSize2", 4), ("tableIndexSize4", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpsConfInfoType.setStatus('mandatory')
dhcpsConfInfoTableOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 7, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpsConfInfoTableOffset.setStatus('mandatory')
dhcpsConfInfoIndexOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 7, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpsConfInfoIndexOffset.setStatus('mandatory')
dhcpsConfInfoRecordCount = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 7, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpsConfInfoRecordCount.setStatus('mandatory')
dhcpsConfInfoRecordLength = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 7, 2, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpsConfInfoRecordLength.setStatus('mandatory')
dhcpsConfTable = MibTable((1, 3, 6, 1, 4, 1, 343, 6, 7, 2, 2), )
if mibBuilder.loadTexts: dhcpsConfTable.setStatus('mandatory')
dhcpsConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 343, 6, 7, 2, 2, 1), ).setIndexNames((0, "INTEL-DHCPS-MIB", "dhcpsConfId"), (0, "INTEL-DHCPS-MIB", "dhcpsConfIndex"), (0, "INTEL-DHCPS-MIB", "dhcpsConfHandle"))
if mibBuilder.loadTexts: dhcpsConfEntry.setStatus('mandatory')
dhcpsConfId = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 7, 2, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpsConfId.setStatus('mandatory')
dhcpsConfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 7, 2, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpsConfIndex.setStatus('mandatory')
dhcpsConfHandle = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 7, 2, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpsConfHandle.setStatus('mandatory')
dhcpsConfData = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 7, 2, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(255, 255)).setFixedLength(255)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpsConfData.setStatus('mandatory')
dhcpsConfOptions = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 7, 2, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpsConfOptions.setStatus('mandatory')
dhcpsConfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 7, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("delete", 2), ("copy", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpsConfStatus.setStatus('mandatory')
mibBuilder.exportSymbols("INTEL-DHCPS-MIB", dhcpsConf=dhcpsConf, dhcpsInfoEntry=dhcpsInfoEntry, dhcpsConfInfoEntry=dhcpsConfInfoEntry, dhcpsInfoHostAddress=dhcpsInfoHostAddress, dhcpsConfId=dhcpsConfId, dhcpsInfo=dhcpsInfo, dhcpsConfInfoHandle=dhcpsConfInfoHandle, dhcpsConfInfoTableOffset=dhcpsConfInfoTableOffset, dhcpsConfData=dhcpsConfData, dhcps=dhcps, dhcpsInfoTable=dhcpsInfoTable, dhcpsInfoAge=dhcpsInfoAge, dhcpsConfStatus=dhcpsConfStatus, dhcpsConfInfoRecordCount=dhcpsConfInfoRecordCount, dhcpsInfoState=dhcpsInfoState, dhcpsConfTable=dhcpsConfTable, dhcpsInfoHostName=dhcpsInfoHostName, dhcpsConfInfoRecordLength=dhcpsConfInfoRecordLength, dhcpsConfInfoIndexOffset=dhcpsConfInfoIndexOffset, dhcpsConfHandle=dhcpsConfHandle, dhcpsConfInfoType=dhcpsConfInfoType, dhcpsConfEntry=dhcpsConfEntry, dhcpsConfIndex=dhcpsConfIndex, dhcpsConfInfoTable=dhcpsConfInfoTable, dhcpsConfOptions=dhcpsConfOptions, dhcpsInfoMacAddress=dhcpsInfoMacAddress, dhcpsConfInfoId=dhcpsConfInfoId)
