#
# PySNMP MIB module DNOS-LLPF-PRIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DNOS-LLPF-PRIVATE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:36:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
dnOS, = mibBuilder.importSymbols("DELL-REF-MIB", "dnOS")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, ObjectIdentity, Gauge32, Counter64, MibIdentifier, iso, TimeTicks, Integer32, Unsigned32, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "Gauge32", "Counter64", "MibIdentifier", "iso", "TimeTicks", "Integer32", "Unsigned32", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType")
RowStatus, MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "MacAddress", "TextualConvention", "DisplayString")
fastPathLlpf = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 48))
fastPathLlpf.setRevisions(('2011-01-26 00:00', '2009-10-26 00:00',))
if mibBuilder.loadTexts: fastPathLlpf.setLastUpdated('201101260000Z')
if mibBuilder.loadTexts: fastPathLlpf.setOrganization('Dell, Inc.')
agentSwitchLlpfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 48, 1))
agentSwitchLlpfPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 48, 1, 1), )
if mibBuilder.loadTexts: agentSwitchLlpfPortConfigTable.setStatus('current')
agentSwitchLlpfPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 48, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "DNOS-LLPF-PRIVATE-MIB", "agentSwitchLlpfProtocolType"))
if mibBuilder.loadTexts: agentSwitchLlpfPortConfigEntry.setStatus('current')
agentSwitchLlpfProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 48, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 6)))
if mibBuilder.loadTexts: agentSwitchLlpfProtocolType.setStatus('current')
agentSwitchLlpfPortBlockMode = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 48, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSwitchLlpfPortBlockMode.setStatus('current')
mibBuilder.exportSymbols("DNOS-LLPF-PRIVATE-MIB", agentSwitchLlpfPortConfigTable=agentSwitchLlpfPortConfigTable, agentSwitchLlpfPortBlockMode=agentSwitchLlpfPortBlockMode, agentSwitchLlpfPortConfigEntry=agentSwitchLlpfPortConfigEntry, agentSwitchLlpfGroup=agentSwitchLlpfGroup, PYSNMP_MODULE_ID=fastPathLlpf, fastPathLlpf=fastPathLlpf, agentSwitchLlpfProtocolType=agentSwitchLlpfProtocolType)
